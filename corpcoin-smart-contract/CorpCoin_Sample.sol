pragma solidity ^0.4.24;

contract IdentityStore {
    mapping(address => bytes32) public tenantMapping;
    
    function isAlive() public pure returns(bool alive) {}
}

contract CorpCoin {
    
    IdentityStore idStore;
    
    function External(address addr) public {
        idStore = IdentityStore(addr);
    }
    
    function helloWorld(address _user) constant public returns (bytes32) {
        return(idStore.tenantMapping(_user));
    }
    
    function Ping() public constant returns(bool response) {
        return idStore.isAlive();
    }
    
}