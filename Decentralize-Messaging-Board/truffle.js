var HDWalletProvider = require("truffle-hdwallet-provider"); //Use for passphrases
var passphrase = "<passphrasse";

module.exports = {
  migrations_directory: "./migrations",
  networks: {
    development: {
      host: "localhost",
      port: 7545,
      network_id: "*" // Match any network id
    }
    ,
    ropsten: {
      provider: () => new HDWalletProvider(passphrase, "https://ropsten.infura.io/x8SDVAzSoKmnTAA7Wwnt"),
      network_id: "*",
      gas: 4712388
    }
  },
  solc: {
    optimizer: {
      enabled: true,
      runs: 500
    }
  } 
};
