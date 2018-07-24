pragma solidity ^0.4.24;

contract IdentityStore {
    
    function isValid(string _tenantId, address _userAddress, uint256 _minTimestamp) view public returns(bool){}

    function userAddressExists(address userAddress) view public returns(bool){}

    function hasAccountExpired(address userAddress, uint validDays ) view public returns(bool){}

    function userTenantHashExists(bytes32 tenantHash) view public returns(bool){}
}