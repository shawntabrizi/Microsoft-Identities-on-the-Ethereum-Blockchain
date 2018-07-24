# solc is needed to compile our Solidity code
from solc import compile_source

# web3 is needed to interact with eth contracts
from web3 import Web3, HTTPProvider

# we'll use ConciseContract to interact with our specific instance of the contract
from web3.contract import ConciseContract

def deploy_contract(file_path = '../../identity-smart-contract/contracts/IdentityStore_Sample.sol'):
    # open a connection to the local ethereum node
    http_provider = HTTPProvider('http://localhost:7545')
    eth_provider = Web3(http_provider).eth

    # we'll use one of our default accounts to deploy from. every write to the chain requires a
    # payment of ethereum called "gas". if we were running an actual test ethereum node locally,
    # then we'd have to go on the test net and get some free ethereum to play with. that is beyond
    # the scope of this tutorial so we're using a mini local node that has unlimited ethereum and
    # the only chain we're using is our own local one
    default_account = eth_provider.accounts[0]
    # every time we write to the chain it's considered a "transaction". every time a transaction
    # is made we need to send with it at a minimum the info of the account that is paying for the gas
    transaction_details = {
        'from': default_account,
    }

    print(file_path)

    # load our Solidity code into an object
    with open(file_path) as file:
        source_code = file.readlines()

    print(source_code)

    # compile the contract
    compiled_code = compile_source(''.join(source_code))

    # store contract_name so we keep our code DRY
    contract_name = 'MSIDonETH'

    # lets make the code a bit more readable by storing these values in variables
    contract_bytecode = compiled_code[f'<stdin>:{contract_name}']['bin']
    contract_abi = compiled_code[f'<stdin>:{contract_name}']['abi']
    # the contract abi is important. it's a json representation of our smart contract. this
    # allows other APIs like JavaScript to understand how to interact with our contract without
    # reverse engineering our compiled code

    # create a contract factory. the contract factory contains the information about the
    # contract that we probably will not change later in the deployment script.
    contract_factory = eth_provider.contract(
        abi=contract_abi,
        bytecode=contract_bytecode,
    )

    # here we pass in a list of smart contract constructor arguments. our contract constructor
    # takes only one argument, a list of candidate names. the contract constructor contains
    # information that we might want to change. below we pass in our list of voting candidates.
    # the factory -> constructor design pattern gives us some flexibility when deploying contracts.
    # if we wanted to deploy two contracts, each with different candidates, we could call the
    # constructor() function twice, each time with different candidates.
    contract_constructor = contract_factory.constructor()

    # here we deploy the smart contract. the bare minimum info we give about the deployment is which
    # ethereum account is paying the gas to put the contract on the chain. the transact() function
    # returns a transaction hash. this is like the id of the transaction on the chain
    transaction_hash = contract_constructor.transact(transaction_details)

    # if we want our frontend to use our deployed contract as it's backend, the frontend
    # needs to know the address where the contract is located. we use the id of the transaction
    # to get the full transaction details, then we get the contract address from there
    transaction_receipt = eth_provider.getTransactionReceipt(transaction_hash)
    contract_address = transaction_receipt['contractAddress']

    contract_instance = eth_provider.contract(
        abi=contract_abi,
        address=contract_address,
        # when a contract instance is converted to python, we call the native solidity
        # functions like: contract_instance.call().someFunctionHere()
        # the .call() notation becomes repetitive so we can pass in ConciseContract as our
        # parent class, allowing us to make calls like: contract_instance.someFunctionHere()
        ContractFactoryClass=ConciseContract,
    )

    print(contract_instance)

    return contract_instance

def main():
    print("Hello")
    deploy_contract()


if __name__ == '__main__':
    main()