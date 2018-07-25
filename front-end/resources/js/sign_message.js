window.addEventListener('load', function () {
    if (typeof web3 !== 'undefined') {
        console.log('Web3 Detected! ' + web3.currentProvider.constructor.name)
        window.web3 = new Web3(web3.currentProvider);
    } else {
        console.log('No Web3 Detected... please install Metamask')
        //You need Metamask to provide account info, so Infura won't do!
        window.web3 = new Web3(new Web3.providers.HttpProvider("https://ropsten.infura.io/<APIKEY>"));
    }
})

async function create_signature(messageJson, accounts) {
    var message = JSON.stringify(messageJson)
    var hex = ''
    for(var i=0;i<message.length;i++) {
        hex += ''+message.charCodeAt(i).toString(16)
    }
    var hexMessage = "0x" + hex
    var signature = web3.eth.personal.sign(hexMessage, accounts[0])
    return signature
}

async function create_signature_private_key(messageJson, private_key) {
    var message = JSON.stringify(messageJson)
    var hex = ''
    for(var i=0;i<message.length;i++) {
        hex += ''+message.charCodeAt(i).toString(16)
    }
    var hexMessage = "0x" + hex
    var signature = web3.eth.accounts.sign(hexMessage, private_key)
    return signature
}


async function sign_message(accounts) {
    var address
    if (global_accounts != null) {
        address = global_accounts.address
    } else {
        console.log("hi")
        accounts = await web3.eth.getAccounts()
        address = accounts[0]
        console.log(accounts)
    }
    var output = {}
    output.registration = {}
    output.registration.address = address
    output.registration.options = {}
    output.registration.options.claims = ["tid"]
    output.registration.token = window.jwt_token
    console.log(output)
    if (global_accounts != null) {
        output.signature = (await create_signature_private_key(output.registration, global_accounts.privateKey)).signature
    } else {
        output.signature = await create_signature(output.registration, accounts)
    }
    load_loading_ux()
    send_payload(output)
}