import json
import time
import web3

from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract

def get_ethereum_contract(file_path):
    contract_file = open(file_path, 'r')
    contract = json.load(contract_file)
    
    return contract



def main():
    file_path = '../../identity-smart-contract//build/contracts/IdentityStore.json'
    
    contract_address = '0x313CaC645b2210b6591EEDd7a6D492521819CF1E'
    contract_definition = get_ethereum_contract(file_path)
    
    w3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/380500510ecf4d9cbac74fdf566c9065"))

    w3.eth.enable_unaudited_features()

    contract_abi = contract_definition['abi']

    contract = w3.eth.contract(abi=contract_abi, address=contract_address)
    
    print(contract)
    
    w3.personal.importRawKey('389e3c80b20359988263bd3abd88a71eb5d964ddae1b3430cf4be61c7e17381f', '!!123abc')


if __name__ == '__main__':
    main()