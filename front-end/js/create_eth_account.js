function get_eth_account()
{
	return {
		address: "0xb8CE9ab6943e0eCED004cDe8e3bBed6568B2Fa01",
    	privateKey: "0x348ce564d427a3311b6536bbcff9390d69395b06ed6c486954e971d960fe8709"
	};
}

function set_qr_account()
{
    qr_account = {
		text : "0x348ce564d427a3311b6536bbcff9390d69395b06ed6c486954e971d960fe8709"
	};

	jQuery('#qrcodeAccount').qrcode({
		text	: "0x348ce564d427a3311b6536bbcff9390d69395b06ed6c486954e971d960fe8709"
	});	
	console.log("creating account");
	console.log(qr_account.text);
}

set_qr_account();