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


w3 = Web3(HTTPProvider())
w3.eth.enable_unaudited_features()

def setTenant(private_key, hashObject, address, timestamp, tenantId):
    
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

<<<<<<< HEAD
    signed = w3.eth.account.signTransaction(transaction, private_key)
=======
    signed = w3.eth.account.signTransaction(transaction, PRIVATE_KEY)
>>>>>>> 287024b0aaba7631c6e9853771d9cea3066f1207

    txn_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    txn = w3.eth.getTransaction(txn_hash)

    print('Contract Transaction Hash {}'.format(txn_hash))
    print('Transaction {}'.format(txn))

<<<<<<< HEAD
def get_deloyed_contract(contract_definition, contract_address): 

    contract_abi = contract_definition['abi']
    contract = w3.eth.contract(abi=contract_abi, address=contract_address)

    return contract


def validate_tenant(contract, tenantId, address, timestamp):

    value = contract.functions.isValid(tenantId, address, timestamp).call()
    print(value)

def main():
    file_path = '../../identity-smart-contract//build/contracts/IdentityStore.json'
    contract_definition = get_ethereum_contract(file_path)
    contract_address = '0x313CaC645b2210b6591EEDd7a6D492521819CF1E'
    
    contract = get_deloyed_contract(contract_definition, contract_address)

    data = 'maydata'
    hash_data = data.encode('utf-8')
    test_address = '0x50c026Df0CD87A38d7Bc746Eb6BD8702fd243B0c'
    tenant_id = "suup" 
    timestamp = 123123

    # setTenant(contract, hash_data, test_address, timestamp, tenant_id)

    validate_tenant(contract, tenant_id, test_address, 12312)

if __name__ == '__main__':
    main()
=======

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

>>>>>>> 287024b0aaba7631c6e9853771d9cea3066f1207
