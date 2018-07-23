var Identity = artifacts.require("IdentityStore");

contract('Identity', function(accounts) {
  
    it("Should Register a Tenant to the contract", function() {
        return Identity.deployed().then(function(instance) {
        
            var tenantHash = web3.sha3('tenantId!');
            var address = "0x47635c238f8af460e37e772387364ddd86c43a61";
            var timestamp = 123123123

            instance.setTenant(tenantHash, address, timestamp);

            return instance.userAddressExists.call(address);

        }).then(function(result) {
            assert.equal(result, true);
        });
    });
});



contract('2nd Identity test', async () => {

    it("s", async () => {
       let instance = await Identity.deployed();
       
       var tenantHash = web3.sha3('tenantId!');
       var address = "0x47635c238f8af460e37e772387364ddd86c43a61";
       var timestamp = 123123123

       await instance.setTenant(tenantHash, address, timestamp);
       
       var threwException = false;

       try {
           await instance.setTenant.call(tenantHash, address, timestamp);
       }
       catch(error){
           threwException = true;
       }

       assert(threwException);

    });
    
});

contract('User hash test', async () => {

    it("should update correctly", async () => {
       let instance = await Identity.deployed();
       
       var tenantHash = web3.sha3('tenantId!');
       var address = "0x47635c238f8af460e37e772387364ddd86c43a61";
       var timestamp = 123123123;
       var newTenantHash = web3.sha3('tenantId+');

       await instance.setTenant(tenantHash, address, timestamp);
       await instance.updateHash(tenantHash, newTenantHash, 1234);

       var updated = await instance.userTenantHashExists.call(newTenantHash);
       var removed = await instance.userTenantHashExists.call(tenantHash);
       assert(updated);
       assert(!removed);
    });
    
});

contract('User hash test 2', async () => {

    it("should return an error when old user hash does not exist", async () => {
       let instance = await Identity.deployed();
       
       var tenantHash = web3.sha3('tenantId!');
       var newTenantHash = web3.sha3('tenantId+');

       var threwException = false
       try {
        await instance.updateHash(tenantHash, newTenantHash, 1234);
       } catch (error) {
           threwException = true;
       }
       assert(threwException);
    });

});

contract('User hash test 3', async () => {

    it("should return an error when new user hash is alerady registered", async () => {
       let instance = await Identity.deployed();
       
       var tenantHash = web3.sha3('tenantId!');
       var address = "0x47635c238f8af460e37e772387364ddd86c43a61";
       var timestamp = 123123123;
       var newTenantHash = web3.sha3('tenantId+');
       var newAddress = "0x47635c238f8af460e37e772387364ddd86c43a62";

       await instance.setTenant(tenantHash, address, timestamp);
       await instance.setTenant(newTenantHash, newAddress, timestamp);

       var threwException = false
       try {
        await instance.updateHash(tenantHash, newTenantHash, 1234);
       } catch (error) {
           threwException = true;
       }
       assert(threwException);
    });
    
});