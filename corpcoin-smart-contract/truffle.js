module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 8545,
      address: "0x6731f0093420d167e89dcea2d26be848dad649f1",
      password: function() { return process.env.ETH_PASSWORD },
      network_id: "*",
      gas: 4600000
    }
  }
};
