pragma solidity ^0.4.24;

import "./ERC20.sol";
import "./../../identity-smart-contract/contracts/IdentityStore.sol";

contract CorpCoin is EIP20Interface {
    
    IdentityStore idStore;
    uint256 expiration = 30 days;
    uint numberOfCoins = 4;
    uint256 constant private MAX_UINT256 = 2**256 - 1;
    mapping (address => uint256) public balances;
    mapping (address => mapping (address => uint256)) public allowed;
    mapping (address => bool) private coinAllocated;

    function CorpCoin(address addr, uint256 _initialAmount) public {
        idStore = IdentityStore(addr);
        balances[msg.sender] = _initialAmount;
        totalSupply = _initialAmount;
    }

    function InitializeCoinToUser(address _to) public {
        require(coinAllocated[_to] == false);
        require(idStore.isValid(_to, 0), "User not valid for transfer");
        if( totalSupply - numberOfCoins >= 0) {
            balances[_to] += numberOfCoins;
            totalSupply -= numberOfCoins;
            coinAllocated[_to] = true;
        }
    }

    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balances[msg.sender] >= _value);
        require(idStore.isValid(_to, 0), "User not valid for transfer");
        balances[msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(msg.sender, _to, _value); 
        return true;
    }

    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        uint256 allowance = allowed[_from][msg.sender];
        require(balances[_from] >= _value && allowance >= _value);
        balances[_to] += _value;
        balances[_from] -= _value;
        if (allowance < MAX_UINT256) {
            allowed[_from][msg.sender] -= _value;
        }
        emit Transfer(_from, _to, _value); 
        return true;
    }

    function balanceOf(address _owner) public view returns (uint256 balance) {
        return balances[_owner];
    }

    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowed[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value); 
        return true;
    }

    function allowance(address _owner, address _spender) public view returns (uint256 remaining) {
        return allowed[_owner][_spender];
    }
}