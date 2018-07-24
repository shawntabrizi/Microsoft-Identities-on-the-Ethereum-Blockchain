import json
import time
import web3

from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from contract import IDENTITY_STORE_JSON

def get_ethereum_contract(file_path):
    contract_file = open(file_path, 'r')
    contract = json.load(contract_file)
    
    return contract

contract_dict = json.loads(IDENTITY_STORE_JSON)
CONTRACT_BYTECODE = contract_dict['bytecode'] 
CONTRACT_ABI = contract_dict['abi']

def create_contract(user_address): 
    w3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/380500510ecf4d9cbac74fdf566c9065"))
    
    w3.eth.defaultAccount = user_address # w3.eth.accounts[0]

    # create contract on network
    Contract = w3.eth.contract(abi=CONTRACT_ABI, bytecode=CONTRACT_BYTECODE)
    tx_hash = Contract.constructor().transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    print('created contract address:' + tx_receipt.contractAddress)

    return tx_receipt.contractAddress
"""
    w3.eth.enable_unaudited_features()

    contract_abi = contract_definition['abi']

    contract = w3.eth.contract(abi=contract_abi, address=contract_address)
    
    print(contract)

    w3.personal.importRawKey('389e3c80b20359988263bd3abd88a71eb5d964ddae1b3430cf4be61c7e17381f', '!!123abc')

    print(json.dumps(contract_abi))
    

    return contract
"""

def main():
    file_path = '../../identity-smart-contract//build/contracts/IdentityStore.json'
    contract_definition = get_ethereum_contract(file_path)
    contract_address = '0x313CaC645b2210b6591EEDd7a6D492521819CF1E'
    deploy(contract_definition, contract_address)

if __name__ == '__main__':
    main()

