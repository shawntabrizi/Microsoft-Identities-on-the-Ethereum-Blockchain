pragma solidity ^0.4.24;

import "openzeppelin-solidity/contracts/ownership/Ownable.sol";

contract IdentityStore is Ownable {

    mapping(address => string) public tenantMapping;
    
    function setTenant(address _user, string _tenant) public {
        tenantMapping[_user] = _tenant;
    }
    
    function isAlive() public pure returns(bool alive) {
        return false;
    }
    
}