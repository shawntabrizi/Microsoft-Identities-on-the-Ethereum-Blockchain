const Web3 = require('web3');
const TruffleConfig = require('../truffle');

var Migrations = artifacts.require("./Migrations.sol");
var Identity = artifacts.require("IdentityStore");

module.exports = function(deployer, network) {
  const config = TruffleConfig.networks[network];

  if(config.password) {
    const web3 = new Web3(new Web3.providers.HttpProvider('http://' + config.host + ':' + config.port));
    console.log('>> Unlocking account ' + config.address);
    web3.personal.unlockAccount(config.address, config.password(), 36000);
  }

  deployer.deploy(Migrations);

  deployer.deploy(Identity)
    .then(() => console.log(Identity.address));
};
