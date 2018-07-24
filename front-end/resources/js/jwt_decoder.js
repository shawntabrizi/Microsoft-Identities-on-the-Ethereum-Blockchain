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
    var tokens = jwt_token.split(".")
    //var header = decoder(tokens[0])
    var payload = decoder(tokens[1])

    return payload
}

var div_header = document.getElementById('token_header')
var div_payload = document.getElementById('token_payload')
var div_signature = document.getElementById('token_signature')
var p_message = document.getElementById('token_message')


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