var global_accounts = null;

async function get_eth_account()
{
	console.log("creating account");
	var account = await web3.eth.accounts.create();
	global_accounts = account;
	return account;
}

async function set_qr_account()
{
	var account = await get_eth_account();
	jQuery('#qrcodeAccount').qrcode({
		text	: account.privateKey.slice(2)
	});	
	document.getElementById('address').innerText = account.address;
	document.getElementById('private_key').innerText = account.privateKey.slice(2);
}

function start_over() {
	global_accounts = null
	window.location.replace("../")
}