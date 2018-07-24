function sign_in() {

    var applicationConfig = {
        clientID: '79d908c3-6cc1-40c6-bbf1-9f7140e927fb',
        graphScopes: ["user.read"]
    };

    var userAgentApplication = new Msal.UserAgentApplication(applicationConfig.clientID, null, function (errorDes, token, error, tokenType, instance) {
        // this callback is called after loginRedirect OR acquireTokenRedirect. It's not used with loginPopup,  acquireTokenPopup.
        if (error) {
            console.log(error + ": " + errorDes);
        }
        else
            console.log("Token type = " + tokenType);

    })

    userAgentApplication.loginRedirect(applicationConfig.graphScopes).then(function (token) {
        var user = userAgentApplication.getUser();
        if (user) {
            console.log("signed in sucessfully");

            // get an access token
            userAgentApplication.acquireTokenSilent(applicationConfig.graphScopes).then(function (token) {
                console.log("Success acquiring access token");
            }, function (error) {
                // interaction required
                if (error.indexOf("interaction_required" != -1)) {
                    userAgentApplication.acquireTokenPopup(applicationConfig.graphScopes).then(function (token) {
                        console.log("Success acquiring access token");
                    }, function (error) {
                        console.log("Failure acquiring token: " + error);
                    });
                }
            });
        } else {
            console.log("signed in failure");
        }
    }, function (error) {
        console.log("error: " + error);
    });
}


var sign_in_button = document.getElementById("sign_in_button");
sign_in_button.addEventListener("click", sign_in);

document.getElementById("create_eth_account").onclick = function () {
    location.href = "./QRAccount.html";
};