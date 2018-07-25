var global_accounts = null;

function get_eth_account()
{
	console.log("creating account");
	var account = web3.eth.accounts.create();
	global_accounts = account;
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

function start_over() {
	global_accounts = null
	window.location.replace("../")
}