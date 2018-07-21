import time
from web3 import Web3, HTTPProvider

# we'll use ConciseContract to interact with our specific instance of the contract
from web3.contract import ConciseContract

def deploy_contract(
    network='http://localhost:8545',
    contractSource='../../identity-smart-contract/IdentityStore_Sample.sol'):
    
    # open a connection to the local ethereum node
    http_provider = HTTPProvider(network)
    eth_provider = Web3(http_provider).eth

    default_account = eth_provider.accounts[0]

    transaction_details = {
        'from': default_account
    }

    #load solditiy code
    with open(contractSource) as file:
        source_code = file.readlines()

    #compile contract
    compiled_code = compile_source(''.join(source_code))

    #contract name
    contract_name = 'MSIDonETH'

    #store contract information in variables
    contract_bytecode = compiled_code[f'<stdin>:{contract_name}']['bin']
    contract_abi = compiled_code[f'<stdin>:{contract_name}']['abi']

    #create contract factory
    contract_factory = eth_provider.contract(
        abi=contract_abi,
        bytecode=contract_bytecode,
    )

    #contract constructor
    contract_constructor = contract_factory.constructor()

    #deploy the contract
    transaction_hash = contract_constructor.transact(transaction_details)

    #get contract address
    transaction_receipt = eth_provider.getTransactionReceipt(transaction_hash)
    contract_address = transaction_receipt['contractAddress']

    # when a contract instance is converted to python, we call the native solidity
    # functions like: contract_instance.call().someFunctionHere()
    # the .call() notation becomes repetitive so we can pass in ConciseContract as our
    # parent class, allowing us to make calls like: contract_instance.someFunctionHere()
    contract_instance = eth_provider.contract(
        abi=contract_abi,
        address=contract_address,
        ContractFactoryClass=ConciseContract,
    )
