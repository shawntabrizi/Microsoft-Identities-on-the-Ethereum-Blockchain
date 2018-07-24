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

const promisify = (inner) =>
    new Promise((resolve, reject) =>
        inner((err, res) => {
            if (err) {
                reject(err);
            } else {
                resolve(res);
            }
        })
    );

async function sign_message(message) {
    var hash = web3.sha3(message)
    var signed_message = promisify(cb => web3.personal.sign(hash, web3.eth.defaultAccount, cb))
    return signed_message
}

async function sign_token() {
    //var jwt_raw = document.getElementById("jwt_raw").innerText
    //var signed_message = await sign_message(jwt_raw)
    //document.getElementById("eth_signature").innerText = signed_message
    final_output()
}

async function final_output() {
    var output = {}
    output.registration = {}
    output.registration.token = document.getElementById("jwt_raw").innerText
    output.registration.address = web3.eth.defaultAccount
    output.registration.options = {}
    output.registration.options.claims = ["tid"]
    output.signature = await sign_message(JSON.stringify(output.registration))
    
    document.getElementById("final_output").innerText = JSON.stringify(output)

}

function add_address() {
    document.getElementById("eth_address").innerText = web3.eth.defaultAccount
}

function afterLoad() {
    add_address()
}

var sign_message_button = document.getElementById("sign_message_button")
sign_message_button.addEventListener("click", sign_token);