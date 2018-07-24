var CorpCoin = artifacts.require("CorpCoin");

contract('CorpCoin', async() => {
    const ownerAddress = "0x6731f0093420d167e89dcea2d26be848dad649f1";
    const initialAmount = 500;

    it("initializes correctly", async () => {
        let instance = await CorpCoin.deployed();
        let balance = await instance.balanceOf(ownerAddress);
        assert.equal(balance.toString(), initialAmount.toString());
     });
});