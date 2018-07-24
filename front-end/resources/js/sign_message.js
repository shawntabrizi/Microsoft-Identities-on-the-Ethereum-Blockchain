window.addEventListener('load', function () {
    if (typeof web3 !== 'undefined') {
        console.log('Web3 Detected! ' + web3.currentProvider.constructor.name)
        window.web3 = new Web3(web3.currentProvider);
    } else {
        console.log('No Web3 Detected... please install Metamask')
        //You need Metamask to provide account info, so Infura won't do!
        window.web3 = new Web3(new Web3.providers.HttpProvider("https://mainnet.infura.io/<APIKEY>"));
    }
})

async function sign_message(messageJson) {
    var message = JSON.stringify(messageJson)
    var accounts = await web3.eth.getAccounts()
    var hex = ''
    for(var i=0;i<message.length;i++) {
        hex += ''+message.charCodeAt(i).toString(16)
    }
    var hexMessage = "0x" + hex
    var signed_message = web3.eth.personal.sign(hexMessage, accounts[0])
    return signed_message
}

async function sign_token() {
    //var jwt_raw = document.getElementById("jwt_raw").innerText
    //var signed_message = await sign_message(jwt_raw)
    //document.getElementById("eth_signature").innerText = signed_message
    final_output()
}

async function final_output(in_accounts) {
    var accounts = in_accounts ?  in_accounts : await web3.eth.getAccounts()
    var output = {}
    output.registration = {}
    output.registration.address = accounts[0]
    output.registration.options = {}
    output.registration.options.claims = ["tid"]
    output.registration.token = document.getElementById("jwt_raw").innerText
    output.signature = await sign_message(output.registration)
    
    document.getElementById("final_output").innerText = JSON.stringify(output)

}