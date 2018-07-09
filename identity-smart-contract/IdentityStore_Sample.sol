pragma solidity ^0.4.24;

contract IdentityStore {
    mapping(address => string) public tenantMapping;
    
    function setTenant(address _user, string _tenant) public {
        tenantMapping[_user] = _tenant;
    }
    
    function isAlive() public pure returns(bool alive) {
        return true;
    }
    
}