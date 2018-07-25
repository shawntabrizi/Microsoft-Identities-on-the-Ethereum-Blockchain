import json
import time
import web3
import sha3

from os import environ
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract

API_KEY = environ.get('API_KEY')  
PRIVATE_KEY = environ.get('PRIVATE_KEY')
CONTRACT_ADDRESS = environ.get('CONTRACT_ADDRESS')
CONTRACT_FILE_PATH = './resources/IdentityStore.json'

NETWORK_ENDPOINT = "https://ropsten.infura.io/v3/{}".format(API_KEY)


w3 = Web3(HTTPProvider(NETWORK_ENDPOINT))
w3.eth.enable_unaudited_features()

def setTenant(hashObject, address, timestamp, tenantId):
    
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

    transaction = {
        'to': contract.address,
        'data': get_data,
        'gas': 1728712,
        'gasPrice': w3.toWei('21', 'gwei'),
        'nonce': w3.eth.getTransactionCount(account.address)
    }

    signed = w3.eth.account.signTransaction(transaction, PRIVATE_KEY)

    txn_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    txn = w3.eth.getTransaction(txn_hash)

    print('Contract Transaction Hash {}'.format(txn_hash))
    print('Transaction {}'.format(txn))

def get_ethereum_contract(file_path='./resources/IdentityStore.json'):
    contract_file = open(file_path, 'r')
    contract = json.load(contract_file)
    
    return contract

def get_deloyed_contract(contract_definition, contract_address): 
    contract_abi = contract_definition['abi']
    contract = w3.eth.contract(abi=contract_abi, address=contract_address)
    return contract

def load_contract():
    contract_definition = get_ethereum_contract(CONTRACT_FILE_PATH) 
    return get_deloyed_contract(contract_definition, CONTRACT_ADDRESS)

def is_valid(tenant_id, user_address):
    contract = load_contract()
    timestamp = int(time.time())
    # call isValid on contract
    isValid = contract.functions.isValid(tenant_id, user_address, timestamp).call()
    return isValid
