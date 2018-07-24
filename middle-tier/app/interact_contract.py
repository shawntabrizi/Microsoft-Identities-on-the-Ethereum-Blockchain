import json
import time
import web3
import sha3

from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract

w3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/380500510ecf4d9cbac74fdf566c9065"))
w3.eth.enable_unaudited_features()

def get_ethereum_contract(file_path):
    
    contract_file = open(file_path, 'r')
    contract = json.load(contract_file)
    
    return contract


def setTenant(contract, hashObject, address, timestamp, tenantId):

    private_key = '389e3c80b20359988263bd3abd88a71eb5d964ddae1b3430cf4be61c7e17381f'
    account = w3.eth.account.privateKeyToAccount(private_key) 

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

    signed = w3.eth.account.signTransaction(transaction, private_key)

    txn_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    txn = w3.eth.getTransaction(txn_hash)

    print('Contract Transaction Hash {}'.format(txn_hash))
    print('Transaction {}'.format(txn))

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
    test_account = '0x50c026Df0CD87A38d7Bc746Eb6BD8702fd243B0c'
    tenant_id = "sup" 
    timestamp = 123123

    setTenant(contract, hash_data, test_account, 123123, tenant_id)

    # validate_tenant(contract, tenant_id, test_account, 12312)

if __name__ == '__main__':
    main()
