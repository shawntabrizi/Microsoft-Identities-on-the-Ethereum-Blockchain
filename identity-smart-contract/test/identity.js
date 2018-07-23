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

contract('Identity', function(accounts) {
  
    it("Should update the registration of Tenant with new account -part 1", function() {
        return Identity.deployed().then(function(instance) {
        
            var tenantHash = web3.sha3('tenantId!');
            var address = "0x47635c238f8af460e37e772387364ddd86c43a61";
            var address2 = "0x47635c238f8af460e37e772387364ddd86c43a62";
            var timestamp = 123123123

            instance.setTenant(tenantHash, address1, timestamp);
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
            var address = "0x47635c238f8af460e37e772387364ddd86c43a61";
            var address2 = "0x47635c238f8af460e37e772387364ddd86c43a62";
            var timestamp = 123123123

            instance.setTenant(tenantHash, address1, timestamp);
            instance.updateAddress(address1, address2);

            return instance.userAddressExists.call(address2);

        }).then(function(result) {
            assert.equal(result, true);
        });
    });
});