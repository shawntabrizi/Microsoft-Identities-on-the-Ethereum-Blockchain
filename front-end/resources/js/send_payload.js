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

  .then(function(response) {
    return response.json();
  }).then(function(data){
    load_success_ux(data.message.transactionHash);
  }).catch(function() {
    load_error_ux();
  })
}

