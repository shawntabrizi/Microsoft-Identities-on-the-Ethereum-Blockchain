pragma solidity ^0.4.24;

import "openzeppelin-solidity/contracts/ownership/Ownable.sol";

contract IdentityStore is Ownable {

    struct User {
        string tenantId;
        uint256 timestamp;
    }

    mapping(address => User) public tenantMapping;

    mapping(bytes32 => address) public tenantHashMapping; 
    
    function setTenant(
        bytes32 _tenantHash,
        address _userAddress,
        string _tenantId) onlyOwner public {
        
        User memory newUser = User(_tenantId, block.timestamp);

        tenantMapping[_userAddress] = newUser;
        tenantHashMapping[_tenantHash] = _userAddress;
    }   
}