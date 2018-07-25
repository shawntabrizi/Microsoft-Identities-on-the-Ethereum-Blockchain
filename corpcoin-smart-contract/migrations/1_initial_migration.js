var Migrations = artifacts.require("./Migrations.sol");
var CorpCoin = artifacts.require("CorpCoin");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
  deployer.deploy(CorpCoin, "0x6731f0093420d167e89dcea2d26be848dad649f1", 500);
};
