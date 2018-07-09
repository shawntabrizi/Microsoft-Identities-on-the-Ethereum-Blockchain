pragma solidity ^0.4.24;

contract IdentityStore {
    mapping(address => string) public tenantMapping;
    
    function isAlive() public pure returns(bool alive) {}
}

contract CorpCoin {
    
    IdentityStore idStore;
    
    function External(address addr) public {
        idStore = IdentityStore(addr);
    }
    
    function helloWorld(address _user) constant public returns (string) {
        return(idStore.tenantMapping(_user));
    }
    
    function Ping() public constant returns(bool response) {
        return idStore.isAlive();
    }
    
    function onlyHiWorks() public constant returns (bool response) {
        require(keccak256("Hi") == keccak256(idStore.tenantMapping(msg.sender)));
        return true;
    }
    
}