"""
"""

import web3
import time
import deploy_contract

from web3 import Web3
from contract import IDENTITY_STORE_JSON
from Crypto.Hash import keccak
from deploy_contract import CONTRACT_ABI


def init_contract(contract_address, contract_abi):
    w3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io/v3/380500510ecf4d9cbac74fdf566c9065"))
    
    # initiate contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi)

    return contract

def hash_keccak(msg):
    keccak_hash = keccak.new(digest_bits=256)
    keccak_hash.update(msg.encode('utf_8'))
    return '0x' + keccak_hash.hexdigest()


contract_address = '0x313CaC645b2210b6591EEDd7a6D492521819CF1E'

def set_tenant(user_address, tenant_id):
    contract = init_contract(contract_address, CONTRACT_ABI)

    tenant_hash = hash_keccak(tenant_id)
    timestamp = int(time.time())

    tx_hash = contract.functions.setTenant(
        tenant_hash, 
        user_address,
        timestamp,
        tenant_id).transact()

    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    return True


def is_valid(tenant_id, user_address):
    contract = init_contract(contract_address, CONTRACT_ABI)
    timestamp = int(time.time())

    # call isValid on contract
    isValid = greeter.functions.isValid(tenant_id, user_address, timestamp).call()

    return isValid
