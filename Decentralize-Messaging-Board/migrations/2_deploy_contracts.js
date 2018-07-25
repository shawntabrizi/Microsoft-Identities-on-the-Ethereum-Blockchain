var SimpleStorage = artifacts.require("SimpleStorage");
var TutorialToken = artifacts.require("TutorialToken");
var ComplexStorage = artifacts.require("ComplexStorage");
var DMB = artifacts.require("DMB");

module.exports = function(deployer) {
  deployer.deploy(DMB);
};
