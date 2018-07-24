module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 8545,
      address: "0xe2c5148294b874142add42168783c92553fb05e1",
      password: function() { return process.env.ETH_PASSWORD },
      network_id: "*",
      gas: 4600000
    }
  }
};
