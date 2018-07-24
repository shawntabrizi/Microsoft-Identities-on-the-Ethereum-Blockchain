var Identity = artifacts.require("IdentityStore");

contract('Identity', function(accounts) {
  
    it("Should Register a Tenant to the contract", function() {
        return Identity.deployed().then(function(instance) {
        
            var tenantHash = web3.sha3('tenantId!');
            var address = "0x47635c238f8af460e37e772387364ddd86c43a61";
            var timestamp = 123123123;
            var tenantId = "tenantID";

            instance.setTenant(tenantHash, address, timestamp, tenantId);

            return instance.userAddressExists.call(address);

        }).then(function(result) {
            assert.equal(result, true);
        });
    });
});

contract('Identity', function(accounts) {
  
    it("Should update the registration of Tenant with new account -part 1", function() {
        return Identity.deployed().then(function(instance) {
        
            var tenantHash = web3.sha3('tenantId!');
            var address1 = "0x47635c238f8af460e37e772387364ddd86c43a61";
            var address2 = "0x47635c238f8af460e37e772387364ddd86c43a62";
            var timestamp = 123123123
            var tenantId = "tenantID";

            instance.setTenant(tenantHash, address1, timestamp, tenantId);
            instance.updateAddress(address1, address2);

            return instance.userAddressExists.call(address1);

        }).then(function(result) {
            assert.equal(result, false);
        });
    });
});

contract('Identity', function(accounts) {
  
    it("Should update the registration of Tenant with new account -part 2", function() {
        return Identity.deployed().then(function(instance) {
        
            var tenantHash = web3.sha3('tenantId!');
            var address1 = "0x47635c238f8af460e37e772387364ddd86c43a61";
            var address2 = "0x47635c238f8af460e37e772387364ddd86c43a62";
            var timestamp = 123123123
            var tenantId = "tenantID";

            instance.setTenant(tenantHash, address1, timestamp, tenantId);
            instance.updateAddress(address1, address2);

            return instance.userAddressExists.call(address2);

        }).then(function(result) {
            assert.equal(result, true);
        });
    });
    
});

contract('User hash test', async () => {

    it("should update correctly", async () => {
       let instance = await Identity.deployed();
       
       var tenantHash = web3.sha3('tenantId!');
       var address = "0x47635c238f8af460e37e772387364ddd86c43a61";
       var timestamp = 123123123;
       var newTenantHash = web3.sha3('tenantId+');
       var tenantId = "tenantID";

       await instance.setTenant(tenantHash, address, timestamp, tenantId);
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
       var tenantId = "tenantID";

       await instance.setTenant(tenantHash, address, timestamp, tenantId);
       await instance.setTenant(newTenantHash, newAddress, timestamp, tenantId);

       var threwException = false
       try {
        await instance.updateHash(tenantHash, newTenantHash, 1234);
       } catch (error) {
           threwException = true;
       }
       assert(threwException);
    });
    
});

contract('is valid user', async () => {
    it("should verify valid user", async () => {
       let instance = await Identity.deployed();
       
       var tenantHash = web3.sha3('tenantId!');
       var address = "0x47635c238f8af460e37e772387364ddd86c43a61";
       var timestamp = 123123123;
       var tenantId = "tenantID";

       await instance.setTenant(tenantHash, address, timestamp, tenantId);

       var verified = await instance.isValid.call(tenantId, address, 0);
       assert(verified);
    });
});

contract('is valid user 2', async () => {
    it("should reject valid user if the timestamp is too old", async () => {
       let instance = await Identity.deployed();
       
       var tenantHash = web3.sha3('tenantId!');
       var address = "0x47635c238f8af460e37e772387364ddd86c43a61";
       var timestamp = 123123123;
       var tenantId = "tenantID";

       await instance.setTenant(tenantHash, address, timestamp, tenantId);

       var verified = await instance.isValid.call(tenantId, address, 1231231234);
       assert(!verified);
    });
});

contract('is valid user3', async () => {
    it("should reject a user with an address that isnt registered", async () => {
       let instance = await Identity.deployed();
       
       var tenantHash = web3.sha3('tenantId!');
       var address = "0x47635c238f8af460e37e772387364ddd86c43a61";
       var timestamp = 123123123;
       var tenantId = "tenantID";
       var address2 = "0x47635c238f8af460e37e772387364ddd86c43a62";

       await instance.setTenant(tenantHash, address, timestamp, tenantId);

       var verified = await instance.isValid.call(tenantId, address2, 0);
       assert(!verified);
    });
});

contract('is valid user4', async () => {
    it("should reject a user with an address that isnt registered to the correct tenant id", async () => {
       let instance = await Identity.deployed();
       
       var tenantHash = web3.sha3('tenantId!');
       var address = "0x47635c238f8af460e37e772387364ddd86c43a61";
       var timestamp = 123123123;
       var tenantId = "tenantID";
       var tenantId2 = "tenantID2";

       await instance.setTenant(tenantHash, address, timestamp, tenantId);

       var verified = await instance.isValid.call(tenantId2, address, 0);
       assert(!verified);
    });
});