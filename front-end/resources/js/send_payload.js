var endpoint = "https://msidoneth.azurewebsites.net/signup"

async function send_payload(payload) {
    (async () => {
        const rawResponse = await fetch(endpoint, {
          method: 'POST',
          headers: {
            'Accept': 'application/json'
            //'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload)
        });
        const content = await rawResponse.json();
      
        console.log(content);
      })();
}