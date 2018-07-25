window.addEventListener('load', function () {
    if (typeof web3 !== 'undefined') {
        console.log('Web3 Detected! ' + web3.currentProvider.constructor.name)
        window.web3 = new Web3(web3.currentProvider);
    } else {
        console.log('No Web3 Detected... please install Metamask')
        //You need Metamask to provide account info, so Infura won't do!
        //window.web3 = new Web3(new Web3.providers.HttpProvider("https://mainnet.infura.io/<APIKEY>"));
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

async function sign_with_metamask() {
    console.log("hi");
    var accounts = await web3.eth.getAccounts()
    final_output(accounts)
}

async function final_output(accounts,) {
    var output = {}
    output.registration = {}
    output.registration.address = accounts[0]
    output.registration.options = {}
    output.registration.options.claims = ["tid"]
    output.registration.token = window.jwt_token
    output.signature = await sign_message(output.registration)
    
    send_payload(output)
}