var endpoint = "https://msidoneth.azurewebsites.net/signup"

async function send_payload(payload) {
  fetch(endpoint, {
    method: 'POST',
    headers: {
      'Accept': 'application/json'
      //'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  })
    .then(function() {
      load_success_ux();
    }).catch(function() {
      load_error_ux();
    })
}