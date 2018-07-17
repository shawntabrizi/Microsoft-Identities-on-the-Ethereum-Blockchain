function sign_in() {
    var userAgentApplication = new Msal.UserAgentApplication('79d908c3-6cc1-40c6-bbf1-9f7140e927fb', null, function (errorDes, token, error, tokenType, instance) {
        // this callback is called after loginRedirect OR acquireTokenRedirect. It's not used with loginPopup,  acquireTokenPopup.
        if (error) {
            console.log(error + ": " + errorDes);
        }
        else
            console.log("Token type = " + tokenType);

    })

    userAgentApplication.loginRedirect(["user.read"]).then(function (token) {
        var user = userAgentApplication.getUser();
        if (user) {
            console.log("signed in sucessfully");

            // get an access token
            userAgentApplication.acquireTokenSilent(["user.read"]).then(function (token) {
                console.log("Success acquiring access token");
            }, function (error) {
                // interaction required
                if (error.indexOf("interaction_required" != -1)) {
                    userAgentApplication.acquireTokenPopup(["user.read"]).then(function (token) {
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


var sign_in_button = document.getElementById("sign_in_button")
sign_in_button.addEventListener("click", sign_in);