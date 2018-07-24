pragma solidity ^0.4.24;

import 'openzeppelin-solidity/contracts/ownership/Ownable.sol';

contract IdentityInterface is Ownable{
    
    function isValid(string _tenantId, address _userAddress, uint256 _minTimestamp) view public returns(bool){}

    function setTenant(bytes32 _tenantHash, address _userAddress, uint256 _timestamp, string _tenantId) onlyOwner public{}

}