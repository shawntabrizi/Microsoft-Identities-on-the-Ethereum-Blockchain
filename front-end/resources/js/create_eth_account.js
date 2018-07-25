function getRNG()
{
	//Webkit2's crazy invertible mapping generator
	// Theory is here: http://dl.acm.org/citation.cfm?id=752741
	// from https://bocoup.com/blog/random-numbers
	var num_digits = 32;
	var max = Math.pow(2, num_digits),
		seed;
	return {
		setSeed : function(val) {
			seed = val || Math.round(Math.random() * max);
		},
		getSeed : function() {
			return seed;
		},
		rand : function() {
			// creates randomness...somehow...
			seed += (seed * seed) | 5;
			// Shift off bits, discarding the sign. Discarding the sign is
			// important because OR w/ 5 can give us + or - numbers.
			return (seed >>> num_digits) / max;
			//return Math.abs(seed);
		}
	};
}

function get_private_key()
{
	var rng = getRNG();
	rng.setSeed();
	var pKey = "";
	for (let i=0; i<8; i++)
	{
		pKey += rng.rand().toString(16).slice(2);
	}
	var hex_digits = 64;
	var pad = hex_digits - pKey.length;
	for (let i = 0; i < pad; i++)
	{
		pKey = '0' + pKey;
	}
	pKey = pKey.length > hex_digits ?  pKey.slice(0, hex_digits) : pKey;
	return pKey;
}

function get_eth_account()
{
	console.log("creating account");
	var account = web3.eth.accounts.create();
	final_output([account]);
	return account;
}

function set_qr_account(account)
{
	jQuery('#qrcodeAccount').qrcode({
		text	: account.privateKey.slice(2)
	});	
	document.getElementById('address').innerText = account.address;
	document.getElementById('private_key').innerText = account.privateKey.slice(2);
}
