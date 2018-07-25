import json
import time
import web3
import sha3

from os import environ
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from contract import IDENTITY_STORE_JSON

API_KEY = environ.get('API_KEY')  
PRIVATE_KEY = environ.get('PRIVATE_KEY')
CONTRACT_ADDRESS = environ.get('CONTRACT_ADDRESS')

NETWORK_ENDPOINT = "https://ropsten.infura.io/v3/{}".format(API_KEY)

w3 = Web3(HTTPProvider(NETWORK_ENDPOINT))
w3.eth.enable_unaudited_features()
#known_nonce = set()

def setTenant(hashObject, address, timestamp, tenantId):
    #global known_nonce

    contract = load_contract()
    account = w3.eth.account.privateKeyToAccount(PRIVATE_KEY) 

    get_data = contract.encodeABI(
        fn_name='setTenant',
        args=[
            hashObject,
            address,
            timestamp,
            tenantId
        ])

    trans_count = w3.eth.getTransactionCount(account.address)
    nonce = trans_count
    #while nonce in known_nonce:
    #    nonce += 1

    print("transaction count=%d nonce=%d" %(trans_count, nonce))

    price = w3.toWei('21', 'gwei')
    success = False
    retry = 100
    while not success and retry > 0:
        retry -= 1
        try:
            transaction = {
                'to': contract.address,
                'data': get_data,
                'gas': 1728712,
                'gasPrice': price,
                'nonce': nonce
            }

            signed = w3.eth.account.signTransaction(transaction, PRIVATE_KEY)
            txn_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
            txn = w3.eth.getTransaction(txn_hash)
            print('Contract Transaction Hash {}'.format(txn_hash))
            print('Transaction {}'.format(txn))

            #known_nonce.add(nonce)
            success = True
        except ValueError as err:
            err_msg = err.args[0]['message']
            print('web3 error:: %s' % err_msg)
            if 'replacement transaction underpriced' in err_msg:
                price += 1
                retry += 1 # underprice doesn't count for retrying
                print('increase price to %d' % price)
            elif 'nonce too low' in err_msg or 'known transaction' in err_msg:
                #known_nonce.add(nonce)
                nonce += 1
                print('increase nonce to %d' % nonce)
            else:
                raise err

    if retry <= 0:
        print('stop retrying')

    return txn


def get_deloyed_contract(contract_definition, contract_address): 
    contract_abi = contract_definition['abi']
    contract = w3.eth.contract(abi=contract_abi, address=contract_address)
    return contract

def load_contract():
    contract_definition = json.loads(IDENTITY_STORE_JSON)
    return get_deloyed_contract(contract_definition, CONTRACT_ADDRESS)

def is_valid(tenant_id, user_address):
    contract = load_contract()
    timestamp = int(time.time())
    # call isValid on contract
    isValid = contract.functions.isValid(tenant_id, user_address, timestamp).call()
    return isValid
