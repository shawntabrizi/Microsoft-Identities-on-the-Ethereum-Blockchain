window.jwt_token

// On load, check if user is signed in
window.onload = async function () {
    // Check for querystrings
    var queryStrings = parseQueryStrings();
    // Set address, and run query from first transaction block to current block
    if (queryStrings['id_token']) {
        console.log(queryStrings['id_token']);
        window.jwt_token = queryStrings['id_token']
        var payload = JSON.parse(jwtdecode(queryStrings['id_token']))
        console.log(payload);

        load_eth_create_ux();

        if (payload['name']) {
            document.getElementById('name').innerText = payload['name']
        }
    } else {
        sign_in();
    }
}

function load_eth_create_ux() {
    var body = document.getElementById("body")
    var ux =
        `
        <section class="top-section">
            <div class="container">
                <div class="row">
                    <div class="col-lg-12 text-center welcome-message">
                        <h2 class="section-heading text-uppercase">Hi <span id="name">there</span>!</h2>
                        <h3 class="section-subheading text-muted">
                            Let's tie your Microsoft account to an Ethereum address.  
                        </h3>
                    </div>
                    <div class="col-lg-12 text-center">
                        <a class="btn btn-primary btn-xl" onclick="load_qr_code_ux()">Create your Ethereum account</a>
                    </div>
                </div>
            </div>
        </section>
        <section class="bg-light small-section">
            <div class="row">
                <div class="col-lg-12 text-center">
                    <p class="text-muted">Already have an Ethereum account?</p>
                    <a class="btn btn-secondary btn-xl" onclick="sign_message()">
                    <img src="../resources/img/metamask_icon.png" height="32">   Sign in with MetaMask
                    </a>
                </div>
            </div>
        </section>
        `
    body.innerHTML = ux;
}

function load_loading_ux() {
    var body = document.getElementById("body")
    var ux =
        `
        <section class="top-section">
            <div class="container">
                <div class="row text-primary top-section">
                    <div class="col-lg-12 text-center">
                        <i class="fa fa-spin fa-spinner fa-5x"></i>
                    </div>
                </div>
            </div>
        </section>
        `
    body.innerHTML = ux;
}

function load_success_ux() {
    var body = document.getElementById("body")
    var ux =
        `
        <section class="top-section">
            <div class="container">
                <div class="row top-section">
                    <div class="col-lg-12 text-center status-message success-message">
                        <span class="fa-stack fa-3x status-icon success">
                            <i class="fa fa-circle fa-stack-2x text-primary"></i>
                            <i class="fa fa-check fa-stack-1x fa-inverse"></i> 
                        </span>
                        <h2 class="section-subheading success-message">Successully signed the message!</h2>
                        <!-- <a href="https://ropsten.etherscan.io/tx/">View this transaction on the blockchain</href> -->
                    </div>
                </div>
            </div>
        </section>
        `
    body.innerHTML = ux;
}

function load_error_ux() {
    var body = document.getElementById("body")
    var ux =
        `
        <section class="top-section">
            <div class="container">
                <div class="row top-section">
                    <div class="col-lg-12 text-center status-message error-message">
                        <span class="fa-stack fa-3x status-icon error">
                            <i class="fa fa-circle fa-stack-2x text-primary"></i>
                            <i class="fa fa-times fa-stack-1x fa-inverse"></i>
                        </span>
                        <h2 class="section-subheading success-message">Could not sign the message</h2>
                    </div>
                    <div class="col-lg-12 text-center">
                        <a class="btn btn-secondary btn-xl sign-message-button" onclick="location.reload()">
                            Try again
                        </a>
                    </div>
                </div>
            </div>
        </section>

        `
    body.innerHTML = ux;
}

async function load_qr_code_ux() {
    var body = document.getElementById("body")
    var ux =
        `
        <section class="top-section">
            <div class="container">
                <div class="row">
                    <div class="col-7 text-center small-section account">
                        <h2 class="section-subheading status-message">We've generated an Ethereum account for you:</h2>
                        <h2 class="small-section-heading">Here's your private key <i class="fa fa-arrow-right"></i></h2>
                        <h3 class="section-subheading small-section-subheading text-muted">Take a photo of it and keep it safe.</h3>
                        <div class="account-details bg-light">
                            <div class="row">Address: <div class="text-center" id="address"></div></div>
                            <div class="row">Private key: <div class="text-center" id="private_key"></div></div>
                        </div>
                    </div>
                    <div class="col-5 text-center">
                        <div class="text-center" id="qrcodeAccount"></div>
                    </div>
                </div>
            </div>
        </section>
        <section class="bg-light small-section">
            <div class="container>
                <div class="row">
                    <div class="col-lg-12 text-center">
                        <h2 class="small-section-heading">Now let's add your company to the blockchain</h2>
                        <a class="btn btn-primary btn-xl sign-message-button" onclick="sign_message()">
                            Sign your request
                            <i class="fa fa-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>
        </section>
        `
    body.innerHTML = ux;

    await set_qr_account(get_eth_account());
}