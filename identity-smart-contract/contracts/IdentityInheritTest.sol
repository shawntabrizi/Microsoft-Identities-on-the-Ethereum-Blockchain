pragma solidity ^0.4.24;

import "contracts/IdentityStore_Sample.sol";
contract IdentityStoreInherit is IdentityStore {
    function updateHashPublic(
        bytes32 _oldHash, 
        bytes32 _newHash, 
        uint256 _timestamp) public {
        updateHash(_oldHash,_newHash, _timestamp);
    }

    function updateAddressPublic(
        address oldUserAddress, 
        address newUserAddress) public  {
        updateAddress(oldUserAddress,newUserAddress);
    }

    function updateTimestampPublic(
        bytes32 _tenantHash, 
        uint256 _timestamp) public  {
        updateTimestamp(_tenantHash,_timestamp);
    }

    function userAddressExistsPublic(
        address userAddress) public returns(bool) {
        return userAddressExists(userAddress);
    }

    function userTenantHashExistsPublic(
        bytes32 tenantHash) public  returns(bool) {
        return userTenantHashExists(tenantHash);
    }
}