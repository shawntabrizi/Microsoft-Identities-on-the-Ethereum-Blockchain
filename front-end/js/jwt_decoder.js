//This function takes a base 64 url encoded string, and converts it to a JSON object... using a few steps.
function decoder(base64url) {
    try {
        //Convert base 64 url to base 64
        var base64 = base64url.replace('-', '+').replace('_', '/')
        //atob() is a built in JS function that decodes a base-64 encoded string
        var utf8 = atob(base64)
        //Then parse that into JSON
        var json = JSON.parse(utf8)
        //Then make that JSON look pretty
        var json_string = JSON.stringify(json, null, 4)
    } catch (err) {
        json_string = "Bad Section.\nError: " + err.message
    }
    return json_string
}

function jwtdecode(jwt_token) {
    var message, Header, Payload, Signature

    Header = "{\n}"
    Payload = "{\n}"
    Signature = "{\n}"

    if (jwt_token.length < 1) {
        message = "Use the text area above to input a JSON Web Token, " + "<a href='javascript:;' onclick='sample()'>or use this sample token.</a>"
    } else {
        //JSON Web Tokens consist of three parts separated by dots "."
        //Header, Payload, and Signature
        //Each of these parts are base-64-url encoded strings with the JSON data
        var tokens = jwt_token.split(".")
        if (tokens.length == 3) {
            message = "Valid Token"
            Header = decoder(tokens[0])
            Payload = decoder(tokens[1])
            if (tokens[2].length > 0) {
                Signature = "[Signed Token]"
            } else {
                Signature = "[Unsigned Token]"
            }
        } else {
            message = "JSON Web Tokens must have 3 sections, even without a signature."
        }
    }
    div_header.innerHTML = Header
    div_payload.innerHTML = Payload
    div_signature.innerHTML = Signature
    p_message.innerHTML = message

    return Payload

}

var div_header = document.getElementById('header')
var div_payload = document.getElementById('payload')
var div_signature = document.getElementById('signature')
var p_message = document.getElementById('message')
var input_field = document.getElementById('input')


// Detect Querystrings
function parseQueryStrings() {
    var queryStrings = {};
    //Parse URL
    var url = window.location.hash.substring(1);
    if (url) {
        //split querystrings
        var pairs = url.split("&");
        for (pair in pairs) {
            pairArray = pairs[pair].split("=");
            queryStrings[pairArray[0]] = pairArray[1]
        }
    }

    return queryStrings;
}

// On load, check if querystrings are present
window.onload = async function () {
    // Check for querystrings
    var queryStrings = parseQueryStrings();
    // Set address, and run query from first transaction block to current block
    if (queryStrings['id_token']) {
        document.getElementById('jwt_raw').innerText = queryStrings['id_token'];
        var payload = JSON.parse(jwtdecode(queryStrings['id_token']))
        if (payload['name']) {
            document.getElementById('name').innerText = payload['name']
            document.getElementById('sign_in_text').hidden = true
            document.getElementById('sign_in_button').hidden = true
        }
    }
}