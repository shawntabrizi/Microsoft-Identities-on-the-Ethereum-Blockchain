pragma solidity ^0.4.24;

import "openzeppelin-solidity/contracts/ownership/Ownable.sol";

contract IdentityStore is Ownable {

    struct User {
        bytes32 tenantHash;
        uint256 timestamp;
    }

    mapping(address => User) private tenantAddressMapping;
    mapping(bytes32 => address) private tenantHashMapping; 

    function setTenant(
        bytes32 _tenantHash,
        address _userAddress,
        uint256 _timestamp) onlyOwner public {

        require(!userAddressExists(_userAddress));
        require(!userTenantHashExists(_tenantHash));

        User memory newUser = User(_tenantHash, _timestamp);
        
        tenantAddressMapping[_userAddress] = newUser;
        tenantHashMapping[_tenantHash] = _userAddress;
    }

    function updateHash(
        bytes32 _oldHash, 
        bytes32 _newHash, 
        uint256 _timestamp) onlyOwner public {

        require(userTenantHashExists(_oldHash), "Old hash does not exist.");
        require(!userTenantHashExists(_newHash), "New hash is already registered.");
        address currentAddress = tenantHashMapping[_oldHash];
        User memory newUserInfo = User(_newHash, _timestamp);

        // update address mapping to user
        tenantAddressMapping[currentAddress] = newUserInfo;

        // delete old hash mapping to address
        delete tenantHashMapping[_oldHash];

        // add new hash mapping to address
        tenantHashMapping[_newHash] = currentAddress;
    }


    function userAddressExists(address userAddress) view public returns(bool) {       
        if(tenantAddressMapping[userAddress].timestamp == 0) {
            return false;
        }
        return true;
    }

    function userTenantHashExists(bytes32 tenantHash) view public returns(bool){
        if(tenantHashMapping[tenantHash] == 0) {
            return false;
        }
        return true;
    }

    function updateAddress (address oldUserAddress, address newUserAddress) public {
        User memory existingUser = tenantAddressMapping[oldUserAddress];
        
        require(!userAddressExists(newUserAddress));
        require(userAddressExists(oldUserAddress));

        tenantHashMapping[existingUser.tenantHash] = newUserAddress;
        tenantAddressMapping[newUserAddress] = existingUser;
        delete tenantAddressMapping[oldUserAddress];
    }


}