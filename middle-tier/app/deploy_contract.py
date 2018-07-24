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
    contract_definition = get_ethereum_contract(file_path)
    contract_address = '0x313CaC645b2210b6591EEDd7a6D492521819CF1E'
    deploy(contract_definition, contract_address)


def deploy(contract_definition, contract_address): 
    w3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/380500510ecf4d9cbac74fdf566c9065"))

    w3.eth.enable_unaudited_features()

    contract_abi = contract_definition['abi']

    contract = w3.eth.contract(abi=contract_abi, address=contract_address)
    print(json.dumps(contract_abi))
    

    return contract


if __name__ == '__main__':
    main()
