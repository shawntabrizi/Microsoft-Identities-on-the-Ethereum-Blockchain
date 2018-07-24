window.addEventListener('load', function () {
    if (typeof web3 !== 'undefined') {
        console.log('Web3 Detected! ' + web3.currentProvider.constructor.name)
        window.web3 = new Web3(web3.currentProvider);
        afterLoad();
    } else {
        console.log('No Web3 Detected... please install Metamask')
        //You need Metamask to provide account info, so Infura won't do!
        //window.web3 = new Web3(new Web3.providers.HttpProvider("https://mainnet.infura.io/<APIKEY>"));
    }
})

async function sign_message(message) {
    var accounts = await web3.eth.getAccounts()
    var hash = web3.eth.accounts.hashMessage(message)
    var signature = web3.eth.personal.sign(hash, accounts[0])
    return signature
}

async function sign_token() {
    //var jwt_raw = document.getElementById("jwt_raw").innerText
    //var signature = await sign_message(jwt_raw)
    //document.getElementById("eth_signature").innerText = signature
    final_output()
}

async function final_output() {
    var accounts = await web3.eth.getAccounts()
    var output = {}
    output.registration = {}
    output.registration.token = document.getElementById("jwt_raw").innerText
    output.registration.address = accounts[0]
    output.registration.options = {}
    output.registration.options.claims = ["tid"]
    output.signature = await sign_message(JSON.stringify(output.registration))
    
    document.getElementById("final_output").innerText = JSON.stringify(output)

}

async function add_address() {
    var accounts = await web3.eth.getAccounts()
    document.getElementById("eth_address").innerText = accounts[0]
}

function afterLoad() {
    add_address()
}

var sign_message_button = document.getElementById("sign_message_button")
sign_message_button.addEventListener("click", sign_token);