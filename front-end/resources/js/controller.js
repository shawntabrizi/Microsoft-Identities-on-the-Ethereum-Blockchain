// On load, check if user is signed in
window.onload = async function () {
    // Check for querystrings
    var queryStrings = parseQueryStrings();
    // Set address, and run query from first transaction block to current block
    if (queryStrings['id_token']) {
        console.log(queryStrings['id_token']);
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
        <div class="container">
            <div class="row">
                <div class="col-lg-12 text-center welcome-message">
                    <h2 class="section-heading text-uppercase">Hi <span id="name">there</span>!</h2>
                    <h3 class="section-subheading text-muted">
                        Let's tie your account to an Ethereum address.  
                    </h3>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-12 text-center">
                    <a class="btn btn-primary btn-xl" id="create_new_button" onclick="load_qr_code_ux()">Create your Ethereum account</a>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-12 text-center">
                    <p class="text-muted">Already have an Ethereum account?</p>
                    <a class="btn btn-secondary btn-xl" role="button" id="existing_account_button">
                        Sign in with an existing account
                    </a>
                </div>
            </div>
        </div>
        `
    body.innerHTML = ux;
}

async function load_qr_code_ux() {
    var body = document.getElementById("body")
    var ux =
        `
        <div class="container">
            <div class="row">
                <div class="col-lg-12 text-center success-message">
                    <span class="fa-stack fa-2x success">
                        <i class="fa fa-circle fa-stack-2x text-primary"></i>
                        <i class="fa fa-check fa-stack-1x fa-inverse"></i>
                    </span>
                    <h2 class="section-subheading success-message">Successfully created your Ethereum account!</h2>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-12 text-center">
                    <p class="text-muted">Here's your private key. Take a picture of it and keep it safe.</p>
                </div>
            </div>

            <div class="text-center" id="qrcodeAccount"></div>
        </div>
        `
    body.innerHTML = ux;

    await set_qr_account(get_eth_account());
}