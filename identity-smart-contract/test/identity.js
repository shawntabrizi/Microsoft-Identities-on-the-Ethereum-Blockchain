var Identity = artifacts.require("IdentityStoreInherit");

contract('Set Tenant 1', function(accounts) {
  
    it("Should Register a Tenant to the contract", function() {
        return Identity.deployed().then(function(instance) {
        
            var tenantHash = web3.sha3('tenantId!');
            var address = "0x47635c238f8af460e37e772387364ddd86c43a61";
            var timestamp = 123123123;
            var tenantId = "tenantID";

            instance.setTenant(tenantHash, address, timestamp, tenantId);

            return instance.userAddressExistsPublic.call(address);

        }).then(function(result) {
            assert.equal(result, true);
        });
    });
});

contract('Set Tenant 2', function(accounts) {
  
    it("setTenant method should update user hash", function() {
        return Identity.deployed().then(function(instance) {
        
            var tenantHash = web3.sha3('tenantId!');
            var tenantHash2 = web3.sha3('tenantId+');
            var address = "0x47635c238f8af460e37e772387364ddd86c43a61";
            var timestamp = 123123123;
            var tenantId = "tenantID";

            instance.setTenant(tenantHash, address, timestamp, tenantId);
            instance.setTenant(tenantHash2, address, timestamp, tenantId);

            return instance.userTenantHashExistsPublic.call(tenantHash2);

        }).then(function(result) {
            assert.equal(result, true);
        });
    });
});

contract('Set Tenant 3', function(accounts) {
  
    it("Should update a user address", function() {
        return Identity.deployed().then(function(instance) {
        
            var tenantHash = web3.sha3('tenantId!');
            var address = "0x47635c238f8af460e37e772387364ddd86c43a61";
            var address2 = "0x47635c238f8af460e37e772387364ddd86c43a62";
            var timestamp = 123123123;
            var tenantId = "tenantID";

            instance.setTenant(tenantHash, address, timestamp, tenantId);
            instance.setTenant(tenantHash, address2, timestamp, tenantId);

            return instance.userAddressExistsPublic.call(address2);

        }).then(function(result) {
            assert.equal(result, true);
        });
    });
});

contract('Set Tenant 4', function(accounts) {
  
    it("Should update a user timestamp", function() {
        return Identity.deployed().then(function(instance) {
        
            var tenantHash = web3.sha3('tenantId!');
            var address = "0x47635c238f8af460e37e772387364ddd86c43a61";
            var timestamp = 123123123;
            var timestamp2 = 1231231232;
            var tenantId = "tenantID";

            instance.setTenant(tenantHash, address, timestamp, tenantId);
            instance.setTenant(tenantHash, address, timestamp2, tenantId);

            return instance.isValidTenant.call(tenantId, address, 1231231231);

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
            instance.updateAddressPublic(address1, address2);

            return instance.userAddressExistsPublic.call(address1);

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
            instance.updateAddressPublic(address1, address2);

            return instance.userAddressExistsPublic.call(address2);

        }).then(function(result) {
            assert.equal(result, true);
        });
    });
    
});

contract('Get User tenant id', async () => {

    it("should return the user tenant id", async () => {
       let instance = await Identity.deployed();
       
       var tenantHash = web3.sha3('tenantId!');
       var address = "0x47635c238f8af460e37e772387364ddd86c43a61";
       var timestamp = 123123123;
       var tenantId = "tenantID";

       await instance.setTenant(tenantHash, address, timestamp, tenantId);

       var tenantIdResult = await instance.getUserTenantId.call(address);
       assert.equal(tenantIdResult, tenantId);
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
       await instance.updateHashPublic(tenantHash, newTenantHash, 1234);

       var updated = await instance.userTenantHashExistsPublic.call(newTenantHash);
       var removed = await instance.userTenantHashExistsPublic.call(tenantHash);
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
        await instance.updateHashPublic(tenantHash, newTenantHash, 1234);
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
        await instance.updateHashPublic(tenantHash, newTenantHash, 1234);
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

       var verified = await instance.isValid.call(address, 0);
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

       var verified = await instance.isValid.call(address, 1231231234);
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

       var verified = await instance.isValid.call(address2, 0);
       assert(!verified);
    });
});
