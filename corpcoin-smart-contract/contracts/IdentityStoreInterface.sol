pragma solidity ^0.4.24;

contract IdentityStore {
    mapping(address => string) public tenantMapping;
    
    function isAlive() public pure returns(bool alive) {}
    function hasAccountExpired(address userAddress, uint validDays ) view public returns(bool){}
}