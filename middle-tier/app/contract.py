IDENTITY_STORE_JSON = r"""
{
  "contractName": "IdentityStore",
  "abi": [
    {
      "constant": false,
      "inputs": [],
      "name": "renounceOwnership",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_newOwner",
          "type": "address"
        }
      ],
      "name": "transferOwnership",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "name": "previousOwner",
          "type": "address"
        }
      ],
      "name": "OwnershipRenounced",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "name": "previousOwner",
          "type": "address"
        },
        {
          "indexed": true,
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "OwnershipTransferred",
      "type": "event"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_tenantHash",
          "type": "bytes32"
        },
        {
          "name": "_userAddress",
          "type": "address"
        },
        {
          "name": "_timestamp",
          "type": "uint256"
        },
        {
          "name": "_tenantId",
          "type": "string"
        }
      ],
      "name": "setTenant",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "_tenantId",
          "type": "string"
        },
        {
          "name": "_userAddress",
          "type": "address"
        },
        {
          "name": "_minTimestamp",
          "type": "uint256"
        }
      ],
      "name": "isValid",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    }
  ],
  "bytecode": "0x6080604052336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550611441806100536000396000f30060806040526004361061006d576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806348d7de6314610072578063715018a61461011357806377cfe1c11461012a5780638da5cb5b146101d5578063f2fde38b1461022c575b600080fd5b34801561007e57600080fd5b506101116004803603810190808035600019169060200190929190803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190803590602001908201803590602001908080601f016020809104026020016040519081016040528093929190818152602001838380828437820191505050505050919291929050505061026f565b005b34801561011f57600080fd5b5061012861050b565b005b34801561013657600080fd5b506101bb600480360381019080803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509192919290803573ffffffffffffffffffffffffffffffffffffffff1690602001909291908035906020019092919050505061060d565b604051808215151515815260200191505060405180910390f35b3480156101e157600080fd5b506101ea61083e565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34801561023857600080fd5b5061026d600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610863565b005b610277611303565b6000806000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156102d557600080fd5b6102de866108ca565b1580156102f157506102ef87610930565b155b156103f1576060604051908101604052808860001916815260200186815260200185815250925082600160008873ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000820151816000019060001916905560208201518160010155604082015181600201908051906020019061038e929190611328565b509050508560026000896000191660001916815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550610502565b6103fa866108ca565b801561040c575061040a87610930565b155b1561046657600160008773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060000154915061046182888761099e565b610502565b61046f87610930565b8015610481575061047f866108ca565b155b156104d35760026000886000191660001916815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1690506104ce8187610d34565b610502565b6104dc87610930565b80156104ed57506104ec866108ca565b5b15610501576104fc8786611128565b610502565b5b50505050505050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561056657600080fd5b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff167ff8df31144d9c2f0f6b59d69b8b98abd5459d07f2742c4df920b25aae33c6482060405160405180910390a260008060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550565b6000610617611303565b610620846108ca565b151561062f5760009150610836565b600160008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206060604051908101604052908160008201546000191660001916815260200160018201548152602001600282018054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561072f5780601f106107045761010080835404028352916020019161072f565b820191906000526020600020905b81548152906001019060200180831161071257829003601f168201915b5050505050815250509050846040518082805190602001908083835b602083101515610770578051825260208201915060208101905060208303925061074b565b6001836020036101000a03801982511681845116808217855250505050505090500191505060405180910390206000191681604001516040518082805190602001908083835b6020831015156107db57805182526020820191506020810190506020830392506107b6565b6001836020036101000a03801982511681845116808217855250505050505090500191505060405180910390206000191614151561081c5760009150610836565b82816020015110156108315760009150610836565b600191505b509392505050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156108be57600080fd5b6108c781611209565b50565b600080600102600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060000154600019161415610926576000905061092b565b600190505b919050565b60008060026000846000191660001916815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614156109945760009050610999565b600190505b919050565b60006109a8611303565b6109b0611303565b6109b986610930565b1515610a2d576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260188152602001807f4f6c64206861736820646f6573206e6f742065786973742e000000000000000081525060200191505060405180910390fd5b610a3685610930565b151515610aab576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601f8152602001807f4e6577206861736820697320616c726561647920726567697374657265642e0081525060200191505060405180910390fd5b60026000876000191660001916815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169250600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206060604051908101604052908160008201546000191660001916815260200160018201548152602001600282018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610be95780601f10610bbe57610100808354040283529160200191610be9565b820191906000526020600020905b815481529060010190602001808311610bcc57829003601f168201915b5050505050815250509150606060405190810160405280866000191681526020018581526020018360400151815250905080600160008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008201518160000190600019169055602082015181600101556040820151816002019080519060200190610c90929190611328565b5090505060026000876000191660001916815260200190815260200160002060006101000a81549073ffffffffffffffffffffffffffffffffffffffff02191690558260026000876000191660001916815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550505050505050565b610d3c611303565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515610d9757600080fd5b600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206060604051908101604052908160008201546000191660001916815260200160018201548152602001600282018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610e975780601f10610e6c57610100808354040283529160200191610e97565b820191906000526020600020905b815481529060010190602001808311610e7a57829003601f168201915b5050505050815250509050610eab826108ca565b151515610f46576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252602f8152602001807f5468657265277320616c726561647920616e206163636f756e7420746965642081526020017f746f20746869732061646472657373000000000000000000000000000000000081525060400191505060405180910390fd5b610f4f836108ca565b1515610fe9576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252602d8152602001807f54686572652773206e6f206163636f756e74207469656420746f20746865206181526020017f646472657373206f726967696e0000000000000000000000000000000000000081525060400191505060405180910390fd5b816002600083600001516000191660001916815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555080600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082015181600001906000191690556020820151816001015560408201518160020190805190602001906110bd929190611328565b50905050600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600080820160009055600182016000905560028201600061112191906113a8565b5050505050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561118357600080fd5b806001600060026000866000191660001916815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600101819055505050565b600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff161415151561124557600080fd5b8073ffffffffffffffffffffffffffffffffffffffff166000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a3806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b6060604051908101604052806000801916815260200160008152602001606081525090565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061136957805160ff1916838001178555611397565b82800160010185558215611397579182015b8281111561139657825182559160200191906001019061137b565b5b5090506113a491906113f0565b5090565b50805460018160011615610100020316600290046000825580601f106113ce57506113ed565b601f0160209004906000526020600020908101906113ec91906113f0565b5b50565b61141291905b8082111561140e5760008160009055506001016113f6565b5090565b905600a165627a7a723058207c67c458c4169c933a8ba606e6b48c72b5bf593805c8b855dcff2fdc024365950029",
  "deployedBytecode": "0x60806040526004361061006d576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806348d7de6314610072578063715018a61461011357806377cfe1c11461012a5780638da5cb5b146101d5578063f2fde38b1461022c575b600080fd5b34801561007e57600080fd5b506101116004803603810190808035600019169060200190929190803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190803590602001908201803590602001908080601f016020809104026020016040519081016040528093929190818152602001838380828437820191505050505050919291929050505061026f565b005b34801561011f57600080fd5b5061012861050b565b005b34801561013657600080fd5b506101bb600480360381019080803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509192919290803573ffffffffffffffffffffffffffffffffffffffff1690602001909291908035906020019092919050505061060d565b604051808215151515815260200191505060405180910390f35b3480156101e157600080fd5b506101ea61083e565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34801561023857600080fd5b5061026d600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610863565b005b610277611303565b6000806000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156102d557600080fd5b6102de866108ca565b1580156102f157506102ef87610930565b155b156103f1576060604051908101604052808860001916815260200186815260200185815250925082600160008873ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000820151816000019060001916905560208201518160010155604082015181600201908051906020019061038e929190611328565b509050508560026000896000191660001916815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550610502565b6103fa866108ca565b801561040c575061040a87610930565b155b1561046657600160008773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060000154915061046182888761099e565b610502565b61046f87610930565b8015610481575061047f866108ca565b155b156104d35760026000886000191660001916815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1690506104ce8187610d34565b610502565b6104dc87610930565b80156104ed57506104ec866108ca565b5b15610501576104fc8786611128565b610502565b5b50505050505050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561056657600080fd5b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff167ff8df31144d9c2f0f6b59d69b8b98abd5459d07f2742c4df920b25aae33c6482060405160405180910390a260008060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550565b6000610617611303565b610620846108ca565b151561062f5760009150610836565b600160008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206060604051908101604052908160008201546000191660001916815260200160018201548152602001600282018054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561072f5780601f106107045761010080835404028352916020019161072f565b820191906000526020600020905b81548152906001019060200180831161071257829003601f168201915b5050505050815250509050846040518082805190602001908083835b602083101515610770578051825260208201915060208101905060208303925061074b565b6001836020036101000a03801982511681845116808217855250505050505090500191505060405180910390206000191681604001516040518082805190602001908083835b6020831015156107db57805182526020820191506020810190506020830392506107b6565b6001836020036101000a03801982511681845116808217855250505050505090500191505060405180910390206000191614151561081c5760009150610836565b82816020015110156108315760009150610836565b600191505b509392505050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156108be57600080fd5b6108c781611209565b50565b600080600102600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060000154600019161415610926576000905061092b565b600190505b919050565b60008060026000846000191660001916815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614156109945760009050610999565b600190505b919050565b60006109a8611303565b6109b0611303565b6109b986610930565b1515610a2d576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260188152602001807f4f6c64206861736820646f6573206e6f742065786973742e000000000000000081525060200191505060405180910390fd5b610a3685610930565b151515610aab576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601f8152602001807f4e6577206861736820697320616c726561647920726567697374657265642e0081525060200191505060405180910390fd5b60026000876000191660001916815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169250600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206060604051908101604052908160008201546000191660001916815260200160018201548152602001600282018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610be95780601f10610bbe57610100808354040283529160200191610be9565b820191906000526020600020905b815481529060010190602001808311610bcc57829003601f168201915b5050505050815250509150606060405190810160405280866000191681526020018581526020018360400151815250905080600160008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008201518160000190600019169055602082015181600101556040820151816002019080519060200190610c90929190611328565b5090505060026000876000191660001916815260200190815260200160002060006101000a81549073ffffffffffffffffffffffffffffffffffffffff02191690558260026000876000191660001916815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550505050505050565b610d3c611303565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515610d9757600080fd5b600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206060604051908101604052908160008201546000191660001916815260200160018201548152602001600282018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610e975780601f10610e6c57610100808354040283529160200191610e97565b820191906000526020600020905b815481529060010190602001808311610e7a57829003601f168201915b5050505050815250509050610eab826108ca565b151515610f46576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252602f8152602001807f5468657265277320616c726561647920616e206163636f756e7420746965642081526020017f746f20746869732061646472657373000000000000000000000000000000000081525060400191505060405180910390fd5b610f4f836108ca565b1515610fe9576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252602d8152602001807f54686572652773206e6f206163636f756e74207469656420746f20746865206181526020017f646472657373206f726967696e0000000000000000000000000000000000000081525060400191505060405180910390fd5b816002600083600001516000191660001916815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555080600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082015181600001906000191690556020820151816001015560408201518160020190805190602001906110bd929190611328565b50905050600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600080820160009055600182016000905560028201600061112191906113a8565b5050505050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561118357600080fd5b806001600060026000866000191660001916815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600101819055505050565b600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff161415151561124557600080fd5b8073ffffffffffffffffffffffffffffffffffffffff166000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a3806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b6060604051908101604052806000801916815260200160008152602001606081525090565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061136957805160ff1916838001178555611397565b82800160010185558215611397579182015b8281111561139657825182559160200191906001019061137b565b5b5090506113a491906113f0565b5090565b50805460018160011615610100020316600290046000825580601f106113ce57506113ed565b601f0160209004906000526020600020908101906113ec91906113f0565b5b50565b61141291905b8082111561140e5760008160009055506001016113f6565b5090565b905600a165627a7a723058207c67c458c4169c933a8ba606e6b48c72b5bf593805c8b855dcff2fdc024365950029",
  "sourceMap": "1687:4196:0:-;;;575:10;567:5;;:18;;;;;;;;;;;;;;;;;;1687:4196;;;;;;",
  "deployedSourceMap": "1687:4196:0:-;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;1955:1283;;8:9:-1;5:2;;;30:1;27;20:12;5:2;1955:1283:0;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;1001:111;;8:9:-1;5:2;;;30:1;27;20:12;5:2;1001:111:0;;;;;;3244:619;;8:9:-1;5:2;;;30:1;27;20:12;5:2;3244:619:0;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;238:20;;8:9:-1;5:2;;;30:1;27;20:12;5:2;238:20:0;;;;;;;;;;;;;;;;;;;;;;;;;;;1274:103;;8:9:-1;5:2;;;30:1;27;20:12;5:2;1274:103:0;;;;;;;;;;;;;;;;;;;;;;;;;;;;1955:1283;2250:19;;:::i;:::-;2601:15;2892:18;719:5;;;;;;;;;;;705:19;;:10;:19;;;697:28;;;;;;;;2152:31;2170:12;2152:17;:31::i;:::-;2151:32;:70;;;;;2188:33;2209:11;2188:20;:33::i;:::-;2187:34;2151:70;2147:313;;;2272:40;;;;;;;;;2277:11;2272:40;;;;;;;2290:10;2272:40;;;;2302:9;2272:40;;;2250:62;;2363:7;2326:20;:34;2347:12;2326:34;;;;;;;;;;;;;;;:44;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::i;:::-;;;;;2417:12;2384:17;:30;2402:11;2384:30;;;;;;;;;;;;;;;;;;:45;;;;;;;;;;;;;;;;;;2443:7;;2147:313;2503:31;2521:12;2503:17;:31::i;:::-;:69;;;;;2539:33;2560:11;2539:20;:33::i;:::-;2538:34;2503:69;2499:254;;;2619:20;:34;2640:12;2619:34;;;;;;;;;;;;;;;:45;;;2601:63;;2678:44;2689:7;2698:11;2711:10;2678;:44::i;:::-;2736:7;;2499:254;2807:33;2828:11;2807:20;:33::i;:::-;:69;;;;;2845:31;2863:12;2845:17;:31::i;:::-;2844:32;2807:69;2803:224;;;2913:17;:30;2931:11;2913:30;;;;;;;;;;;;;;;;;;;;;;;;;;;2892:51;;2957:39;2971:10;2983:12;2957:13;:39::i;:::-;3010:7;;2803:224;3077:33;3098:11;3077:20;:33::i;:::-;:68;;;;;3114:31;3132:12;3114:17;:31::i;:::-;3077:68;3073:159;;;3161:40;3177:11;3190:10;3161:15;:40::i;:::-;3215:7;;3073:159;731:1;1955:1283;;;;;;;:::o;1001:111::-;719:5;;;;;;;;;;;705:19;;:10;:19;;;697:28;;;;;;;;1077:5;;;;;;;;;;;1058:25;;;;;;;;;;;;1105:1;1089:5;;:18;;;;;;;;;;;;;;;;;;1001:111::o;3244:619::-;3370:4;3502:23;;:::i;:::-;3422:31;3440:12;3422:17;:31::i;:::-;3421:32;3418:74;;;3476:5;3469:12;;;;3418:74;3528:20;:34;3549:12;3528:34;;;;;;;;;;;;;;;3502:60;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;3654:9;3644:20;;;;;;;;;;;;;36:153:-1;66:2;61:3;58:11;51:19;36:153;;;182:3;176:10;171:3;164:23;98:2;93:3;89:12;82:19;;123:2;118:3;114:12;107:19;;148:2;143:3;139:12;132:19;;36:153;;;274:1;267:3;263:2;259:12;254:3;250:22;246:30;315:4;311:9;305:3;299:10;295:26;356:4;350:3;344:10;340:21;389:7;380;377:20;372:3;365:33;3:399;;;3644:20:0;;;;;;;;;;;;;;;;3609:55;;;3619:11;:20;;;3609:31;;;;;;;;;;;;;36:153:-1;66:2;61:3;58:11;51:19;36:153;;;182:3;176:10;171:3;164:23;98:2;93:3;89:12;82:19;;123:2;118:3;114:12;107:19;;148:2;143:3;139:12;132:19;;36:153;;;274:1;267:3;263:2;259:12;254:3;250:22;246:30;315:4;311:9;305:3;299:10;295:26;356:4;350:3;344:10;340:21;389:7;380;377:20;372:3;365:33;3:399;;;3609:31:0;;;;;;;;;;;;;;;;:55;;;;;3606:97;;;3687:5;3680:12;;;;3606:97;3783:13;3759:11;:21;;;:37;3756:79;;;3819:5;3812:12;;;;3756:79;3852:4;3845:11;;3244:619;;;;;;;:::o;238:20::-;;;;;;;;;;;;;:::o;1274:103::-;719:5;;;;;;;;;;;705:19;;:10;:19;;;697:28;;;;;;;;1343:29;1362:9;1343:18;:29::i;:::-;1274:103;:::o;5424:211::-;5494:4;5568:1;5520:49;;:20;:33;5541:11;5520:33;;;;;;;;;;;;;;;:44;;;:49;;;;5517:91;;;5592:5;5585:12;;;;5517:91;5624:4;5617:11;;5424:211;;;;:::o;5641:240::-;5713:4;5814:1;5781:17;:29;5799:10;5781:29;;;;;;;;;;;;;;;;;;;;;;;;;;;:34;;;5778:76;;;5838:5;5831:12;;;;5778:76;5870:4;5863:11;;5641:240;;;;:::o;3869:792::-;4154:22;4216:23;;:::i;:::-;4288;;:::i;:::-;4000:30;4021:8;4000:20;:30::i;:::-;3992:67;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;4078:30;4099:8;4078:20;:30::i;:::-;4077:31;4069:75;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;4179:17;:27;4197:8;4179:27;;;;;;;;;;;;;;;;;;;;;;;;;;;4154:52;;4242:20;:36;4263:14;4242:36;;;;;;;;;;;;;;;4216:62;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;4314:48;;;;;;;;;4319:8;4314:48;;;;;;;4329:10;4314:48;;;;4341:11;:20;;;4314:48;;;4288:74;;4454:11;4415:20;:36;4436:14;4415:36;;;;;;;;;;;;;;;:50;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::i;:::-;;;;;4529:17;:27;4547:8;4529:27;;;;;;;;;;;;;;;;;;4522:34;;;;;;;;;;;4640:14;4610:17;:27;4628:8;4610:27;;;;;;;;;;;;;;;;;;:44;;;;;;;;;;;;;;;;;;3869:792;;;;;;:::o;4667:568::-;4767:24;;:::i;:::-;719:5;;;;;;;;;;;705:19;;:10;:19;;;697:28;;;;;;;;4794:20;:36;4815:14;4794:36;;;;;;;;;;;;;;;4767:63;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;4858:33;4876:14;4858:17;:33::i;:::-;4857:34;4849:94;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;4961:33;4979:14;4961:17;:33::i;:::-;4953:91;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;5100:14;5055:17;:42;5073:12;:23;;;5055:42;;;;;;;;;;;;;;;;;;:59;;;;;;;;;;;;;;;;;;5163:12;5124:20;:36;5145:14;5124:36;;;;;;;;;;;;;;;:51;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::i;:::-;;;;;5192:20;:36;5213:14;5192:36;;;;;;;;;;;;;;;;5185:43;;;;;;;;;;;;;;;;;;;;:::i;:::-;;;4667:568;;;:::o;5241:177::-;719:5;;;;;;;;;;;705:19;;:10;:19;;;697:28;;;;;;;;5401:10;5336:20;:52;5357:17;:30;5375:11;5357:30;;;;;;;;;;;;;;;;;;;;;;;;;;;5336:52;;;;;;;;;;;;;;;:62;;:75;;;;5241:177;;:::o;1512:171::-;1603:1;1582:23;;:9;:23;;;;1574:32;;;;;;;;1645:9;1617:38;;1638:5;;;;;;;;;;;1617:38;;;;;;;;;;;;1669:9;1661:5;;:17;;;;;;;;;;;;;;;;;;1512:171;:::o;1687:4196::-;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::o;:::-;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::i;:::-;;;:::o;:::-;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::i;:::-;;;:::o;:::-;;;;;;;;;;;;;;;;;;;;;;;;;;;:::o",
  "source": "pragma solidity ^0.4.24;\n\n\n/**\n * @title Ownable\n * @dev The Ownable contract has an owner address, and provides basic authorization control\n * functions, this simplifies the implementation of \"user permissions\".\n */\ncontract Ownable {\n  address public owner;\n\n\n  event OwnershipRenounced(address indexed previousOwner);\n  event OwnershipTransferred(\n    address indexed previousOwner,\n    address indexed newOwner\n  );\n\n\n  /**\n   * @dev The Ownable constructor sets the original `owner` of the contract to the sender\n   * account.\n   */\n  constructor() public {\n    owner = msg.sender;\n  }\n\n  /**\n   * @dev Throws if called by any account other than the owner.\n   */\n  modifier onlyOwner() {\n    require(msg.sender == owner);\n    _;\n  }\n\n  /**\n   * @dev Allows the current owner to relinquish control of the contract.\n   * @notice Renouncing to ownership will leave the contract without an owner.\n   * It will not be possible to call the functions with the `onlyOwner`\n   * modifier anymore.\n   */\n  function renounceOwnership() public onlyOwner {\n    emit OwnershipRenounced(owner);\n    owner = address(0);\n  }\n\n  /**\n   * @dev Allows the current owner to transfer control of the contract to a newOwner.\n   * @param _newOwner The address to transfer ownership to.\n   */\n  function transferOwnership(address _newOwner) public onlyOwner {\n    _transferOwnership(_newOwner);\n  }\n\n  /**\n   * @dev Transfers control of the contract to a newOwner.\n   * @param _newOwner The address to transfer ownership to.\n   */\n  function _transferOwnership(address _newOwner) internal {\n    require(_newOwner != address(0));\n    emit OwnershipTransferred(owner, _newOwner);\n    owner = _newOwner;\n  }\n}\n\ncontract IdentityStore is Ownable {\n  \n    struct User {\n        bytes32 tenantHash;\n        uint256 timestamp;\n        string tenantId;\n    }\n\n    mapping(address => User) private tenantAddressMapping;\n    mapping(bytes32 => address) private tenantHashMapping; \n\n    function setTenant(\n        bytes32 _tenantHash,\n        address _userAddress,\n        uint256 _timestamp,\n        string _tenantId) onlyOwner public {\n\n        // Completely new user\n        if (!userAddressExists(_userAddress) && !userTenantHashExists(_tenantHash)) {\n            \n            User memory newUser = User(_tenantHash, _timestamp, _tenantId);\n            tenantAddressMapping[_userAddress] = newUser;\n            tenantHashMapping[_tenantHash] = _userAddress;\n            return;\n        }\n\n        // Update user hash.\n        if (userAddressExists(_userAddress) && !userTenantHashExists(_tenantHash)) {\n            \n            bytes32 oldHash = tenantAddressMapping[_userAddress].tenantHash;\n            updateHash(oldHash, _tenantHash, _timestamp);\n            return;\n        }\n        \n        // Update user address.\n        if (userTenantHashExists(_tenantHash) && !userAddressExists(_userAddress)) {\n            address oldAddress = tenantHashMapping[_tenantHash];\n            updateAddress(oldAddress, _userAddress);\n            return;\n        }\n        \n        // Update timestamp\n        if (userTenantHashExists(_tenantHash) && userAddressExists(_userAddress)) {\n            updateTimestamp(_tenantHash, _timestamp);\n            return;\n        }\n    }\n\n    function isValid(\n        string _tenantId, \n        address _userAddress,\n        uint256 _minTimestamp) view public returns(bool) {\n\n        // check valid address\n        if(!userAddressExists(_userAddress)) {\n            return false;\n        }\n\n        User memory currentUser = tenantAddressMapping[_userAddress];\n\n        // check valid tenant id\n        if(keccak256(currentUser.tenantId) != keccak256(_tenantId)) {\n            return false;\n        }\n        \n        // check minimum timestamp\n        if(currentUser.timestamp < _minTimestamp) {\n            return false;\n        }\n\n        return true;\n    }\n\n    function updateHash(\n        bytes32 _oldHash, \n        bytes32 _newHash, \n        uint256 _timestamp) internal {\n\n        require(userTenantHashExists(_oldHash), \"Old hash does not exist.\");\n        require(!userTenantHashExists(_newHash), \"New hash is already registered.\");\n        address currentAddress = tenantHashMapping[_oldHash];\n        User memory oldUserInfo = tenantAddressMapping[currentAddress];\n        User memory newUserInfo = User(_newHash, _timestamp, oldUserInfo.tenantId);\n\n        // update address mapping to user\n        tenantAddressMapping[currentAddress] = newUserInfo;\n\n        // delete old hash mapping to address\n        delete tenantHashMapping[_oldHash];\n\n        // add new hash mapping to address\n        tenantHashMapping[_newHash] = currentAddress;\n    }\n\n    function updateAddress(address oldUserAddress, address newUserAddress) onlyOwner internal {\n        User memory existingUser = tenantAddressMapping[oldUserAddress];\n        \n        require(!userAddressExists(newUserAddress), \"There's already an account tied to this address\");\n        require(userAddressExists(oldUserAddress), \"There's no account tied to the address origin\");\n\n        tenantHashMapping[existingUser.tenantHash] = newUserAddress;\n        tenantAddressMapping[newUserAddress] = existingUser;\n        delete tenantAddressMapping[oldUserAddress];\n    }\n\n    function updateTimestamp(bytes32 _tenantHash, uint256 _timestamp) onlyOwner internal {\n        tenantAddressMapping[tenantHashMapping[_tenantHash]].timestamp = _timestamp;\n    }\n\n    function userAddressExists(address userAddress) view internal returns(bool) {       \n        if(tenantAddressMapping[userAddress].tenantHash == 0) {\n            return false;\n        }\n        return true;\n    }\n\n    function userTenantHashExists(bytes32 tenantHash) view internal returns(bool){\n        // pray it be who can find the 0X Address\n        if(tenantHashMapping[tenantHash] == 0) {\n            return false;\n        }\n        return true;\n    }\n}",
  "sourcePath": "/Users/fernandolobato/Desktop/Microsoft-Identities-on-the-Ethereum-Blockchain/identity-smart-contract/contracts/IdentityStore_Sample.sol",
  "ast": {
    "absolutePath": "/Users/fernandolobato/Desktop/Microsoft-Identities-on-the-Ethereum-Blockchain/identity-smart-contract/contracts/IdentityStore_Sample.sol",
    "exportedSymbols": {
      "IdentityStore": [
        428
      ],
      "Ownable": [
        85
      ]
    },
    "id": 429,
    "nodeType": "SourceUnit",
    "nodes": [
      {
        "id": 1,
        "literals": [
          "solidity",
          "^",
          "0.4",
          ".24"
        ],
        "nodeType": "PragmaDirective",
        "src": "0:24:0"
      },
      {
        "baseContracts": [],
        "contractDependencies": [],
        "contractKind": "contract",
        "documentation": "@title Ownable\n@dev The Ownable contract has an owner address, and provides basic authorization control\nfunctions, this simplifies the implementation of \"user permissions\".",
        "fullyImplemented": true,
        "id": 85,
        "linearizedBaseContracts": [
          85
        ],
        "name": "Ownable",
        "nodeType": "ContractDefinition",
        "nodes": [
          {
            "constant": false,
            "id": 3,
            "name": "owner",
            "nodeType": "VariableDeclaration",
            "scope": 85,
            "src": "238:20:0",
            "stateVariable": true,
            "storageLocation": "default",
            "typeDescriptions": {
              "typeIdentifier": "t_address",
              "typeString": "address"
            },
            "typeName": {
              "id": 2,
              "name": "address",
              "nodeType": "ElementaryTypeName",
              "src": "238:7:0",
              "typeDescriptions": {
                "typeIdentifier": "t_address",
                "typeString": "address"
              }
            },
            "value": null,
            "visibility": "public"
          },
          {
            "anonymous": false,
            "documentation": null,
            "id": 7,
            "name": "OwnershipRenounced",
            "nodeType": "EventDefinition",
            "parameters": {
              "id": 6,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 5,
                  "indexed": true,
                  "name": "previousOwner",
                  "nodeType": "VariableDeclaration",
                  "scope": 7,
                  "src": "289:29:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 4,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "289:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "288:31:0"
            },
            "src": "264:56:0"
          },
          {
            "anonymous": false,
            "documentation": null,
            "id": 13,
            "name": "OwnershipTransferred",
            "nodeType": "EventDefinition",
            "parameters": {
              "id": 12,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 9,
                  "indexed": true,
                  "name": "previousOwner",
                  "nodeType": "VariableDeclaration",
                  "scope": 13,
                  "src": "355:29:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 8,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "355:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 11,
                  "indexed": true,
                  "name": "newOwner",
                  "nodeType": "VariableDeclaration",
                  "scope": 13,
                  "src": "390:24:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 10,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "390:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "349:69:0"
            },
            "src": "323:96:0"
          },
          {
            "body": {
              "id": 21,
              "nodeType": "Block",
              "src": "561:29:0",
              "statements": [
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 19,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftHandSide": {
                      "argumentTypes": null,
                      "id": 16,
                      "name": "owner",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 3,
                      "src": "567:5:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "nodeType": "Assignment",
                    "operator": "=",
                    "rightHandSide": {
                      "argumentTypes": null,
                      "expression": {
                        "argumentTypes": null,
                        "id": 17,
                        "name": "msg",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 529,
                        "src": "575:3:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_magic_message",
                          "typeString": "msg"
                        }
                      },
                      "id": 18,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "lValueRequested": false,
                      "memberName": "sender",
                      "nodeType": "MemberAccess",
                      "referencedDeclaration": null,
                      "src": "575:10:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "src": "567:18:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "id": 20,
                  "nodeType": "ExpressionStatement",
                  "src": "567:18:0"
                }
              ]
            },
            "documentation": "@dev The Ownable constructor sets the original `owner` of the contract to the sender\naccount.",
            "id": 22,
            "implemented": true,
            "isConstructor": true,
            "isDeclaredConst": false,
            "modifiers": [],
            "name": "",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 14,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "551:2:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 15,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "561:0:0"
            },
            "scope": 85,
            "src": "540:50:0",
            "stateMutability": "nonpayable",
            "superFunction": null,
            "visibility": "public"
          },
          {
            "body": {
              "id": 32,
              "nodeType": "Block",
              "src": "691:46:0",
              "statements": [
                {
                  "expression": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "commonType": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        },
                        "id": 28,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftExpression": {
                          "argumentTypes": null,
                          "expression": {
                            "argumentTypes": null,
                            "id": 25,
                            "name": "msg",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 529,
                            "src": "705:3:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_magic_message",
                              "typeString": "msg"
                            }
                          },
                          "id": 26,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "lValueRequested": false,
                          "memberName": "sender",
                          "nodeType": "MemberAccess",
                          "referencedDeclaration": null,
                          "src": "705:10:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        },
                        "nodeType": "BinaryOperation",
                        "operator": "==",
                        "rightExpression": {
                          "argumentTypes": null,
                          "id": 27,
                          "name": "owner",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 3,
                          "src": "719:5:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        },
                        "src": "705:19:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      ],
                      "id": 24,
                      "name": "require",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [
                        532,
                        533
                      ],
                      "referencedDeclaration": 532,
                      "src": "697:7:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_require_pure$_t_bool_$returns$__$",
                        "typeString": "function (bool) pure"
                      }
                    },
                    "id": 29,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "697:28:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 30,
                  "nodeType": "ExpressionStatement",
                  "src": "697:28:0"
                },
                {
                  "id": 31,
                  "nodeType": "PlaceholderStatement",
                  "src": "731:1:0"
                }
              ]
            },
            "documentation": "@dev Throws if called by any account other than the owner.",
            "id": 33,
            "name": "onlyOwner",
            "nodeType": "ModifierDefinition",
            "parameters": {
              "id": 23,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "688:2:0"
            },
            "src": "670:67:0",
            "visibility": "internal"
          },
          {
            "body": {
              "id": 48,
              "nodeType": "Block",
              "src": "1047:65:0",
              "statements": [
                {
                  "eventCall": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "id": 39,
                        "name": "owner",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 3,
                        "src": "1077:5:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      ],
                      "id": 38,
                      "name": "OwnershipRenounced",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 7,
                      "src": "1058:18:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_event_nonpayable$_t_address_$returns$__$",
                        "typeString": "function (address)"
                      }
                    },
                    "id": 40,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "1058:25:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 41,
                  "nodeType": "EmitStatement",
                  "src": "1053:30:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 46,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftHandSide": {
                      "argumentTypes": null,
                      "id": 42,
                      "name": "owner",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 3,
                      "src": "1089:5:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "nodeType": "Assignment",
                    "operator": "=",
                    "rightHandSide": {
                      "argumentTypes": null,
                      "arguments": [
                        {
                          "argumentTypes": null,
                          "hexValue": "30",
                          "id": 44,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": true,
                          "kind": "number",
                          "lValueRequested": false,
                          "nodeType": "Literal",
                          "src": "1105:1:0",
                          "subdenomination": null,
                          "typeDescriptions": {
                            "typeIdentifier": "t_rational_0_by_1",
                            "typeString": "int_const 0"
                          },
                          "value": "0"
                        }
                      ],
                      "expression": {
                        "argumentTypes": [
                          {
                            "typeIdentifier": "t_rational_0_by_1",
                            "typeString": "int_const 0"
                          }
                        ],
                        "id": 43,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": true,
                        "lValueRequested": false,
                        "nodeType": "ElementaryTypeNameExpression",
                        "src": "1097:7:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_type$_t_address_$",
                          "typeString": "type(address)"
                        },
                        "typeName": "address"
                      },
                      "id": 45,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": true,
                      "kind": "typeConversion",
                      "lValueRequested": false,
                      "names": [],
                      "nodeType": "FunctionCall",
                      "src": "1097:10:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "src": "1089:18:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "id": 47,
                  "nodeType": "ExpressionStatement",
                  "src": "1089:18:0"
                }
              ]
            },
            "documentation": "@dev Allows the current owner to relinquish control of the contract.\n@notice Renouncing to ownership will leave the contract without an owner.\nIt will not be possible to call the functions with the `onlyOwner`\nmodifier anymore.",
            "id": 49,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": false,
            "modifiers": [
              {
                "arguments": null,
                "id": 36,
                "modifierName": {
                  "argumentTypes": null,
                  "id": 35,
                  "name": "onlyOwner",
                  "nodeType": "Identifier",
                  "overloadedDeclarations": [],
                  "referencedDeclaration": 33,
                  "src": "1037:9:0",
                  "typeDescriptions": {
                    "typeIdentifier": "t_modifier$__$",
                    "typeString": "modifier ()"
                  }
                },
                "nodeType": "ModifierInvocation",
                "src": "1037:9:0"
              }
            ],
            "name": "renounceOwnership",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 34,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "1027:2:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 37,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "1047:0:0"
            },
            "scope": 85,
            "src": "1001:111:0",
            "stateMutability": "nonpayable",
            "superFunction": null,
            "visibility": "public"
          },
          {
            "body": {
              "id": 60,
              "nodeType": "Block",
              "src": "1337:40:0",
              "statements": [
                {
                  "expression": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "id": 57,
                        "name": "_newOwner",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 51,
                        "src": "1362:9:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      ],
                      "id": 56,
                      "name": "_transferOwnership",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 84,
                      "src": "1343:18:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_internal_nonpayable$_t_address_$returns$__$",
                        "typeString": "function (address)"
                      }
                    },
                    "id": 58,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "1343:29:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 59,
                  "nodeType": "ExpressionStatement",
                  "src": "1343:29:0"
                }
              ]
            },
            "documentation": "@dev Allows the current owner to transfer control of the contract to a newOwner.\n@param _newOwner The address to transfer ownership to.",
            "id": 61,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": false,
            "modifiers": [
              {
                "arguments": null,
                "id": 54,
                "modifierName": {
                  "argumentTypes": null,
                  "id": 53,
                  "name": "onlyOwner",
                  "nodeType": "Identifier",
                  "overloadedDeclarations": [],
                  "referencedDeclaration": 33,
                  "src": "1327:9:0",
                  "typeDescriptions": {
                    "typeIdentifier": "t_modifier$__$",
                    "typeString": "modifier ()"
                  }
                },
                "nodeType": "ModifierInvocation",
                "src": "1327:9:0"
              }
            ],
            "name": "transferOwnership",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 52,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 51,
                  "name": "_newOwner",
                  "nodeType": "VariableDeclaration",
                  "scope": 61,
                  "src": "1301:17:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 50,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "1301:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "1300:19:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 55,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "1337:0:0"
            },
            "scope": 85,
            "src": "1274:103:0",
            "stateMutability": "nonpayable",
            "superFunction": null,
            "visibility": "public"
          },
          {
            "body": {
              "id": 83,
              "nodeType": "Block",
              "src": "1568:115:0",
              "statements": [
                {
                  "expression": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "commonType": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        },
                        "id": 71,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftExpression": {
                          "argumentTypes": null,
                          "id": 67,
                          "name": "_newOwner",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 63,
                          "src": "1582:9:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        },
                        "nodeType": "BinaryOperation",
                        "operator": "!=",
                        "rightExpression": {
                          "argumentTypes": null,
                          "arguments": [
                            {
                              "argumentTypes": null,
                              "hexValue": "30",
                              "id": 69,
                              "isConstant": false,
                              "isLValue": false,
                              "isPure": true,
                              "kind": "number",
                              "lValueRequested": false,
                              "nodeType": "Literal",
                              "src": "1603:1:0",
                              "subdenomination": null,
                              "typeDescriptions": {
                                "typeIdentifier": "t_rational_0_by_1",
                                "typeString": "int_const 0"
                              },
                              "value": "0"
                            }
                          ],
                          "expression": {
                            "argumentTypes": [
                              {
                                "typeIdentifier": "t_rational_0_by_1",
                                "typeString": "int_const 0"
                              }
                            ],
                            "id": 68,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": true,
                            "lValueRequested": false,
                            "nodeType": "ElementaryTypeNameExpression",
                            "src": "1595:7:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_type$_t_address_$",
                              "typeString": "type(address)"
                            },
                            "typeName": "address"
                          },
                          "id": 70,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": true,
                          "kind": "typeConversion",
                          "lValueRequested": false,
                          "names": [],
                          "nodeType": "FunctionCall",
                          "src": "1595:10:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        },
                        "src": "1582:23:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      ],
                      "id": 66,
                      "name": "require",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [
                        532,
                        533
                      ],
                      "referencedDeclaration": 532,
                      "src": "1574:7:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_require_pure$_t_bool_$returns$__$",
                        "typeString": "function (bool) pure"
                      }
                    },
                    "id": 72,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "1574:32:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 73,
                  "nodeType": "ExpressionStatement",
                  "src": "1574:32:0"
                },
                {
                  "eventCall": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "id": 75,
                        "name": "owner",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 3,
                        "src": "1638:5:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      },
                      {
                        "argumentTypes": null,
                        "id": 76,
                        "name": "_newOwner",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 63,
                        "src": "1645:9:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        },
                        {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      ],
                      "id": 74,
                      "name": "OwnershipTransferred",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 13,
                      "src": "1617:20:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_event_nonpayable$_t_address_$_t_address_$returns$__$",
                        "typeString": "function (address,address)"
                      }
                    },
                    "id": 77,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "1617:38:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 78,
                  "nodeType": "EmitStatement",
                  "src": "1612:43:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 81,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftHandSide": {
                      "argumentTypes": null,
                      "id": 79,
                      "name": "owner",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 3,
                      "src": "1661:5:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "nodeType": "Assignment",
                    "operator": "=",
                    "rightHandSide": {
                      "argumentTypes": null,
                      "id": 80,
                      "name": "_newOwner",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 63,
                      "src": "1669:9:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "src": "1661:17:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "id": 82,
                  "nodeType": "ExpressionStatement",
                  "src": "1661:17:0"
                }
              ]
            },
            "documentation": "@dev Transfers control of the contract to a newOwner.\n@param _newOwner The address to transfer ownership to.",
            "id": 84,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": false,
            "modifiers": [],
            "name": "_transferOwnership",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 64,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 63,
                  "name": "_newOwner",
                  "nodeType": "VariableDeclaration",
                  "scope": 84,
                  "src": "1540:17:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 62,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "1540:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "1539:19:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 65,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "1568:0:0"
            },
            "scope": 85,
            "src": "1512:171:0",
            "stateMutability": "nonpayable",
            "superFunction": null,
            "visibility": "internal"
          }
        ],
        "scope": 429,
        "src": "217:1468:0"
      },
      {
        "baseContracts": [
          {
            "arguments": null,
            "baseName": {
              "contractScope": null,
              "id": 86,
              "name": "Ownable",
              "nodeType": "UserDefinedTypeName",
              "referencedDeclaration": 85,
              "src": "1713:7:0",
              "typeDescriptions": {
                "typeIdentifier": "t_contract$_Ownable_$85",
                "typeString": "contract Ownable"
              }
            },
            "id": 87,
            "nodeType": "InheritanceSpecifier",
            "src": "1713:7:0"
          }
        ],
        "contractDependencies": [
          85
        ],
        "contractKind": "contract",
        "documentation": null,
        "fullyImplemented": true,
        "id": 428,
        "linearizedBaseContracts": [
          428,
          85
        ],
        "name": "IdentityStore",
        "nodeType": "ContractDefinition",
        "nodes": [
          {
            "canonicalName": "IdentityStore.User",
            "id": 94,
            "members": [
              {
                "constant": false,
                "id": 89,
                "name": "tenantHash",
                "nodeType": "VariableDeclaration",
                "scope": 94,
                "src": "1752:18:0",
                "stateVariable": false,
                "storageLocation": "default",
                "typeDescriptions": {
                  "typeIdentifier": "t_bytes32",
                  "typeString": "bytes32"
                },
                "typeName": {
                  "id": 88,
                  "name": "bytes32",
                  "nodeType": "ElementaryTypeName",
                  "src": "1752:7:0",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                  }
                },
                "value": null,
                "visibility": "internal"
              },
              {
                "constant": false,
                "id": 91,
                "name": "timestamp",
                "nodeType": "VariableDeclaration",
                "scope": 94,
                "src": "1780:17:0",
                "stateVariable": false,
                "storageLocation": "default",
                "typeDescriptions": {
                  "typeIdentifier": "t_uint256",
                  "typeString": "uint256"
                },
                "typeName": {
                  "id": 90,
                  "name": "uint256",
                  "nodeType": "ElementaryTypeName",
                  "src": "1780:7:0",
                  "typeDescriptions": {
                    "typeIdentifier": "t_uint256",
                    "typeString": "uint256"
                  }
                },
                "value": null,
                "visibility": "internal"
              },
              {
                "constant": false,
                "id": 93,
                "name": "tenantId",
                "nodeType": "VariableDeclaration",
                "scope": 94,
                "src": "1807:15:0",
                "stateVariable": false,
                "storageLocation": "default",
                "typeDescriptions": {
                  "typeIdentifier": "t_string_storage_ptr",
                  "typeString": "string"
                },
                "typeName": {
                  "id": 92,
                  "name": "string",
                  "nodeType": "ElementaryTypeName",
                  "src": "1807:6:0",
                  "typeDescriptions": {
                    "typeIdentifier": "t_string_storage_ptr",
                    "typeString": "string"
                  }
                },
                "value": null,
                "visibility": "internal"
              }
            ],
            "name": "User",
            "nodeType": "StructDefinition",
            "scope": 428,
            "src": "1730:99:0",
            "visibility": "public"
          },
          {
            "constant": false,
            "id": 98,
            "name": "tenantAddressMapping",
            "nodeType": "VariableDeclaration",
            "scope": 428,
            "src": "1835:53:0",
            "stateVariable": true,
            "storageLocation": "default",
            "typeDescriptions": {
              "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
              "typeString": "mapping(address => struct IdentityStore.User)"
            },
            "typeName": {
              "id": 97,
              "keyType": {
                "id": 95,
                "name": "address",
                "nodeType": "ElementaryTypeName",
                "src": "1843:7:0",
                "typeDescriptions": {
                  "typeIdentifier": "t_address",
                  "typeString": "address"
                }
              },
              "nodeType": "Mapping",
              "src": "1835:24:0",
              "typeDescriptions": {
                "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                "typeString": "mapping(address => struct IdentityStore.User)"
              },
              "valueType": {
                "contractScope": null,
                "id": 96,
                "name": "User",
                "nodeType": "UserDefinedTypeName",
                "referencedDeclaration": 94,
                "src": "1854:4:0",
                "typeDescriptions": {
                  "typeIdentifier": "t_struct$_User_$94_storage_ptr",
                  "typeString": "struct IdentityStore.User"
                }
              }
            },
            "value": null,
            "visibility": "private"
          },
          {
            "constant": false,
            "id": 102,
            "name": "tenantHashMapping",
            "nodeType": "VariableDeclaration",
            "scope": 428,
            "src": "1894:53:0",
            "stateVariable": true,
            "storageLocation": "default",
            "typeDescriptions": {
              "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
              "typeString": "mapping(bytes32 => address)"
            },
            "typeName": {
              "id": 101,
              "keyType": {
                "id": 99,
                "name": "bytes32",
                "nodeType": "ElementaryTypeName",
                "src": "1902:7:0",
                "typeDescriptions": {
                  "typeIdentifier": "t_bytes32",
                  "typeString": "bytes32"
                }
              },
              "nodeType": "Mapping",
              "src": "1894:27:0",
              "typeDescriptions": {
                "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                "typeString": "mapping(bytes32 => address)"
              },
              "valueType": {
                "id": 100,
                "name": "address",
                "nodeType": "ElementaryTypeName",
                "src": "1913:7:0",
                "typeDescriptions": {
                  "typeIdentifier": "t_address",
                  "typeString": "address"
                }
              }
            },
            "value": null,
            "visibility": "private"
          },
          {
            "body": {
              "id": 208,
              "nodeType": "Block",
              "src": "2105:1133:0",
              "statements": [
                {
                  "condition": {
                    "argumentTypes": null,
                    "commonType": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    },
                    "id": 123,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftExpression": {
                      "argumentTypes": null,
                      "id": 118,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "lValueRequested": false,
                      "nodeType": "UnaryOperation",
                      "operator": "!",
                      "prefix": true,
                      "src": "2151:32:0",
                      "subExpression": {
                        "argumentTypes": null,
                        "arguments": [
                          {
                            "argumentTypes": null,
                            "id": 116,
                            "name": "_userAddress",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 106,
                            "src": "2170:12:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            }
                          }
                        ],
                        "expression": {
                          "argumentTypes": [
                            {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            }
                          ],
                          "id": 115,
                          "name": "userAddressExists",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 408,
                          "src": "2152:17:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_function_internal_view$_t_address_$returns$_t_bool_$",
                            "typeString": "function (address) view returns (bool)"
                          }
                        },
                        "id": 117,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "2152:31:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      },
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "nodeType": "BinaryOperation",
                    "operator": "&&",
                    "rightExpression": {
                      "argumentTypes": null,
                      "id": 122,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "lValueRequested": false,
                      "nodeType": "UnaryOperation",
                      "operator": "!",
                      "prefix": true,
                      "src": "2187:34:0",
                      "subExpression": {
                        "argumentTypes": null,
                        "arguments": [
                          {
                            "argumentTypes": null,
                            "id": 120,
                            "name": "_tenantHash",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 104,
                            "src": "2209:11:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            }
                          }
                        ],
                        "expression": {
                          "argumentTypes": [
                            {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            }
                          ],
                          "id": 119,
                          "name": "userTenantHashExists",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 427,
                          "src": "2188:20:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_function_internal_view$_t_bytes32_$returns$_t_bool_$",
                            "typeString": "function (bytes32) view returns (bool)"
                          }
                        },
                        "id": 121,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "2188:33:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      },
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "src": "2151:70:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 146,
                  "nodeType": "IfStatement",
                  "src": "2147:313:0",
                  "trueBody": {
                    "id": 145,
                    "nodeType": "Block",
                    "src": "2223:237:0",
                    "statements": [
                      {
                        "assignments": [
                          125
                        ],
                        "declarations": [
                          {
                            "constant": false,
                            "id": 125,
                            "name": "newUser",
                            "nodeType": "VariableDeclaration",
                            "scope": 209,
                            "src": "2250:19:0",
                            "stateVariable": false,
                            "storageLocation": "memory",
                            "typeDescriptions": {
                              "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                              "typeString": "struct IdentityStore.User"
                            },
                            "typeName": {
                              "contractScope": null,
                              "id": 124,
                              "name": "User",
                              "nodeType": "UserDefinedTypeName",
                              "referencedDeclaration": 94,
                              "src": "2250:4:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_struct$_User_$94_storage_ptr",
                                "typeString": "struct IdentityStore.User"
                              }
                            },
                            "value": null,
                            "visibility": "internal"
                          }
                        ],
                        "id": 131,
                        "initialValue": {
                          "argumentTypes": null,
                          "arguments": [
                            {
                              "argumentTypes": null,
                              "id": 127,
                              "name": "_tenantHash",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 104,
                              "src": "2277:11:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              }
                            },
                            {
                              "argumentTypes": null,
                              "id": 128,
                              "name": "_timestamp",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 108,
                              "src": "2290:10:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_uint256",
                                "typeString": "uint256"
                              }
                            },
                            {
                              "argumentTypes": null,
                              "id": 129,
                              "name": "_tenantId",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 110,
                              "src": "2302:9:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_string_memory_ptr",
                                "typeString": "string memory"
                              }
                            }
                          ],
                          "expression": {
                            "argumentTypes": [
                              {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              },
                              {
                                "typeIdentifier": "t_uint256",
                                "typeString": "uint256"
                              },
                              {
                                "typeIdentifier": "t_string_memory_ptr",
                                "typeString": "string memory"
                              }
                            ],
                            "id": 126,
                            "name": "User",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 94,
                            "src": "2272:4:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_type$_t_struct$_User_$94_storage_ptr_$",
                              "typeString": "type(struct IdentityStore.User storage pointer)"
                            }
                          },
                          "id": 130,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "kind": "structConstructorCall",
                          "lValueRequested": false,
                          "names": [],
                          "nodeType": "FunctionCall",
                          "src": "2272:40:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_struct$_User_$94_memory",
                            "typeString": "struct IdentityStore.User memory"
                          }
                        },
                        "nodeType": "VariableDeclarationStatement",
                        "src": "2250:62:0"
                      },
                      {
                        "expression": {
                          "argumentTypes": null,
                          "id": 136,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "lValueRequested": false,
                          "leftHandSide": {
                            "argumentTypes": null,
                            "baseExpression": {
                              "argumentTypes": null,
                              "id": 132,
                              "name": "tenantAddressMapping",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 98,
                              "src": "2326:20:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                                "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                              }
                            },
                            "id": 134,
                            "indexExpression": {
                              "argumentTypes": null,
                              "id": 133,
                              "name": "_userAddress",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 106,
                              "src": "2347:12:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              }
                            },
                            "isConstant": false,
                            "isLValue": true,
                            "isPure": false,
                            "lValueRequested": true,
                            "nodeType": "IndexAccess",
                            "src": "2326:34:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_struct$_User_$94_storage",
                              "typeString": "struct IdentityStore.User storage ref"
                            }
                          },
                          "nodeType": "Assignment",
                          "operator": "=",
                          "rightHandSide": {
                            "argumentTypes": null,
                            "id": 135,
                            "name": "newUser",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 125,
                            "src": "2363:7:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                              "typeString": "struct IdentityStore.User memory"
                            }
                          },
                          "src": "2326:44:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_struct$_User_$94_storage",
                            "typeString": "struct IdentityStore.User storage ref"
                          }
                        },
                        "id": 137,
                        "nodeType": "ExpressionStatement",
                        "src": "2326:44:0"
                      },
                      {
                        "expression": {
                          "argumentTypes": null,
                          "id": 142,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "lValueRequested": false,
                          "leftHandSide": {
                            "argumentTypes": null,
                            "baseExpression": {
                              "argumentTypes": null,
                              "id": 138,
                              "name": "tenantHashMapping",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 102,
                              "src": "2384:17:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                                "typeString": "mapping(bytes32 => address)"
                              }
                            },
                            "id": 140,
                            "indexExpression": {
                              "argumentTypes": null,
                              "id": 139,
                              "name": "_tenantHash",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 104,
                              "src": "2402:11:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              }
                            },
                            "isConstant": false,
                            "isLValue": true,
                            "isPure": false,
                            "lValueRequested": true,
                            "nodeType": "IndexAccess",
                            "src": "2384:30:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            }
                          },
                          "nodeType": "Assignment",
                          "operator": "=",
                          "rightHandSide": {
                            "argumentTypes": null,
                            "id": 141,
                            "name": "_userAddress",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 106,
                            "src": "2417:12:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            }
                          },
                          "src": "2384:45:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        },
                        "id": 143,
                        "nodeType": "ExpressionStatement",
                        "src": "2384:45:0"
                      },
                      {
                        "expression": null,
                        "functionReturnParameters": 114,
                        "id": 144,
                        "nodeType": "Return",
                        "src": "2443:7:0"
                      }
                    ]
                  }
                },
                {
                  "condition": {
                    "argumentTypes": null,
                    "commonType": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    },
                    "id": 154,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftExpression": {
                      "argumentTypes": null,
                      "arguments": [
                        {
                          "argumentTypes": null,
                          "id": 148,
                          "name": "_userAddress",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 106,
                          "src": "2521:12:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        }
                      ],
                      "expression": {
                        "argumentTypes": [
                          {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        ],
                        "id": 147,
                        "name": "userAddressExists",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 408,
                        "src": "2503:17:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_function_internal_view$_t_address_$returns$_t_bool_$",
                          "typeString": "function (address) view returns (bool)"
                        }
                      },
                      "id": 149,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "kind": "functionCall",
                      "lValueRequested": false,
                      "names": [],
                      "nodeType": "FunctionCall",
                      "src": "2503:31:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "nodeType": "BinaryOperation",
                    "operator": "&&",
                    "rightExpression": {
                      "argumentTypes": null,
                      "id": 153,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "lValueRequested": false,
                      "nodeType": "UnaryOperation",
                      "operator": "!",
                      "prefix": true,
                      "src": "2538:34:0",
                      "subExpression": {
                        "argumentTypes": null,
                        "arguments": [
                          {
                            "argumentTypes": null,
                            "id": 151,
                            "name": "_tenantHash",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 104,
                            "src": "2560:11:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            }
                          }
                        ],
                        "expression": {
                          "argumentTypes": [
                            {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            }
                          ],
                          "id": 150,
                          "name": "userTenantHashExists",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 427,
                          "src": "2539:20:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_function_internal_view$_t_bytes32_$returns$_t_bool_$",
                            "typeString": "function (bytes32) view returns (bool)"
                          }
                        },
                        "id": 152,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "2539:33:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      },
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "src": "2503:69:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 170,
                  "nodeType": "IfStatement",
                  "src": "2499:254:0",
                  "trueBody": {
                    "id": 169,
                    "nodeType": "Block",
                    "src": "2574:179:0",
                    "statements": [
                      {
                        "assignments": [
                          156
                        ],
                        "declarations": [
                          {
                            "constant": false,
                            "id": 156,
                            "name": "oldHash",
                            "nodeType": "VariableDeclaration",
                            "scope": 209,
                            "src": "2601:15:0",
                            "stateVariable": false,
                            "storageLocation": "default",
                            "typeDescriptions": {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            },
                            "typeName": {
                              "id": 155,
                              "name": "bytes32",
                              "nodeType": "ElementaryTypeName",
                              "src": "2601:7:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              }
                            },
                            "value": null,
                            "visibility": "internal"
                          }
                        ],
                        "id": 161,
                        "initialValue": {
                          "argumentTypes": null,
                          "expression": {
                            "argumentTypes": null,
                            "baseExpression": {
                              "argumentTypes": null,
                              "id": 157,
                              "name": "tenantAddressMapping",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 98,
                              "src": "2619:20:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                                "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                              }
                            },
                            "id": 159,
                            "indexExpression": {
                              "argumentTypes": null,
                              "id": 158,
                              "name": "_userAddress",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 106,
                              "src": "2640:12:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              }
                            },
                            "isConstant": false,
                            "isLValue": true,
                            "isPure": false,
                            "lValueRequested": false,
                            "nodeType": "IndexAccess",
                            "src": "2619:34:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_struct$_User_$94_storage",
                              "typeString": "struct IdentityStore.User storage ref"
                            }
                          },
                          "id": 160,
                          "isConstant": false,
                          "isLValue": true,
                          "isPure": false,
                          "lValueRequested": false,
                          "memberName": "tenantHash",
                          "nodeType": "MemberAccess",
                          "referencedDeclaration": 89,
                          "src": "2619:45:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                          }
                        },
                        "nodeType": "VariableDeclarationStatement",
                        "src": "2601:63:0"
                      },
                      {
                        "expression": {
                          "argumentTypes": null,
                          "arguments": [
                            {
                              "argumentTypes": null,
                              "id": 163,
                              "name": "oldHash",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 156,
                              "src": "2689:7:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              }
                            },
                            {
                              "argumentTypes": null,
                              "id": 164,
                              "name": "_tenantHash",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 104,
                              "src": "2698:11:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              }
                            },
                            {
                              "argumentTypes": null,
                              "id": 165,
                              "name": "_timestamp",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 108,
                              "src": "2711:10:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_uint256",
                                "typeString": "uint256"
                              }
                            }
                          ],
                          "expression": {
                            "argumentTypes": [
                              {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              },
                              {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              },
                              {
                                "typeIdentifier": "t_uint256",
                                "typeString": "uint256"
                              }
                            ],
                            "id": 162,
                            "name": "updateHash",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 320,
                            "src": "2678:10:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_function_internal_nonpayable$_t_bytes32_$_t_bytes32_$_t_uint256_$returns$__$",
                              "typeString": "function (bytes32,bytes32,uint256)"
                            }
                          },
                          "id": 166,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "kind": "functionCall",
                          "lValueRequested": false,
                          "names": [],
                          "nodeType": "FunctionCall",
                          "src": "2678:44:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_tuple$__$",
                            "typeString": "tuple()"
                          }
                        },
                        "id": 167,
                        "nodeType": "ExpressionStatement",
                        "src": "2678:44:0"
                      },
                      {
                        "expression": null,
                        "functionReturnParameters": 114,
                        "id": 168,
                        "nodeType": "Return",
                        "src": "2736:7:0"
                      }
                    ]
                  }
                },
                {
                  "condition": {
                    "argumentTypes": null,
                    "commonType": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    },
                    "id": 178,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftExpression": {
                      "argumentTypes": null,
                      "arguments": [
                        {
                          "argumentTypes": null,
                          "id": 172,
                          "name": "_tenantHash",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 104,
                          "src": "2828:11:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                          }
                        }
                      ],
                      "expression": {
                        "argumentTypes": [
                          {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                          }
                        ],
                        "id": 171,
                        "name": "userTenantHashExists",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 427,
                        "src": "2807:20:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_function_internal_view$_t_bytes32_$returns$_t_bool_$",
                          "typeString": "function (bytes32) view returns (bool)"
                        }
                      },
                      "id": 173,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "kind": "functionCall",
                      "lValueRequested": false,
                      "names": [],
                      "nodeType": "FunctionCall",
                      "src": "2807:33:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "nodeType": "BinaryOperation",
                    "operator": "&&",
                    "rightExpression": {
                      "argumentTypes": null,
                      "id": 177,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "lValueRequested": false,
                      "nodeType": "UnaryOperation",
                      "operator": "!",
                      "prefix": true,
                      "src": "2844:32:0",
                      "subExpression": {
                        "argumentTypes": null,
                        "arguments": [
                          {
                            "argumentTypes": null,
                            "id": 175,
                            "name": "_userAddress",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 106,
                            "src": "2863:12:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            }
                          }
                        ],
                        "expression": {
                          "argumentTypes": [
                            {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            }
                          ],
                          "id": 174,
                          "name": "userAddressExists",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 408,
                          "src": "2845:17:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_function_internal_view$_t_address_$returns$_t_bool_$",
                            "typeString": "function (address) view returns (bool)"
                          }
                        },
                        "id": 176,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "2845:31:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      },
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "src": "2807:69:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 192,
                  "nodeType": "IfStatement",
                  "src": "2803:224:0",
                  "trueBody": {
                    "id": 191,
                    "nodeType": "Block",
                    "src": "2878:149:0",
                    "statements": [
                      {
                        "assignments": [
                          180
                        ],
                        "declarations": [
                          {
                            "constant": false,
                            "id": 180,
                            "name": "oldAddress",
                            "nodeType": "VariableDeclaration",
                            "scope": 209,
                            "src": "2892:18:0",
                            "stateVariable": false,
                            "storageLocation": "default",
                            "typeDescriptions": {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            },
                            "typeName": {
                              "id": 179,
                              "name": "address",
                              "nodeType": "ElementaryTypeName",
                              "src": "2892:7:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              }
                            },
                            "value": null,
                            "visibility": "internal"
                          }
                        ],
                        "id": 184,
                        "initialValue": {
                          "argumentTypes": null,
                          "baseExpression": {
                            "argumentTypes": null,
                            "id": 181,
                            "name": "tenantHashMapping",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 102,
                            "src": "2913:17:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                              "typeString": "mapping(bytes32 => address)"
                            }
                          },
                          "id": 183,
                          "indexExpression": {
                            "argumentTypes": null,
                            "id": 182,
                            "name": "_tenantHash",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 104,
                            "src": "2931:11:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            }
                          },
                          "isConstant": false,
                          "isLValue": true,
                          "isPure": false,
                          "lValueRequested": false,
                          "nodeType": "IndexAccess",
                          "src": "2913:30:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        },
                        "nodeType": "VariableDeclarationStatement",
                        "src": "2892:51:0"
                      },
                      {
                        "expression": {
                          "argumentTypes": null,
                          "arguments": [
                            {
                              "argumentTypes": null,
                              "id": 186,
                              "name": "oldAddress",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 180,
                              "src": "2971:10:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              }
                            },
                            {
                              "argumentTypes": null,
                              "id": 187,
                              "name": "_userAddress",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 106,
                              "src": "2983:12:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              }
                            }
                          ],
                          "expression": {
                            "argumentTypes": [
                              {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              },
                              {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              }
                            ],
                            "id": 185,
                            "name": "updateAddress",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 369,
                            "src": "2957:13:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_function_internal_nonpayable$_t_address_$_t_address_$returns$__$",
                              "typeString": "function (address,address)"
                            }
                          },
                          "id": 188,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "kind": "functionCall",
                          "lValueRequested": false,
                          "names": [],
                          "nodeType": "FunctionCall",
                          "src": "2957:39:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_tuple$__$",
                            "typeString": "tuple()"
                          }
                        },
                        "id": 189,
                        "nodeType": "ExpressionStatement",
                        "src": "2957:39:0"
                      },
                      {
                        "expression": null,
                        "functionReturnParameters": 114,
                        "id": 190,
                        "nodeType": "Return",
                        "src": "3010:7:0"
                      }
                    ]
                  }
                },
                {
                  "condition": {
                    "argumentTypes": null,
                    "commonType": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    },
                    "id": 199,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftExpression": {
                      "argumentTypes": null,
                      "arguments": [
                        {
                          "argumentTypes": null,
                          "id": 194,
                          "name": "_tenantHash",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 104,
                          "src": "3098:11:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                          }
                        }
                      ],
                      "expression": {
                        "argumentTypes": [
                          {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                          }
                        ],
                        "id": 193,
                        "name": "userTenantHashExists",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 427,
                        "src": "3077:20:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_function_internal_view$_t_bytes32_$returns$_t_bool_$",
                          "typeString": "function (bytes32) view returns (bool)"
                        }
                      },
                      "id": 195,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "kind": "functionCall",
                      "lValueRequested": false,
                      "names": [],
                      "nodeType": "FunctionCall",
                      "src": "3077:33:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "nodeType": "BinaryOperation",
                    "operator": "&&",
                    "rightExpression": {
                      "argumentTypes": null,
                      "arguments": [
                        {
                          "argumentTypes": null,
                          "id": 197,
                          "name": "_userAddress",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 106,
                          "src": "3132:12:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        }
                      ],
                      "expression": {
                        "argumentTypes": [
                          {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        ],
                        "id": 196,
                        "name": "userAddressExists",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 408,
                        "src": "3114:17:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_function_internal_view$_t_address_$returns$_t_bool_$",
                          "typeString": "function (address) view returns (bool)"
                        }
                      },
                      "id": 198,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "kind": "functionCall",
                      "lValueRequested": false,
                      "names": [],
                      "nodeType": "FunctionCall",
                      "src": "3114:31:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "src": "3077:68:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 207,
                  "nodeType": "IfStatement",
                  "src": "3073:159:0",
                  "trueBody": {
                    "id": 206,
                    "nodeType": "Block",
                    "src": "3147:85:0",
                    "statements": [
                      {
                        "expression": {
                          "argumentTypes": null,
                          "arguments": [
                            {
                              "argumentTypes": null,
                              "id": 201,
                              "name": "_tenantHash",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 104,
                              "src": "3177:11:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              }
                            },
                            {
                              "argumentTypes": null,
                              "id": 202,
                              "name": "_timestamp",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 108,
                              "src": "3190:10:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_uint256",
                                "typeString": "uint256"
                              }
                            }
                          ],
                          "expression": {
                            "argumentTypes": [
                              {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              },
                              {
                                "typeIdentifier": "t_uint256",
                                "typeString": "uint256"
                              }
                            ],
                            "id": 200,
                            "name": "updateTimestamp",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 388,
                            "src": "3161:15:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_function_internal_nonpayable$_t_bytes32_$_t_uint256_$returns$__$",
                              "typeString": "function (bytes32,uint256)"
                            }
                          },
                          "id": 203,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "kind": "functionCall",
                          "lValueRequested": false,
                          "names": [],
                          "nodeType": "FunctionCall",
                          "src": "3161:40:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_tuple$__$",
                            "typeString": "tuple()"
                          }
                        },
                        "id": 204,
                        "nodeType": "ExpressionStatement",
                        "src": "3161:40:0"
                      },
                      {
                        "expression": null,
                        "functionReturnParameters": 114,
                        "id": 205,
                        "nodeType": "Return",
                        "src": "3215:7:0"
                      }
                    ]
                  }
                }
              ]
            },
            "documentation": null,
            "id": 209,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": false,
            "modifiers": [
              {
                "arguments": null,
                "id": 113,
                "modifierName": {
                  "argumentTypes": null,
                  "id": 112,
                  "name": "onlyOwner",
                  "nodeType": "Identifier",
                  "overloadedDeclarations": [],
                  "referencedDeclaration": 33,
                  "src": "2088:9:0",
                  "typeDescriptions": {
                    "typeIdentifier": "t_modifier$__$",
                    "typeString": "modifier ()"
                  }
                },
                "nodeType": "ModifierInvocation",
                "src": "2088:9:0"
              }
            ],
            "name": "setTenant",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 111,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 104,
                  "name": "_tenantHash",
                  "nodeType": "VariableDeclaration",
                  "scope": 209,
                  "src": "1983:19:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                  },
                  "typeName": {
                    "id": 103,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "1983:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bytes32",
                      "typeString": "bytes32"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 106,
                  "name": "_userAddress",
                  "nodeType": "VariableDeclaration",
                  "scope": 209,
                  "src": "2012:20:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 105,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "2012:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 108,
                  "name": "_timestamp",
                  "nodeType": "VariableDeclaration",
                  "scope": 209,
                  "src": "2042:18:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_uint256",
                    "typeString": "uint256"
                  },
                  "typeName": {
                    "id": 107,
                    "name": "uint256",
                    "nodeType": "ElementaryTypeName",
                    "src": "2042:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_uint256",
                      "typeString": "uint256"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 110,
                  "name": "_tenantId",
                  "nodeType": "VariableDeclaration",
                  "scope": 209,
                  "src": "2070:16:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_string_memory_ptr",
                    "typeString": "string"
                  },
                  "typeName": {
                    "id": 109,
                    "name": "string",
                    "nodeType": "ElementaryTypeName",
                    "src": "2070:6:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_string_storage_ptr",
                      "typeString": "string"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "1973:114:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 114,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "2105:0:0"
            },
            "scope": 428,
            "src": "1955:1283:0",
            "stateMutability": "nonpayable",
            "superFunction": null,
            "visibility": "public"
          },
          {
            "body": {
              "id": 256,
              "nodeType": "Block",
              "src": "3376:487:0",
              "statements": [
                {
                  "condition": {
                    "argumentTypes": null,
                    "id": 223,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "nodeType": "UnaryOperation",
                    "operator": "!",
                    "prefix": true,
                    "src": "3421:32:0",
                    "subExpression": {
                      "argumentTypes": null,
                      "arguments": [
                        {
                          "argumentTypes": null,
                          "id": 221,
                          "name": "_userAddress",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 213,
                          "src": "3440:12:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        }
                      ],
                      "expression": {
                        "argumentTypes": [
                          {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        ],
                        "id": 220,
                        "name": "userAddressExists",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 408,
                        "src": "3422:17:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_function_internal_view$_t_address_$returns$_t_bool_$",
                          "typeString": "function (address) view returns (bool)"
                        }
                      },
                      "id": 222,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "kind": "functionCall",
                      "lValueRequested": false,
                      "names": [],
                      "nodeType": "FunctionCall",
                      "src": "3422:31:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 227,
                  "nodeType": "IfStatement",
                  "src": "3418:74:0",
                  "trueBody": {
                    "id": 226,
                    "nodeType": "Block",
                    "src": "3455:37:0",
                    "statements": [
                      {
                        "expression": {
                          "argumentTypes": null,
                          "hexValue": "66616c7365",
                          "id": 224,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": true,
                          "kind": "bool",
                          "lValueRequested": false,
                          "nodeType": "Literal",
                          "src": "3476:5:0",
                          "subdenomination": null,
                          "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                          },
                          "value": "false"
                        },
                        "functionReturnParameters": 219,
                        "id": 225,
                        "nodeType": "Return",
                        "src": "3469:12:0"
                      }
                    ]
                  }
                },
                {
                  "assignments": [
                    229
                  ],
                  "declarations": [
                    {
                      "constant": false,
                      "id": 229,
                      "name": "currentUser",
                      "nodeType": "VariableDeclaration",
                      "scope": 257,
                      "src": "3502:23:0",
                      "stateVariable": false,
                      "storageLocation": "memory",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                        "typeString": "struct IdentityStore.User"
                      },
                      "typeName": {
                        "contractScope": null,
                        "id": 228,
                        "name": "User",
                        "nodeType": "UserDefinedTypeName",
                        "referencedDeclaration": 94,
                        "src": "3502:4:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_struct$_User_$94_storage_ptr",
                          "typeString": "struct IdentityStore.User"
                        }
                      },
                      "value": null,
                      "visibility": "internal"
                    }
                  ],
                  "id": 233,
                  "initialValue": {
                    "argumentTypes": null,
                    "baseExpression": {
                      "argumentTypes": null,
                      "id": 230,
                      "name": "tenantAddressMapping",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 98,
                      "src": "3528:20:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                        "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                      }
                    },
                    "id": 232,
                    "indexExpression": {
                      "argumentTypes": null,
                      "id": 231,
                      "name": "_userAddress",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 213,
                      "src": "3549:12:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "isConstant": false,
                    "isLValue": true,
                    "isPure": false,
                    "lValueRequested": false,
                    "nodeType": "IndexAccess",
                    "src": "3528:34:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_struct$_User_$94_storage",
                      "typeString": "struct IdentityStore.User storage ref"
                    }
                  },
                  "nodeType": "VariableDeclarationStatement",
                  "src": "3502:60:0"
                },
                {
                  "condition": {
                    "argumentTypes": null,
                    "commonType": {
                      "typeIdentifier": "t_bytes32",
                      "typeString": "bytes32"
                    },
                    "id": 241,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftExpression": {
                      "argumentTypes": null,
                      "arguments": [
                        {
                          "argumentTypes": null,
                          "expression": {
                            "argumentTypes": null,
                            "id": 235,
                            "name": "currentUser",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 229,
                            "src": "3619:11:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                              "typeString": "struct IdentityStore.User memory"
                            }
                          },
                          "id": 236,
                          "isConstant": false,
                          "isLValue": true,
                          "isPure": false,
                          "lValueRequested": false,
                          "memberName": "tenantId",
                          "nodeType": "MemberAccess",
                          "referencedDeclaration": 93,
                          "src": "3619:20:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_string_memory",
                            "typeString": "string memory"
                          }
                        }
                      ],
                      "expression": {
                        "argumentTypes": [
                          {
                            "typeIdentifier": "t_string_memory",
                            "typeString": "string memory"
                          }
                        ],
                        "id": 234,
                        "name": "keccak256",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 523,
                        "src": "3609:9:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_function_sha3_pure$__$returns$_t_bytes32_$",
                          "typeString": "function () pure returns (bytes32)"
                        }
                      },
                      "id": 237,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "kind": "functionCall",
                      "lValueRequested": false,
                      "names": [],
                      "nodeType": "FunctionCall",
                      "src": "3609:31:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                      }
                    },
                    "nodeType": "BinaryOperation",
                    "operator": "!=",
                    "rightExpression": {
                      "argumentTypes": null,
                      "arguments": [
                        {
                          "argumentTypes": null,
                          "id": 239,
                          "name": "_tenantId",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 211,
                          "src": "3654:9:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_string_memory_ptr",
                            "typeString": "string memory"
                          }
                        }
                      ],
                      "expression": {
                        "argumentTypes": [
                          {
                            "typeIdentifier": "t_string_memory_ptr",
                            "typeString": "string memory"
                          }
                        ],
                        "id": 238,
                        "name": "keccak256",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 523,
                        "src": "3644:9:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_function_sha3_pure$__$returns$_t_bytes32_$",
                          "typeString": "function () pure returns (bytes32)"
                        }
                      },
                      "id": 240,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "kind": "functionCall",
                      "lValueRequested": false,
                      "names": [],
                      "nodeType": "FunctionCall",
                      "src": "3644:20:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                      }
                    },
                    "src": "3609:55:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 245,
                  "nodeType": "IfStatement",
                  "src": "3606:97:0",
                  "trueBody": {
                    "id": 244,
                    "nodeType": "Block",
                    "src": "3666:37:0",
                    "statements": [
                      {
                        "expression": {
                          "argumentTypes": null,
                          "hexValue": "66616c7365",
                          "id": 242,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": true,
                          "kind": "bool",
                          "lValueRequested": false,
                          "nodeType": "Literal",
                          "src": "3687:5:0",
                          "subdenomination": null,
                          "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                          },
                          "value": "false"
                        },
                        "functionReturnParameters": 219,
                        "id": 243,
                        "nodeType": "Return",
                        "src": "3680:12:0"
                      }
                    ]
                  }
                },
                {
                  "condition": {
                    "argumentTypes": null,
                    "commonType": {
                      "typeIdentifier": "t_uint256",
                      "typeString": "uint256"
                    },
                    "id": 249,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftExpression": {
                      "argumentTypes": null,
                      "expression": {
                        "argumentTypes": null,
                        "id": 246,
                        "name": "currentUser",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 229,
                        "src": "3759:11:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                          "typeString": "struct IdentityStore.User memory"
                        }
                      },
                      "id": 247,
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": false,
                      "memberName": "timestamp",
                      "nodeType": "MemberAccess",
                      "referencedDeclaration": 91,
                      "src": "3759:21:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_uint256",
                        "typeString": "uint256"
                      }
                    },
                    "nodeType": "BinaryOperation",
                    "operator": "<",
                    "rightExpression": {
                      "argumentTypes": null,
                      "id": 248,
                      "name": "_minTimestamp",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 215,
                      "src": "3783:13:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_uint256",
                        "typeString": "uint256"
                      }
                    },
                    "src": "3759:37:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 253,
                  "nodeType": "IfStatement",
                  "src": "3756:79:0",
                  "trueBody": {
                    "id": 252,
                    "nodeType": "Block",
                    "src": "3798:37:0",
                    "statements": [
                      {
                        "expression": {
                          "argumentTypes": null,
                          "hexValue": "66616c7365",
                          "id": 250,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": true,
                          "kind": "bool",
                          "lValueRequested": false,
                          "nodeType": "Literal",
                          "src": "3819:5:0",
                          "subdenomination": null,
                          "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                          },
                          "value": "false"
                        },
                        "functionReturnParameters": 219,
                        "id": 251,
                        "nodeType": "Return",
                        "src": "3812:12:0"
                      }
                    ]
                  }
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "hexValue": "74727565",
                    "id": 254,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": true,
                    "kind": "bool",
                    "lValueRequested": false,
                    "nodeType": "Literal",
                    "src": "3852:4:0",
                    "subdenomination": null,
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    },
                    "value": "true"
                  },
                  "functionReturnParameters": 219,
                  "id": 255,
                  "nodeType": "Return",
                  "src": "3845:11:0"
                }
              ]
            },
            "documentation": null,
            "id": 257,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": true,
            "modifiers": [],
            "name": "isValid",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 216,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 211,
                  "name": "_tenantId",
                  "nodeType": "VariableDeclaration",
                  "scope": 257,
                  "src": "3270:16:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_string_memory_ptr",
                    "typeString": "string"
                  },
                  "typeName": {
                    "id": 210,
                    "name": "string",
                    "nodeType": "ElementaryTypeName",
                    "src": "3270:6:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_string_storage_ptr",
                      "typeString": "string"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 213,
                  "name": "_userAddress",
                  "nodeType": "VariableDeclaration",
                  "scope": 257,
                  "src": "3297:20:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 212,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "3297:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 215,
                  "name": "_minTimestamp",
                  "nodeType": "VariableDeclaration",
                  "scope": 257,
                  "src": "3327:21:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_uint256",
                    "typeString": "uint256"
                  },
                  "typeName": {
                    "id": 214,
                    "name": "uint256",
                    "nodeType": "ElementaryTypeName",
                    "src": "3327:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_uint256",
                      "typeString": "uint256"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "3260:89:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 219,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 218,
                  "name": "",
                  "nodeType": "VariableDeclaration",
                  "scope": 257,
                  "src": "3370:4:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bool",
                    "typeString": "bool"
                  },
                  "typeName": {
                    "id": 217,
                    "name": "bool",
                    "nodeType": "ElementaryTypeName",
                    "src": "3370:4:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "3369:6:0"
            },
            "scope": 428,
            "src": "3244:619:0",
            "stateMutability": "view",
            "superFunction": null,
            "visibility": "public"
          },
          {
            "body": {
              "id": 319,
              "nodeType": "Block",
              "src": "3981:680:0",
              "statements": [
                {
                  "expression": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "arguments": [
                          {
                            "argumentTypes": null,
                            "id": 268,
                            "name": "_oldHash",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 259,
                            "src": "4021:8:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            }
                          }
                        ],
                        "expression": {
                          "argumentTypes": [
                            {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            }
                          ],
                          "id": 267,
                          "name": "userTenantHashExists",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 427,
                          "src": "4000:20:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_function_internal_view$_t_bytes32_$returns$_t_bool_$",
                            "typeString": "function (bytes32) view returns (bool)"
                          }
                        },
                        "id": 269,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "4000:30:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      },
                      {
                        "argumentTypes": null,
                        "hexValue": "4f6c64206861736820646f6573206e6f742065786973742e",
                        "id": 270,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": true,
                        "kind": "string",
                        "lValueRequested": false,
                        "nodeType": "Literal",
                        "src": "4032:26:0",
                        "subdenomination": null,
                        "typeDescriptions": {
                          "typeIdentifier": "t_stringliteral_b8700c17c6c187693f3b5aed9e32b4020bef3af87a53f2dfbedfc5d2ef1b0560",
                          "typeString": "literal_string \"Old hash does not exist.\""
                        },
                        "value": "Old hash does not exist."
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        },
                        {
                          "typeIdentifier": "t_stringliteral_b8700c17c6c187693f3b5aed9e32b4020bef3af87a53f2dfbedfc5d2ef1b0560",
                          "typeString": "literal_string \"Old hash does not exist.\""
                        }
                      ],
                      "id": 266,
                      "name": "require",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [
                        532,
                        533
                      ],
                      "referencedDeclaration": 533,
                      "src": "3992:7:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                        "typeString": "function (bool,string memory) pure"
                      }
                    },
                    "id": 271,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "3992:67:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 272,
                  "nodeType": "ExpressionStatement",
                  "src": "3992:67:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "id": 277,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "nodeType": "UnaryOperation",
                        "operator": "!",
                        "prefix": true,
                        "src": "4077:31:0",
                        "subExpression": {
                          "argumentTypes": null,
                          "arguments": [
                            {
                              "argumentTypes": null,
                              "id": 275,
                              "name": "_newHash",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 261,
                              "src": "4099:8:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              }
                            }
                          ],
                          "expression": {
                            "argumentTypes": [
                              {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              }
                            ],
                            "id": 274,
                            "name": "userTenantHashExists",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 427,
                            "src": "4078:20:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_function_internal_view$_t_bytes32_$returns$_t_bool_$",
                              "typeString": "function (bytes32) view returns (bool)"
                            }
                          },
                          "id": 276,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "kind": "functionCall",
                          "lValueRequested": false,
                          "names": [],
                          "nodeType": "FunctionCall",
                          "src": "4078:30:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                          }
                        },
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      },
                      {
                        "argumentTypes": null,
                        "hexValue": "4e6577206861736820697320616c726561647920726567697374657265642e",
                        "id": 278,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": true,
                        "kind": "string",
                        "lValueRequested": false,
                        "nodeType": "Literal",
                        "src": "4110:33:0",
                        "subdenomination": null,
                        "typeDescriptions": {
                          "typeIdentifier": "t_stringliteral_0ba289e2ad90e453db834a95ce678dd3931ad19c254b07b01da7cb9c678d4148",
                          "typeString": "literal_string \"New hash is already registered.\""
                        },
                        "value": "New hash is already registered."
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        },
                        {
                          "typeIdentifier": "t_stringliteral_0ba289e2ad90e453db834a95ce678dd3931ad19c254b07b01da7cb9c678d4148",
                          "typeString": "literal_string \"New hash is already registered.\""
                        }
                      ],
                      "id": 273,
                      "name": "require",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [
                        532,
                        533
                      ],
                      "referencedDeclaration": 533,
                      "src": "4069:7:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                        "typeString": "function (bool,string memory) pure"
                      }
                    },
                    "id": 279,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "4069:75:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 280,
                  "nodeType": "ExpressionStatement",
                  "src": "4069:75:0"
                },
                {
                  "assignments": [
                    282
                  ],
                  "declarations": [
                    {
                      "constant": false,
                      "id": 282,
                      "name": "currentAddress",
                      "nodeType": "VariableDeclaration",
                      "scope": 320,
                      "src": "4154:22:0",
                      "stateVariable": false,
                      "storageLocation": "default",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      },
                      "typeName": {
                        "id": 281,
                        "name": "address",
                        "nodeType": "ElementaryTypeName",
                        "src": "4154:7:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      },
                      "value": null,
                      "visibility": "internal"
                    }
                  ],
                  "id": 286,
                  "initialValue": {
                    "argumentTypes": null,
                    "baseExpression": {
                      "argumentTypes": null,
                      "id": 283,
                      "name": "tenantHashMapping",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 102,
                      "src": "4179:17:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                        "typeString": "mapping(bytes32 => address)"
                      }
                    },
                    "id": 285,
                    "indexExpression": {
                      "argumentTypes": null,
                      "id": 284,
                      "name": "_oldHash",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 259,
                      "src": "4197:8:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                      }
                    },
                    "isConstant": false,
                    "isLValue": true,
                    "isPure": false,
                    "lValueRequested": false,
                    "nodeType": "IndexAccess",
                    "src": "4179:27:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "nodeType": "VariableDeclarationStatement",
                  "src": "4154:52:0"
                },
                {
                  "assignments": [
                    288
                  ],
                  "declarations": [
                    {
                      "constant": false,
                      "id": 288,
                      "name": "oldUserInfo",
                      "nodeType": "VariableDeclaration",
                      "scope": 320,
                      "src": "4216:23:0",
                      "stateVariable": false,
                      "storageLocation": "memory",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                        "typeString": "struct IdentityStore.User"
                      },
                      "typeName": {
                        "contractScope": null,
                        "id": 287,
                        "name": "User",
                        "nodeType": "UserDefinedTypeName",
                        "referencedDeclaration": 94,
                        "src": "4216:4:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_struct$_User_$94_storage_ptr",
                          "typeString": "struct IdentityStore.User"
                        }
                      },
                      "value": null,
                      "visibility": "internal"
                    }
                  ],
                  "id": 292,
                  "initialValue": {
                    "argumentTypes": null,
                    "baseExpression": {
                      "argumentTypes": null,
                      "id": 289,
                      "name": "tenantAddressMapping",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 98,
                      "src": "4242:20:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                        "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                      }
                    },
                    "id": 291,
                    "indexExpression": {
                      "argumentTypes": null,
                      "id": 290,
                      "name": "currentAddress",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 282,
                      "src": "4263:14:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "isConstant": false,
                    "isLValue": true,
                    "isPure": false,
                    "lValueRequested": false,
                    "nodeType": "IndexAccess",
                    "src": "4242:36:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_struct$_User_$94_storage",
                      "typeString": "struct IdentityStore.User storage ref"
                    }
                  },
                  "nodeType": "VariableDeclarationStatement",
                  "src": "4216:62:0"
                },
                {
                  "assignments": [
                    294
                  ],
                  "declarations": [
                    {
                      "constant": false,
                      "id": 294,
                      "name": "newUserInfo",
                      "nodeType": "VariableDeclaration",
                      "scope": 320,
                      "src": "4288:23:0",
                      "stateVariable": false,
                      "storageLocation": "memory",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                        "typeString": "struct IdentityStore.User"
                      },
                      "typeName": {
                        "contractScope": null,
                        "id": 293,
                        "name": "User",
                        "nodeType": "UserDefinedTypeName",
                        "referencedDeclaration": 94,
                        "src": "4288:4:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_struct$_User_$94_storage_ptr",
                          "typeString": "struct IdentityStore.User"
                        }
                      },
                      "value": null,
                      "visibility": "internal"
                    }
                  ],
                  "id": 301,
                  "initialValue": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "id": 296,
                        "name": "_newHash",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 261,
                        "src": "4319:8:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bytes32",
                          "typeString": "bytes32"
                        }
                      },
                      {
                        "argumentTypes": null,
                        "id": 297,
                        "name": "_timestamp",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 263,
                        "src": "4329:10:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_uint256",
                          "typeString": "uint256"
                        }
                      },
                      {
                        "argumentTypes": null,
                        "expression": {
                          "argumentTypes": null,
                          "id": 298,
                          "name": "oldUserInfo",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 288,
                          "src": "4341:11:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                            "typeString": "struct IdentityStore.User memory"
                          }
                        },
                        "id": 299,
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": false,
                        "memberName": "tenantId",
                        "nodeType": "MemberAccess",
                        "referencedDeclaration": 93,
                        "src": "4341:20:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_string_memory",
                          "typeString": "string memory"
                        }
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_bytes32",
                          "typeString": "bytes32"
                        },
                        {
                          "typeIdentifier": "t_uint256",
                          "typeString": "uint256"
                        },
                        {
                          "typeIdentifier": "t_string_memory",
                          "typeString": "string memory"
                        }
                      ],
                      "id": 295,
                      "name": "User",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 94,
                      "src": "4314:4:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_type$_t_struct$_User_$94_storage_ptr_$",
                        "typeString": "type(struct IdentityStore.User storage pointer)"
                      }
                    },
                    "id": 300,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "structConstructorCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "4314:48:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_struct$_User_$94_memory",
                      "typeString": "struct IdentityStore.User memory"
                    }
                  },
                  "nodeType": "VariableDeclarationStatement",
                  "src": "4288:74:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 306,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftHandSide": {
                      "argumentTypes": null,
                      "baseExpression": {
                        "argumentTypes": null,
                        "id": 302,
                        "name": "tenantAddressMapping",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 98,
                        "src": "4415:20:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                          "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                        }
                      },
                      "id": 304,
                      "indexExpression": {
                        "argumentTypes": null,
                        "id": 303,
                        "name": "currentAddress",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 282,
                        "src": "4436:14:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      },
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": true,
                      "nodeType": "IndexAccess",
                      "src": "4415:36:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_storage",
                        "typeString": "struct IdentityStore.User storage ref"
                      }
                    },
                    "nodeType": "Assignment",
                    "operator": "=",
                    "rightHandSide": {
                      "argumentTypes": null,
                      "id": 305,
                      "name": "newUserInfo",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 294,
                      "src": "4454:11:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                        "typeString": "struct IdentityStore.User memory"
                      }
                    },
                    "src": "4415:50:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_struct$_User_$94_storage",
                      "typeString": "struct IdentityStore.User storage ref"
                    }
                  },
                  "id": 307,
                  "nodeType": "ExpressionStatement",
                  "src": "4415:50:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 311,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "nodeType": "UnaryOperation",
                    "operator": "delete",
                    "prefix": true,
                    "src": "4522:34:0",
                    "subExpression": {
                      "argumentTypes": null,
                      "baseExpression": {
                        "argumentTypes": null,
                        "id": 308,
                        "name": "tenantHashMapping",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 102,
                        "src": "4529:17:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                          "typeString": "mapping(bytes32 => address)"
                        }
                      },
                      "id": 310,
                      "indexExpression": {
                        "argumentTypes": null,
                        "id": 309,
                        "name": "_oldHash",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 259,
                        "src": "4547:8:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bytes32",
                          "typeString": "bytes32"
                        }
                      },
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": true,
                      "nodeType": "IndexAccess",
                      "src": "4529:27:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 312,
                  "nodeType": "ExpressionStatement",
                  "src": "4522:34:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 317,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftHandSide": {
                      "argumentTypes": null,
                      "baseExpression": {
                        "argumentTypes": null,
                        "id": 313,
                        "name": "tenantHashMapping",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 102,
                        "src": "4610:17:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                          "typeString": "mapping(bytes32 => address)"
                        }
                      },
                      "id": 315,
                      "indexExpression": {
                        "argumentTypes": null,
                        "id": 314,
                        "name": "_newHash",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 261,
                        "src": "4628:8:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bytes32",
                          "typeString": "bytes32"
                        }
                      },
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": true,
                      "nodeType": "IndexAccess",
                      "src": "4610:27:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "nodeType": "Assignment",
                    "operator": "=",
                    "rightHandSide": {
                      "argumentTypes": null,
                      "id": 316,
                      "name": "currentAddress",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 282,
                      "src": "4640:14:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "src": "4610:44:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "id": 318,
                  "nodeType": "ExpressionStatement",
                  "src": "4610:44:0"
                }
              ]
            },
            "documentation": null,
            "id": 320,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": false,
            "modifiers": [],
            "name": "updateHash",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 264,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 259,
                  "name": "_oldHash",
                  "nodeType": "VariableDeclaration",
                  "scope": 320,
                  "src": "3898:16:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                  },
                  "typeName": {
                    "id": 258,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "3898:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bytes32",
                      "typeString": "bytes32"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 261,
                  "name": "_newHash",
                  "nodeType": "VariableDeclaration",
                  "scope": 320,
                  "src": "3925:16:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                  },
                  "typeName": {
                    "id": 260,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "3925:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bytes32",
                      "typeString": "bytes32"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 263,
                  "name": "_timestamp",
                  "nodeType": "VariableDeclaration",
                  "scope": 320,
                  "src": "3952:18:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_uint256",
                    "typeString": "uint256"
                  },
                  "typeName": {
                    "id": 262,
                    "name": "uint256",
                    "nodeType": "ElementaryTypeName",
                    "src": "3952:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_uint256",
                      "typeString": "uint256"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "3888:83:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 265,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "3981:0:0"
            },
            "scope": 428,
            "src": "3869:792:0",
            "stateMutability": "nonpayable",
            "superFunction": null,
            "visibility": "internal"
          },
          {
            "body": {
              "id": 368,
              "nodeType": "Block",
              "src": "4757:478:0",
              "statements": [
                {
                  "assignments": [
                    330
                  ],
                  "declarations": [
                    {
                      "constant": false,
                      "id": 330,
                      "name": "existingUser",
                      "nodeType": "VariableDeclaration",
                      "scope": 369,
                      "src": "4767:24:0",
                      "stateVariable": false,
                      "storageLocation": "memory",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                        "typeString": "struct IdentityStore.User"
                      },
                      "typeName": {
                        "contractScope": null,
                        "id": 329,
                        "name": "User",
                        "nodeType": "UserDefinedTypeName",
                        "referencedDeclaration": 94,
                        "src": "4767:4:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_struct$_User_$94_storage_ptr",
                          "typeString": "struct IdentityStore.User"
                        }
                      },
                      "value": null,
                      "visibility": "internal"
                    }
                  ],
                  "id": 334,
                  "initialValue": {
                    "argumentTypes": null,
                    "baseExpression": {
                      "argumentTypes": null,
                      "id": 331,
                      "name": "tenantAddressMapping",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 98,
                      "src": "4794:20:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                        "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                      }
                    },
                    "id": 333,
                    "indexExpression": {
                      "argumentTypes": null,
                      "id": 332,
                      "name": "oldUserAddress",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 322,
                      "src": "4815:14:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "isConstant": false,
                    "isLValue": true,
                    "isPure": false,
                    "lValueRequested": false,
                    "nodeType": "IndexAccess",
                    "src": "4794:36:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_struct$_User_$94_storage",
                      "typeString": "struct IdentityStore.User storage ref"
                    }
                  },
                  "nodeType": "VariableDeclarationStatement",
                  "src": "4767:63:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "id": 339,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "nodeType": "UnaryOperation",
                        "operator": "!",
                        "prefix": true,
                        "src": "4857:34:0",
                        "subExpression": {
                          "argumentTypes": null,
                          "arguments": [
                            {
                              "argumentTypes": null,
                              "id": 337,
                              "name": "newUserAddress",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 324,
                              "src": "4876:14:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              }
                            }
                          ],
                          "expression": {
                            "argumentTypes": [
                              {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              }
                            ],
                            "id": 336,
                            "name": "userAddressExists",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 408,
                            "src": "4858:17:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_function_internal_view$_t_address_$returns$_t_bool_$",
                              "typeString": "function (address) view returns (bool)"
                            }
                          },
                          "id": 338,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "kind": "functionCall",
                          "lValueRequested": false,
                          "names": [],
                          "nodeType": "FunctionCall",
                          "src": "4858:33:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                          }
                        },
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      },
                      {
                        "argumentTypes": null,
                        "hexValue": "5468657265277320616c726561647920616e206163636f756e74207469656420746f20746869732061646472657373",
                        "id": 340,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": true,
                        "kind": "string",
                        "lValueRequested": false,
                        "nodeType": "Literal",
                        "src": "4893:49:0",
                        "subdenomination": null,
                        "typeDescriptions": {
                          "typeIdentifier": "t_stringliteral_d9560d649baa3d7d7d6686d1da4373048e51f0d0b91e83baff65cef3893b4f78",
                          "typeString": "literal_string \"There's already an account tied to this address\""
                        },
                        "value": "There's already an account tied to this address"
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        },
                        {
                          "typeIdentifier": "t_stringliteral_d9560d649baa3d7d7d6686d1da4373048e51f0d0b91e83baff65cef3893b4f78",
                          "typeString": "literal_string \"There's already an account tied to this address\""
                        }
                      ],
                      "id": 335,
                      "name": "require",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [
                        532,
                        533
                      ],
                      "referencedDeclaration": 533,
                      "src": "4849:7:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                        "typeString": "function (bool,string memory) pure"
                      }
                    },
                    "id": 341,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "4849:94:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 342,
                  "nodeType": "ExpressionStatement",
                  "src": "4849:94:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "arguments": [
                          {
                            "argumentTypes": null,
                            "id": 345,
                            "name": "oldUserAddress",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 322,
                            "src": "4979:14:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            }
                          }
                        ],
                        "expression": {
                          "argumentTypes": [
                            {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            }
                          ],
                          "id": 344,
                          "name": "userAddressExists",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 408,
                          "src": "4961:17:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_function_internal_view$_t_address_$returns$_t_bool_$",
                            "typeString": "function (address) view returns (bool)"
                          }
                        },
                        "id": 346,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "4961:33:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      },
                      {
                        "argumentTypes": null,
                        "hexValue": "54686572652773206e6f206163636f756e74207469656420746f207468652061646472657373206f726967696e",
                        "id": 347,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": true,
                        "kind": "string",
                        "lValueRequested": false,
                        "nodeType": "Literal",
                        "src": "4996:47:0",
                        "subdenomination": null,
                        "typeDescriptions": {
                          "typeIdentifier": "t_stringliteral_9bce1635c23a28e7d2bc063a3170a795f5e51362f4736a79230f6fc9fa52d788",
                          "typeString": "literal_string \"There's no account tied to the address origin\""
                        },
                        "value": "There's no account tied to the address origin"
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        },
                        {
                          "typeIdentifier": "t_stringliteral_9bce1635c23a28e7d2bc063a3170a795f5e51362f4736a79230f6fc9fa52d788",
                          "typeString": "literal_string \"There's no account tied to the address origin\""
                        }
                      ],
                      "id": 343,
                      "name": "require",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [
                        532,
                        533
                      ],
                      "referencedDeclaration": 533,
                      "src": "4953:7:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                        "typeString": "function (bool,string memory) pure"
                      }
                    },
                    "id": 348,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "4953:91:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 349,
                  "nodeType": "ExpressionStatement",
                  "src": "4953:91:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 355,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftHandSide": {
                      "argumentTypes": null,
                      "baseExpression": {
                        "argumentTypes": null,
                        "id": 350,
                        "name": "tenantHashMapping",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 102,
                        "src": "5055:17:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                          "typeString": "mapping(bytes32 => address)"
                        }
                      },
                      "id": 353,
                      "indexExpression": {
                        "argumentTypes": null,
                        "expression": {
                          "argumentTypes": null,
                          "id": 351,
                          "name": "existingUser",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 330,
                          "src": "5073:12:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                            "typeString": "struct IdentityStore.User memory"
                          }
                        },
                        "id": 352,
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": false,
                        "memberName": "tenantHash",
                        "nodeType": "MemberAccess",
                        "referencedDeclaration": 89,
                        "src": "5073:23:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bytes32",
                          "typeString": "bytes32"
                        }
                      },
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": true,
                      "nodeType": "IndexAccess",
                      "src": "5055:42:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "nodeType": "Assignment",
                    "operator": "=",
                    "rightHandSide": {
                      "argumentTypes": null,
                      "id": 354,
                      "name": "newUserAddress",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 324,
                      "src": "5100:14:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "src": "5055:59:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "id": 356,
                  "nodeType": "ExpressionStatement",
                  "src": "5055:59:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 361,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftHandSide": {
                      "argumentTypes": null,
                      "baseExpression": {
                        "argumentTypes": null,
                        "id": 357,
                        "name": "tenantAddressMapping",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 98,
                        "src": "5124:20:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                          "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                        }
                      },
                      "id": 359,
                      "indexExpression": {
                        "argumentTypes": null,
                        "id": 358,
                        "name": "newUserAddress",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 324,
                        "src": "5145:14:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      },
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": true,
                      "nodeType": "IndexAccess",
                      "src": "5124:36:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_storage",
                        "typeString": "struct IdentityStore.User storage ref"
                      }
                    },
                    "nodeType": "Assignment",
                    "operator": "=",
                    "rightHandSide": {
                      "argumentTypes": null,
                      "id": 360,
                      "name": "existingUser",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 330,
                      "src": "5163:12:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                        "typeString": "struct IdentityStore.User memory"
                      }
                    },
                    "src": "5124:51:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_struct$_User_$94_storage",
                      "typeString": "struct IdentityStore.User storage ref"
                    }
                  },
                  "id": 362,
                  "nodeType": "ExpressionStatement",
                  "src": "5124:51:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 366,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "nodeType": "UnaryOperation",
                    "operator": "delete",
                    "prefix": true,
                    "src": "5185:43:0",
                    "subExpression": {
                      "argumentTypes": null,
                      "baseExpression": {
                        "argumentTypes": null,
                        "id": 363,
                        "name": "tenantAddressMapping",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 98,
                        "src": "5192:20:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                          "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                        }
                      },
                      "id": 365,
                      "indexExpression": {
                        "argumentTypes": null,
                        "id": 364,
                        "name": "oldUserAddress",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 322,
                        "src": "5213:14:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      },
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": true,
                      "nodeType": "IndexAccess",
                      "src": "5192:36:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_storage",
                        "typeString": "struct IdentityStore.User storage ref"
                      }
                    },
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 367,
                  "nodeType": "ExpressionStatement",
                  "src": "5185:43:0"
                }
              ]
            },
            "documentation": null,
            "id": 369,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": false,
            "modifiers": [
              {
                "arguments": null,
                "id": 327,
                "modifierName": {
                  "argumentTypes": null,
                  "id": 326,
                  "name": "onlyOwner",
                  "nodeType": "Identifier",
                  "overloadedDeclarations": [],
                  "referencedDeclaration": 33,
                  "src": "4738:9:0",
                  "typeDescriptions": {
                    "typeIdentifier": "t_modifier$__$",
                    "typeString": "modifier ()"
                  }
                },
                "nodeType": "ModifierInvocation",
                "src": "4738:9:0"
              }
            ],
            "name": "updateAddress",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 325,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 322,
                  "name": "oldUserAddress",
                  "nodeType": "VariableDeclaration",
                  "scope": 369,
                  "src": "4690:22:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 321,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "4690:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 324,
                  "name": "newUserAddress",
                  "nodeType": "VariableDeclaration",
                  "scope": 369,
                  "src": "4714:22:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 323,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "4714:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "4689:48:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 328,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "4757:0:0"
            },
            "scope": 428,
            "src": "4667:568:0",
            "stateMutability": "nonpayable",
            "superFunction": null,
            "visibility": "internal"
          },
          {
            "body": {
              "id": 387,
              "nodeType": "Block",
              "src": "5326:92:0",
              "statements": [
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 385,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftHandSide": {
                      "argumentTypes": null,
                      "expression": {
                        "argumentTypes": null,
                        "baseExpression": {
                          "argumentTypes": null,
                          "id": 378,
                          "name": "tenantAddressMapping",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 98,
                          "src": "5336:20:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                            "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                          }
                        },
                        "id": 382,
                        "indexExpression": {
                          "argumentTypes": null,
                          "baseExpression": {
                            "argumentTypes": null,
                            "id": 379,
                            "name": "tenantHashMapping",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 102,
                            "src": "5357:17:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                              "typeString": "mapping(bytes32 => address)"
                            }
                          },
                          "id": 381,
                          "indexExpression": {
                            "argumentTypes": null,
                            "id": 380,
                            "name": "_tenantHash",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 371,
                            "src": "5375:11:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            }
                          },
                          "isConstant": false,
                          "isLValue": true,
                          "isPure": false,
                          "lValueRequested": false,
                          "nodeType": "IndexAccess",
                          "src": "5357:30:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": false,
                        "nodeType": "IndexAccess",
                        "src": "5336:52:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_struct$_User_$94_storage",
                          "typeString": "struct IdentityStore.User storage ref"
                        }
                      },
                      "id": 383,
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": true,
                      "memberName": "timestamp",
                      "nodeType": "MemberAccess",
                      "referencedDeclaration": 91,
                      "src": "5336:62:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_uint256",
                        "typeString": "uint256"
                      }
                    },
                    "nodeType": "Assignment",
                    "operator": "=",
                    "rightHandSide": {
                      "argumentTypes": null,
                      "id": 384,
                      "name": "_timestamp",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 373,
                      "src": "5401:10:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_uint256",
                        "typeString": "uint256"
                      }
                    },
                    "src": "5336:75:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_uint256",
                      "typeString": "uint256"
                    }
                  },
                  "id": 386,
                  "nodeType": "ExpressionStatement",
                  "src": "5336:75:0"
                }
              ]
            },
            "documentation": null,
            "id": 388,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": false,
            "modifiers": [
              {
                "arguments": null,
                "id": 376,
                "modifierName": {
                  "argumentTypes": null,
                  "id": 375,
                  "name": "onlyOwner",
                  "nodeType": "Identifier",
                  "overloadedDeclarations": [],
                  "referencedDeclaration": 33,
                  "src": "5307:9:0",
                  "typeDescriptions": {
                    "typeIdentifier": "t_modifier$__$",
                    "typeString": "modifier ()"
                  }
                },
                "nodeType": "ModifierInvocation",
                "src": "5307:9:0"
              }
            ],
            "name": "updateTimestamp",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 374,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 371,
                  "name": "_tenantHash",
                  "nodeType": "VariableDeclaration",
                  "scope": 388,
                  "src": "5266:19:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                  },
                  "typeName": {
                    "id": 370,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "5266:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bytes32",
                      "typeString": "bytes32"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 373,
                  "name": "_timestamp",
                  "nodeType": "VariableDeclaration",
                  "scope": 388,
                  "src": "5287:18:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_uint256",
                    "typeString": "uint256"
                  },
                  "typeName": {
                    "id": 372,
                    "name": "uint256",
                    "nodeType": "ElementaryTypeName",
                    "src": "5287:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_uint256",
                      "typeString": "uint256"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "5265:41:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 377,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "5326:0:0"
            },
            "scope": 428,
            "src": "5241:177:0",
            "stateMutability": "nonpayable",
            "superFunction": null,
            "visibility": "internal"
          },
          {
            "body": {
              "id": 407,
              "nodeType": "Block",
              "src": "5500:135:0",
              "statements": [
                {
                  "condition": {
                    "argumentTypes": null,
                    "commonType": {
                      "typeIdentifier": "t_bytes32",
                      "typeString": "bytes32"
                    },
                    "id": 400,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftExpression": {
                      "argumentTypes": null,
                      "expression": {
                        "argumentTypes": null,
                        "baseExpression": {
                          "argumentTypes": null,
                          "id": 395,
                          "name": "tenantAddressMapping",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 98,
                          "src": "5520:20:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                            "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                          }
                        },
                        "id": 397,
                        "indexExpression": {
                          "argumentTypes": null,
                          "id": 396,
                          "name": "userAddress",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 390,
                          "src": "5541:11:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": false,
                        "nodeType": "IndexAccess",
                        "src": "5520:33:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_struct$_User_$94_storage",
                          "typeString": "struct IdentityStore.User storage ref"
                        }
                      },
                      "id": 398,
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": false,
                      "memberName": "tenantHash",
                      "nodeType": "MemberAccess",
                      "referencedDeclaration": 89,
                      "src": "5520:44:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                      }
                    },
                    "nodeType": "BinaryOperation",
                    "operator": "==",
                    "rightExpression": {
                      "argumentTypes": null,
                      "hexValue": "30",
                      "id": 399,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": true,
                      "kind": "number",
                      "lValueRequested": false,
                      "nodeType": "Literal",
                      "src": "5568:1:0",
                      "subdenomination": null,
                      "typeDescriptions": {
                        "typeIdentifier": "t_rational_0_by_1",
                        "typeString": "int_const 0"
                      },
                      "value": "0"
                    },
                    "src": "5520:49:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 404,
                  "nodeType": "IfStatement",
                  "src": "5517:91:0",
                  "trueBody": {
                    "id": 403,
                    "nodeType": "Block",
                    "src": "5571:37:0",
                    "statements": [
                      {
                        "expression": {
                          "argumentTypes": null,
                          "hexValue": "66616c7365",
                          "id": 401,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": true,
                          "kind": "bool",
                          "lValueRequested": false,
                          "nodeType": "Literal",
                          "src": "5592:5:0",
                          "subdenomination": null,
                          "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                          },
                          "value": "false"
                        },
                        "functionReturnParameters": 394,
                        "id": 402,
                        "nodeType": "Return",
                        "src": "5585:12:0"
                      }
                    ]
                  }
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "hexValue": "74727565",
                    "id": 405,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": true,
                    "kind": "bool",
                    "lValueRequested": false,
                    "nodeType": "Literal",
                    "src": "5624:4:0",
                    "subdenomination": null,
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    },
                    "value": "true"
                  },
                  "functionReturnParameters": 394,
                  "id": 406,
                  "nodeType": "Return",
                  "src": "5617:11:0"
                }
              ]
            },
            "documentation": null,
            "id": 408,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": true,
            "modifiers": [],
            "name": "userAddressExists",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 391,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 390,
                  "name": "userAddress",
                  "nodeType": "VariableDeclaration",
                  "scope": 408,
                  "src": "5451:19:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 389,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "5451:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "5450:21:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 394,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 393,
                  "name": "",
                  "nodeType": "VariableDeclaration",
                  "scope": 408,
                  "src": "5494:4:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bool",
                    "typeString": "bool"
                  },
                  "typeName": {
                    "id": 392,
                    "name": "bool",
                    "nodeType": "ElementaryTypeName",
                    "src": "5494:4:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "5493:6:0"
            },
            "scope": 428,
            "src": "5424:211:0",
            "stateMutability": "view",
            "superFunction": null,
            "visibility": "internal"
          },
          {
            "body": {
              "id": 426,
              "nodeType": "Block",
              "src": "5718:163:0",
              "statements": [
                {
                  "condition": {
                    "argumentTypes": null,
                    "commonType": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    },
                    "id": 419,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftExpression": {
                      "argumentTypes": null,
                      "baseExpression": {
                        "argumentTypes": null,
                        "id": 415,
                        "name": "tenantHashMapping",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 102,
                        "src": "5781:17:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                          "typeString": "mapping(bytes32 => address)"
                        }
                      },
                      "id": 417,
                      "indexExpression": {
                        "argumentTypes": null,
                        "id": 416,
                        "name": "tenantHash",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 410,
                        "src": "5799:10:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bytes32",
                          "typeString": "bytes32"
                        }
                      },
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": false,
                      "nodeType": "IndexAccess",
                      "src": "5781:29:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "nodeType": "BinaryOperation",
                    "operator": "==",
                    "rightExpression": {
                      "argumentTypes": null,
                      "hexValue": "30",
                      "id": 418,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": true,
                      "kind": "number",
                      "lValueRequested": false,
                      "nodeType": "Literal",
                      "src": "5814:1:0",
                      "subdenomination": null,
                      "typeDescriptions": {
                        "typeIdentifier": "t_rational_0_by_1",
                        "typeString": "int_const 0"
                      },
                      "value": "0"
                    },
                    "src": "5781:34:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 423,
                  "nodeType": "IfStatement",
                  "src": "5778:76:0",
                  "trueBody": {
                    "id": 422,
                    "nodeType": "Block",
                    "src": "5817:37:0",
                    "statements": [
                      {
                        "expression": {
                          "argumentTypes": null,
                          "hexValue": "66616c7365",
                          "id": 420,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": true,
                          "kind": "bool",
                          "lValueRequested": false,
                          "nodeType": "Literal",
                          "src": "5838:5:0",
                          "subdenomination": null,
                          "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                          },
                          "value": "false"
                        },
                        "functionReturnParameters": 414,
                        "id": 421,
                        "nodeType": "Return",
                        "src": "5831:12:0"
                      }
                    ]
                  }
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "hexValue": "74727565",
                    "id": 424,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": true,
                    "kind": "bool",
                    "lValueRequested": false,
                    "nodeType": "Literal",
                    "src": "5870:4:0",
                    "subdenomination": null,
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    },
                    "value": "true"
                  },
                  "functionReturnParameters": 414,
                  "id": 425,
                  "nodeType": "Return",
                  "src": "5863:11:0"
                }
              ]
            },
            "documentation": null,
            "id": 427,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": true,
            "modifiers": [],
            "name": "userTenantHashExists",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 411,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 410,
                  "name": "tenantHash",
                  "nodeType": "VariableDeclaration",
                  "scope": 427,
                  "src": "5671:18:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                  },
                  "typeName": {
                    "id": 409,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "5671:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bytes32",
                      "typeString": "bytes32"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "5670:20:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 414,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 413,
                  "name": "",
                  "nodeType": "VariableDeclaration",
                  "scope": 427,
                  "src": "5713:4:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bool",
                    "typeString": "bool"
                  },
                  "typeName": {
                    "id": 412,
                    "name": "bool",
                    "nodeType": "ElementaryTypeName",
                    "src": "5713:4:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "5712:6:0"
            },
            "scope": 428,
            "src": "5641:240:0",
            "stateMutability": "view",
            "superFunction": null,
            "visibility": "internal"
          }
        ],
        "scope": 429,
        "src": "1687:4196:0"
      }
    ],
    "src": "0:5883:0"
  },
  "legacyAST": {
    "absolutePath": "/Users/fernandolobato/Desktop/Microsoft-Identities-on-the-Ethereum-Blockchain/identity-smart-contract/contracts/IdentityStore_Sample.sol",
    "exportedSymbols": {
      "IdentityStore": [
        428
      ],
      "Ownable": [
        85
      ]
    },
    "id": 429,
    "nodeType": "SourceUnit",
    "nodes": [
      {
        "id": 1,
        "literals": [
          "solidity",
          "^",
          "0.4",
          ".24"
        ],
        "nodeType": "PragmaDirective",
        "src": "0:24:0"
      },
      {
        "baseContracts": [],
        "contractDependencies": [],
        "contractKind": "contract",
        "documentation": "@title Ownable\n@dev The Ownable contract has an owner address, and provides basic authorization control\nfunctions, this simplifies the implementation of \"user permissions\".",
        "fullyImplemented": true,
        "id": 85,
        "linearizedBaseContracts": [
          85
        ],
        "name": "Ownable",
        "nodeType": "ContractDefinition",
        "nodes": [
          {
            "constant": false,
            "id": 3,
            "name": "owner",
            "nodeType": "VariableDeclaration",
            "scope": 85,
            "src": "238:20:0",
            "stateVariable": true,
            "storageLocation": "default",
            "typeDescriptions": {
              "typeIdentifier": "t_address",
              "typeString": "address"
            },
            "typeName": {
              "id": 2,
              "name": "address",
              "nodeType": "ElementaryTypeName",
              "src": "238:7:0",
              "typeDescriptions": {
                "typeIdentifier": "t_address",
                "typeString": "address"
              }
            },
            "value": null,
            "visibility": "public"
          },
          {
            "anonymous": false,
            "documentation": null,
            "id": 7,
            "name": "OwnershipRenounced",
            "nodeType": "EventDefinition",
            "parameters": {
              "id": 6,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 5,
                  "indexed": true,
                  "name": "previousOwner",
                  "nodeType": "VariableDeclaration",
                  "scope": 7,
                  "src": "289:29:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 4,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "289:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "288:31:0"
            },
            "src": "264:56:0"
          },
          {
            "anonymous": false,
            "documentation": null,
            "id": 13,
            "name": "OwnershipTransferred",
            "nodeType": "EventDefinition",
            "parameters": {
              "id": 12,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 9,
                  "indexed": true,
                  "name": "previousOwner",
                  "nodeType": "VariableDeclaration",
                  "scope": 13,
                  "src": "355:29:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 8,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "355:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 11,
                  "indexed": true,
                  "name": "newOwner",
                  "nodeType": "VariableDeclaration",
                  "scope": 13,
                  "src": "390:24:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 10,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "390:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "349:69:0"
            },
            "src": "323:96:0"
          },
          {
            "body": {
              "id": 21,
              "nodeType": "Block",
              "src": "561:29:0",
              "statements": [
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 19,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftHandSide": {
                      "argumentTypes": null,
                      "id": 16,
                      "name": "owner",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 3,
                      "src": "567:5:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "nodeType": "Assignment",
                    "operator": "=",
                    "rightHandSide": {
                      "argumentTypes": null,
                      "expression": {
                        "argumentTypes": null,
                        "id": 17,
                        "name": "msg",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 529,
                        "src": "575:3:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_magic_message",
                          "typeString": "msg"
                        }
                      },
                      "id": 18,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "lValueRequested": false,
                      "memberName": "sender",
                      "nodeType": "MemberAccess",
                      "referencedDeclaration": null,
                      "src": "575:10:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "src": "567:18:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "id": 20,
                  "nodeType": "ExpressionStatement",
                  "src": "567:18:0"
                }
              ]
            },
            "documentation": "@dev The Ownable constructor sets the original `owner` of the contract to the sender\naccount.",
            "id": 22,
            "implemented": true,
            "isConstructor": true,
            "isDeclaredConst": false,
            "modifiers": [],
            "name": "",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 14,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "551:2:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 15,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "561:0:0"
            },
            "scope": 85,
            "src": "540:50:0",
            "stateMutability": "nonpayable",
            "superFunction": null,
            "visibility": "public"
          },
          {
            "body": {
              "id": 32,
              "nodeType": "Block",
              "src": "691:46:0",
              "statements": [
                {
                  "expression": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "commonType": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        },
                        "id": 28,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftExpression": {
                          "argumentTypes": null,
                          "expression": {
                            "argumentTypes": null,
                            "id": 25,
                            "name": "msg",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 529,
                            "src": "705:3:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_magic_message",
                              "typeString": "msg"
                            }
                          },
                          "id": 26,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "lValueRequested": false,
                          "memberName": "sender",
                          "nodeType": "MemberAccess",
                          "referencedDeclaration": null,
                          "src": "705:10:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        },
                        "nodeType": "BinaryOperation",
                        "operator": "==",
                        "rightExpression": {
                          "argumentTypes": null,
                          "id": 27,
                          "name": "owner",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 3,
                          "src": "719:5:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        },
                        "src": "705:19:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      ],
                      "id": 24,
                      "name": "require",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [
                        532,
                        533
                      ],
                      "referencedDeclaration": 532,
                      "src": "697:7:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_require_pure$_t_bool_$returns$__$",
                        "typeString": "function (bool) pure"
                      }
                    },
                    "id": 29,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "697:28:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 30,
                  "nodeType": "ExpressionStatement",
                  "src": "697:28:0"
                },
                {
                  "id": 31,
                  "nodeType": "PlaceholderStatement",
                  "src": "731:1:0"
                }
              ]
            },
            "documentation": "@dev Throws if called by any account other than the owner.",
            "id": 33,
            "name": "onlyOwner",
            "nodeType": "ModifierDefinition",
            "parameters": {
              "id": 23,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "688:2:0"
            },
            "src": "670:67:0",
            "visibility": "internal"
          },
          {
            "body": {
              "id": 48,
              "nodeType": "Block",
              "src": "1047:65:0",
              "statements": [
                {
                  "eventCall": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "id": 39,
                        "name": "owner",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 3,
                        "src": "1077:5:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      ],
                      "id": 38,
                      "name": "OwnershipRenounced",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 7,
                      "src": "1058:18:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_event_nonpayable$_t_address_$returns$__$",
                        "typeString": "function (address)"
                      }
                    },
                    "id": 40,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "1058:25:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 41,
                  "nodeType": "EmitStatement",
                  "src": "1053:30:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 46,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftHandSide": {
                      "argumentTypes": null,
                      "id": 42,
                      "name": "owner",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 3,
                      "src": "1089:5:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "nodeType": "Assignment",
                    "operator": "=",
                    "rightHandSide": {
                      "argumentTypes": null,
                      "arguments": [
                        {
                          "argumentTypes": null,
                          "hexValue": "30",
                          "id": 44,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": true,
                          "kind": "number",
                          "lValueRequested": false,
                          "nodeType": "Literal",
                          "src": "1105:1:0",
                          "subdenomination": null,
                          "typeDescriptions": {
                            "typeIdentifier": "t_rational_0_by_1",
                            "typeString": "int_const 0"
                          },
                          "value": "0"
                        }
                      ],
                      "expression": {
                        "argumentTypes": [
                          {
                            "typeIdentifier": "t_rational_0_by_1",
                            "typeString": "int_const 0"
                          }
                        ],
                        "id": 43,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": true,
                        "lValueRequested": false,
                        "nodeType": "ElementaryTypeNameExpression",
                        "src": "1097:7:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_type$_t_address_$",
                          "typeString": "type(address)"
                        },
                        "typeName": "address"
                      },
                      "id": 45,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": true,
                      "kind": "typeConversion",
                      "lValueRequested": false,
                      "names": [],
                      "nodeType": "FunctionCall",
                      "src": "1097:10:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "src": "1089:18:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "id": 47,
                  "nodeType": "ExpressionStatement",
                  "src": "1089:18:0"
                }
              ]
            },
            "documentation": "@dev Allows the current owner to relinquish control of the contract.\n@notice Renouncing to ownership will leave the contract without an owner.\nIt will not be possible to call the functions with the `onlyOwner`\nmodifier anymore.",
            "id": 49,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": false,
            "modifiers": [
              {
                "arguments": null,
                "id": 36,
                "modifierName": {
                  "argumentTypes": null,
                  "id": 35,
                  "name": "onlyOwner",
                  "nodeType": "Identifier",
                  "overloadedDeclarations": [],
                  "referencedDeclaration": 33,
                  "src": "1037:9:0",
                  "typeDescriptions": {
                    "typeIdentifier": "t_modifier$__$",
                    "typeString": "modifier ()"
                  }
                },
                "nodeType": "ModifierInvocation",
                "src": "1037:9:0"
              }
            ],
            "name": "renounceOwnership",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 34,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "1027:2:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 37,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "1047:0:0"
            },
            "scope": 85,
            "src": "1001:111:0",
            "stateMutability": "nonpayable",
            "superFunction": null,
            "visibility": "public"
          },
          {
            "body": {
              "id": 60,
              "nodeType": "Block",
              "src": "1337:40:0",
              "statements": [
                {
                  "expression": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "id": 57,
                        "name": "_newOwner",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 51,
                        "src": "1362:9:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      ],
                      "id": 56,
                      "name": "_transferOwnership",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 84,
                      "src": "1343:18:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_internal_nonpayable$_t_address_$returns$__$",
                        "typeString": "function (address)"
                      }
                    },
                    "id": 58,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "1343:29:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 59,
                  "nodeType": "ExpressionStatement",
                  "src": "1343:29:0"
                }
              ]
            },
            "documentation": "@dev Allows the current owner to transfer control of the contract to a newOwner.\n@param _newOwner The address to transfer ownership to.",
            "id": 61,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": false,
            "modifiers": [
              {
                "arguments": null,
                "id": 54,
                "modifierName": {
                  "argumentTypes": null,
                  "id": 53,
                  "name": "onlyOwner",
                  "nodeType": "Identifier",
                  "overloadedDeclarations": [],
                  "referencedDeclaration": 33,
                  "src": "1327:9:0",
                  "typeDescriptions": {
                    "typeIdentifier": "t_modifier$__$",
                    "typeString": "modifier ()"
                  }
                },
                "nodeType": "ModifierInvocation",
                "src": "1327:9:0"
              }
            ],
            "name": "transferOwnership",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 52,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 51,
                  "name": "_newOwner",
                  "nodeType": "VariableDeclaration",
                  "scope": 61,
                  "src": "1301:17:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 50,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "1301:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "1300:19:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 55,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "1337:0:0"
            },
            "scope": 85,
            "src": "1274:103:0",
            "stateMutability": "nonpayable",
            "superFunction": null,
            "visibility": "public"
          },
          {
            "body": {
              "id": 83,
              "nodeType": "Block",
              "src": "1568:115:0",
              "statements": [
                {
                  "expression": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "commonType": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        },
                        "id": 71,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "leftExpression": {
                          "argumentTypes": null,
                          "id": 67,
                          "name": "_newOwner",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 63,
                          "src": "1582:9:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        },
                        "nodeType": "BinaryOperation",
                        "operator": "!=",
                        "rightExpression": {
                          "argumentTypes": null,
                          "arguments": [
                            {
                              "argumentTypes": null,
                              "hexValue": "30",
                              "id": 69,
                              "isConstant": false,
                              "isLValue": false,
                              "isPure": true,
                              "kind": "number",
                              "lValueRequested": false,
                              "nodeType": "Literal",
                              "src": "1603:1:0",
                              "subdenomination": null,
                              "typeDescriptions": {
                                "typeIdentifier": "t_rational_0_by_1",
                                "typeString": "int_const 0"
                              },
                              "value": "0"
                            }
                          ],
                          "expression": {
                            "argumentTypes": [
                              {
                                "typeIdentifier": "t_rational_0_by_1",
                                "typeString": "int_const 0"
                              }
                            ],
                            "id": 68,
                            "isConstant": false,
                            "isLValue": false,
                            "isPure": true,
                            "lValueRequested": false,
                            "nodeType": "ElementaryTypeNameExpression",
                            "src": "1595:7:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_type$_t_address_$",
                              "typeString": "type(address)"
                            },
                            "typeName": "address"
                          },
                          "id": 70,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": true,
                          "kind": "typeConversion",
                          "lValueRequested": false,
                          "names": [],
                          "nodeType": "FunctionCall",
                          "src": "1595:10:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        },
                        "src": "1582:23:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      ],
                      "id": 66,
                      "name": "require",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [
                        532,
                        533
                      ],
                      "referencedDeclaration": 532,
                      "src": "1574:7:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_require_pure$_t_bool_$returns$__$",
                        "typeString": "function (bool) pure"
                      }
                    },
                    "id": 72,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "1574:32:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 73,
                  "nodeType": "ExpressionStatement",
                  "src": "1574:32:0"
                },
                {
                  "eventCall": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "id": 75,
                        "name": "owner",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 3,
                        "src": "1638:5:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      },
                      {
                        "argumentTypes": null,
                        "id": 76,
                        "name": "_newOwner",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 63,
                        "src": "1645:9:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        },
                        {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      ],
                      "id": 74,
                      "name": "OwnershipTransferred",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 13,
                      "src": "1617:20:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_event_nonpayable$_t_address_$_t_address_$returns$__$",
                        "typeString": "function (address,address)"
                      }
                    },
                    "id": 77,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "1617:38:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 78,
                  "nodeType": "EmitStatement",
                  "src": "1612:43:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 81,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftHandSide": {
                      "argumentTypes": null,
                      "id": 79,
                      "name": "owner",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 3,
                      "src": "1661:5:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "nodeType": "Assignment",
                    "operator": "=",
                    "rightHandSide": {
                      "argumentTypes": null,
                      "id": 80,
                      "name": "_newOwner",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 63,
                      "src": "1669:9:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "src": "1661:17:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "id": 82,
                  "nodeType": "ExpressionStatement",
                  "src": "1661:17:0"
                }
              ]
            },
            "documentation": "@dev Transfers control of the contract to a newOwner.\n@param _newOwner The address to transfer ownership to.",
            "id": 84,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": false,
            "modifiers": [],
            "name": "_transferOwnership",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 64,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 63,
                  "name": "_newOwner",
                  "nodeType": "VariableDeclaration",
                  "scope": 84,
                  "src": "1540:17:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 62,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "1540:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "1539:19:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 65,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "1568:0:0"
            },
            "scope": 85,
            "src": "1512:171:0",
            "stateMutability": "nonpayable",
            "superFunction": null,
            "visibility": "internal"
          }
        ],
        "scope": 429,
        "src": "217:1468:0"
      },
      {
        "baseContracts": [
          {
            "arguments": null,
            "baseName": {
              "contractScope": null,
              "id": 86,
              "name": "Ownable",
              "nodeType": "UserDefinedTypeName",
              "referencedDeclaration": 85,
              "src": "1713:7:0",
              "typeDescriptions": {
                "typeIdentifier": "t_contract$_Ownable_$85",
                "typeString": "contract Ownable"
              }
            },
            "id": 87,
            "nodeType": "InheritanceSpecifier",
            "src": "1713:7:0"
          }
        ],
        "contractDependencies": [
          85
        ],
        "contractKind": "contract",
        "documentation": null,
        "fullyImplemented": true,
        "id": 428,
        "linearizedBaseContracts": [
          428,
          85
        ],
        "name": "IdentityStore",
        "nodeType": "ContractDefinition",
        "nodes": [
          {
            "canonicalName": "IdentityStore.User",
            "id": 94,
            "members": [
              {
                "constant": false,
                "id": 89,
                "name": "tenantHash",
                "nodeType": "VariableDeclaration",
                "scope": 94,
                "src": "1752:18:0",
                "stateVariable": false,
                "storageLocation": "default",
                "typeDescriptions": {
                  "typeIdentifier": "t_bytes32",
                  "typeString": "bytes32"
                },
                "typeName": {
                  "id": 88,
                  "name": "bytes32",
                  "nodeType": "ElementaryTypeName",
                  "src": "1752:7:0",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                  }
                },
                "value": null,
                "visibility": "internal"
              },
              {
                "constant": false,
                "id": 91,
                "name": "timestamp",
                "nodeType": "VariableDeclaration",
                "scope": 94,
                "src": "1780:17:0",
                "stateVariable": false,
                "storageLocation": "default",
                "typeDescriptions": {
                  "typeIdentifier": "t_uint256",
                  "typeString": "uint256"
                },
                "typeName": {
                  "id": 90,
                  "name": "uint256",
                  "nodeType": "ElementaryTypeName",
                  "src": "1780:7:0",
                  "typeDescriptions": {
                    "typeIdentifier": "t_uint256",
                    "typeString": "uint256"
                  }
                },
                "value": null,
                "visibility": "internal"
              },
              {
                "constant": false,
                "id": 93,
                "name": "tenantId",
                "nodeType": "VariableDeclaration",
                "scope": 94,
                "src": "1807:15:0",
                "stateVariable": false,
                "storageLocation": "default",
                "typeDescriptions": {
                  "typeIdentifier": "t_string_storage_ptr",
                  "typeString": "string"
                },
                "typeName": {
                  "id": 92,
                  "name": "string",
                  "nodeType": "ElementaryTypeName",
                  "src": "1807:6:0",
                  "typeDescriptions": {
                    "typeIdentifier": "t_string_storage_ptr",
                    "typeString": "string"
                  }
                },
                "value": null,
                "visibility": "internal"
              }
            ],
            "name": "User",
            "nodeType": "StructDefinition",
            "scope": 428,
            "src": "1730:99:0",
            "visibility": "public"
          },
          {
            "constant": false,
            "id": 98,
            "name": "tenantAddressMapping",
            "nodeType": "VariableDeclaration",
            "scope": 428,
            "src": "1835:53:0",
            "stateVariable": true,
            "storageLocation": "default",
            "typeDescriptions": {
              "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
              "typeString": "mapping(address => struct IdentityStore.User)"
            },
            "typeName": {
              "id": 97,
              "keyType": {
                "id": 95,
                "name": "address",
                "nodeType": "ElementaryTypeName",
                "src": "1843:7:0",
                "typeDescriptions": {
                  "typeIdentifier": "t_address",
                  "typeString": "address"
                }
              },
              "nodeType": "Mapping",
              "src": "1835:24:0",
              "typeDescriptions": {
                "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                "typeString": "mapping(address => struct IdentityStore.User)"
              },
              "valueType": {
                "contractScope": null,
                "id": 96,
                "name": "User",
                "nodeType": "UserDefinedTypeName",
                "referencedDeclaration": 94,
                "src": "1854:4:0",
                "typeDescriptions": {
                  "typeIdentifier": "t_struct$_User_$94_storage_ptr",
                  "typeString": "struct IdentityStore.User"
                }
              }
            },
            "value": null,
            "visibility": "private"
          },
          {
            "constant": false,
            "id": 102,
            "name": "tenantHashMapping",
            "nodeType": "VariableDeclaration",
            "scope": 428,
            "src": "1894:53:0",
            "stateVariable": true,
            "storageLocation": "default",
            "typeDescriptions": {
              "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
              "typeString": "mapping(bytes32 => address)"
            },
            "typeName": {
              "id": 101,
              "keyType": {
                "id": 99,
                "name": "bytes32",
                "nodeType": "ElementaryTypeName",
                "src": "1902:7:0",
                "typeDescriptions": {
                  "typeIdentifier": "t_bytes32",
                  "typeString": "bytes32"
                }
              },
              "nodeType": "Mapping",
              "src": "1894:27:0",
              "typeDescriptions": {
                "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                "typeString": "mapping(bytes32 => address)"
              },
              "valueType": {
                "id": 100,
                "name": "address",
                "nodeType": "ElementaryTypeName",
                "src": "1913:7:0",
                "typeDescriptions": {
                  "typeIdentifier": "t_address",
                  "typeString": "address"
                }
              }
            },
            "value": null,
            "visibility": "private"
          },
          {
            "body": {
              "id": 208,
              "nodeType": "Block",
              "src": "2105:1133:0",
              "statements": [
                {
                  "condition": {
                    "argumentTypes": null,
                    "commonType": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    },
                    "id": 123,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftExpression": {
                      "argumentTypes": null,
                      "id": 118,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "lValueRequested": false,
                      "nodeType": "UnaryOperation",
                      "operator": "!",
                      "prefix": true,
                      "src": "2151:32:0",
                      "subExpression": {
                        "argumentTypes": null,
                        "arguments": [
                          {
                            "argumentTypes": null,
                            "id": 116,
                            "name": "_userAddress",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 106,
                            "src": "2170:12:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            }
                          }
                        ],
                        "expression": {
                          "argumentTypes": [
                            {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            }
                          ],
                          "id": 115,
                          "name": "userAddressExists",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 408,
                          "src": "2152:17:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_function_internal_view$_t_address_$returns$_t_bool_$",
                            "typeString": "function (address) view returns (bool)"
                          }
                        },
                        "id": 117,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "2152:31:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      },
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "nodeType": "BinaryOperation",
                    "operator": "&&",
                    "rightExpression": {
                      "argumentTypes": null,
                      "id": 122,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "lValueRequested": false,
                      "nodeType": "UnaryOperation",
                      "operator": "!",
                      "prefix": true,
                      "src": "2187:34:0",
                      "subExpression": {
                        "argumentTypes": null,
                        "arguments": [
                          {
                            "argumentTypes": null,
                            "id": 120,
                            "name": "_tenantHash",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 104,
                            "src": "2209:11:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            }
                          }
                        ],
                        "expression": {
                          "argumentTypes": [
                            {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            }
                          ],
                          "id": 119,
                          "name": "userTenantHashExists",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 427,
                          "src": "2188:20:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_function_internal_view$_t_bytes32_$returns$_t_bool_$",
                            "typeString": "function (bytes32) view returns (bool)"
                          }
                        },
                        "id": 121,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "2188:33:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      },
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "src": "2151:70:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 146,
                  "nodeType": "IfStatement",
                  "src": "2147:313:0",
                  "trueBody": {
                    "id": 145,
                    "nodeType": "Block",
                    "src": "2223:237:0",
                    "statements": [
                      {
                        "assignments": [
                          125
                        ],
                        "declarations": [
                          {
                            "constant": false,
                            "id": 125,
                            "name": "newUser",
                            "nodeType": "VariableDeclaration",
                            "scope": 209,
                            "src": "2250:19:0",
                            "stateVariable": false,
                            "storageLocation": "memory",
                            "typeDescriptions": {
                              "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                              "typeString": "struct IdentityStore.User"
                            },
                            "typeName": {
                              "contractScope": null,
                              "id": 124,
                              "name": "User",
                              "nodeType": "UserDefinedTypeName",
                              "referencedDeclaration": 94,
                              "src": "2250:4:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_struct$_User_$94_storage_ptr",
                                "typeString": "struct IdentityStore.User"
                              }
                            },
                            "value": null,
                            "visibility": "internal"
                          }
                        ],
                        "id": 131,
                        "initialValue": {
                          "argumentTypes": null,
                          "arguments": [
                            {
                              "argumentTypes": null,
                              "id": 127,
                              "name": "_tenantHash",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 104,
                              "src": "2277:11:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              }
                            },
                            {
                              "argumentTypes": null,
                              "id": 128,
                              "name": "_timestamp",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 108,
                              "src": "2290:10:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_uint256",
                                "typeString": "uint256"
                              }
                            },
                            {
                              "argumentTypes": null,
                              "id": 129,
                              "name": "_tenantId",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 110,
                              "src": "2302:9:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_string_memory_ptr",
                                "typeString": "string memory"
                              }
                            }
                          ],
                          "expression": {
                            "argumentTypes": [
                              {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              },
                              {
                                "typeIdentifier": "t_uint256",
                                "typeString": "uint256"
                              },
                              {
                                "typeIdentifier": "t_string_memory_ptr",
                                "typeString": "string memory"
                              }
                            ],
                            "id": 126,
                            "name": "User",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 94,
                            "src": "2272:4:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_type$_t_struct$_User_$94_storage_ptr_$",
                              "typeString": "type(struct IdentityStore.User storage pointer)"
                            }
                          },
                          "id": 130,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "kind": "structConstructorCall",
                          "lValueRequested": false,
                          "names": [],
                          "nodeType": "FunctionCall",
                          "src": "2272:40:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_struct$_User_$94_memory",
                            "typeString": "struct IdentityStore.User memory"
                          }
                        },
                        "nodeType": "VariableDeclarationStatement",
                        "src": "2250:62:0"
                      },
                      {
                        "expression": {
                          "argumentTypes": null,
                          "id": 136,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "lValueRequested": false,
                          "leftHandSide": {
                            "argumentTypes": null,
                            "baseExpression": {
                              "argumentTypes": null,
                              "id": 132,
                              "name": "tenantAddressMapping",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 98,
                              "src": "2326:20:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                                "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                              }
                            },
                            "id": 134,
                            "indexExpression": {
                              "argumentTypes": null,
                              "id": 133,
                              "name": "_userAddress",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 106,
                              "src": "2347:12:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              }
                            },
                            "isConstant": false,
                            "isLValue": true,
                            "isPure": false,
                            "lValueRequested": true,
                            "nodeType": "IndexAccess",
                            "src": "2326:34:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_struct$_User_$94_storage",
                              "typeString": "struct IdentityStore.User storage ref"
                            }
                          },
                          "nodeType": "Assignment",
                          "operator": "=",
                          "rightHandSide": {
                            "argumentTypes": null,
                            "id": 135,
                            "name": "newUser",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 125,
                            "src": "2363:7:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                              "typeString": "struct IdentityStore.User memory"
                            }
                          },
                          "src": "2326:44:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_struct$_User_$94_storage",
                            "typeString": "struct IdentityStore.User storage ref"
                          }
                        },
                        "id": 137,
                        "nodeType": "ExpressionStatement",
                        "src": "2326:44:0"
                      },
                      {
                        "expression": {
                          "argumentTypes": null,
                          "id": 142,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "lValueRequested": false,
                          "leftHandSide": {
                            "argumentTypes": null,
                            "baseExpression": {
                              "argumentTypes": null,
                              "id": 138,
                              "name": "tenantHashMapping",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 102,
                              "src": "2384:17:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                                "typeString": "mapping(bytes32 => address)"
                              }
                            },
                            "id": 140,
                            "indexExpression": {
                              "argumentTypes": null,
                              "id": 139,
                              "name": "_tenantHash",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 104,
                              "src": "2402:11:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              }
                            },
                            "isConstant": false,
                            "isLValue": true,
                            "isPure": false,
                            "lValueRequested": true,
                            "nodeType": "IndexAccess",
                            "src": "2384:30:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            }
                          },
                          "nodeType": "Assignment",
                          "operator": "=",
                          "rightHandSide": {
                            "argumentTypes": null,
                            "id": 141,
                            "name": "_userAddress",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 106,
                            "src": "2417:12:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            }
                          },
                          "src": "2384:45:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        },
                        "id": 143,
                        "nodeType": "ExpressionStatement",
                        "src": "2384:45:0"
                      },
                      {
                        "expression": null,
                        "functionReturnParameters": 114,
                        "id": 144,
                        "nodeType": "Return",
                        "src": "2443:7:0"
                      }
                    ]
                  }
                },
                {
                  "condition": {
                    "argumentTypes": null,
                    "commonType": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    },
                    "id": 154,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftExpression": {
                      "argumentTypes": null,
                      "arguments": [
                        {
                          "argumentTypes": null,
                          "id": 148,
                          "name": "_userAddress",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 106,
                          "src": "2521:12:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        }
                      ],
                      "expression": {
                        "argumentTypes": [
                          {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        ],
                        "id": 147,
                        "name": "userAddressExists",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 408,
                        "src": "2503:17:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_function_internal_view$_t_address_$returns$_t_bool_$",
                          "typeString": "function (address) view returns (bool)"
                        }
                      },
                      "id": 149,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "kind": "functionCall",
                      "lValueRequested": false,
                      "names": [],
                      "nodeType": "FunctionCall",
                      "src": "2503:31:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "nodeType": "BinaryOperation",
                    "operator": "&&",
                    "rightExpression": {
                      "argumentTypes": null,
                      "id": 153,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "lValueRequested": false,
                      "nodeType": "UnaryOperation",
                      "operator": "!",
                      "prefix": true,
                      "src": "2538:34:0",
                      "subExpression": {
                        "argumentTypes": null,
                        "arguments": [
                          {
                            "argumentTypes": null,
                            "id": 151,
                            "name": "_tenantHash",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 104,
                            "src": "2560:11:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            }
                          }
                        ],
                        "expression": {
                          "argumentTypes": [
                            {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            }
                          ],
                          "id": 150,
                          "name": "userTenantHashExists",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 427,
                          "src": "2539:20:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_function_internal_view$_t_bytes32_$returns$_t_bool_$",
                            "typeString": "function (bytes32) view returns (bool)"
                          }
                        },
                        "id": 152,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "2539:33:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      },
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "src": "2503:69:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 170,
                  "nodeType": "IfStatement",
                  "src": "2499:254:0",
                  "trueBody": {
                    "id": 169,
                    "nodeType": "Block",
                    "src": "2574:179:0",
                    "statements": [
                      {
                        "assignments": [
                          156
                        ],
                        "declarations": [
                          {
                            "constant": false,
                            "id": 156,
                            "name": "oldHash",
                            "nodeType": "VariableDeclaration",
                            "scope": 209,
                            "src": "2601:15:0",
                            "stateVariable": false,
                            "storageLocation": "default",
                            "typeDescriptions": {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            },
                            "typeName": {
                              "id": 155,
                              "name": "bytes32",
                              "nodeType": "ElementaryTypeName",
                              "src": "2601:7:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              }
                            },
                            "value": null,
                            "visibility": "internal"
                          }
                        ],
                        "id": 161,
                        "initialValue": {
                          "argumentTypes": null,
                          "expression": {
                            "argumentTypes": null,
                            "baseExpression": {
                              "argumentTypes": null,
                              "id": 157,
                              "name": "tenantAddressMapping",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 98,
                              "src": "2619:20:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                                "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                              }
                            },
                            "id": 159,
                            "indexExpression": {
                              "argumentTypes": null,
                              "id": 158,
                              "name": "_userAddress",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 106,
                              "src": "2640:12:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              }
                            },
                            "isConstant": false,
                            "isLValue": true,
                            "isPure": false,
                            "lValueRequested": false,
                            "nodeType": "IndexAccess",
                            "src": "2619:34:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_struct$_User_$94_storage",
                              "typeString": "struct IdentityStore.User storage ref"
                            }
                          },
                          "id": 160,
                          "isConstant": false,
                          "isLValue": true,
                          "isPure": false,
                          "lValueRequested": false,
                          "memberName": "tenantHash",
                          "nodeType": "MemberAccess",
                          "referencedDeclaration": 89,
                          "src": "2619:45:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                          }
                        },
                        "nodeType": "VariableDeclarationStatement",
                        "src": "2601:63:0"
                      },
                      {
                        "expression": {
                          "argumentTypes": null,
                          "arguments": [
                            {
                              "argumentTypes": null,
                              "id": 163,
                              "name": "oldHash",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 156,
                              "src": "2689:7:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              }
                            },
                            {
                              "argumentTypes": null,
                              "id": 164,
                              "name": "_tenantHash",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 104,
                              "src": "2698:11:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              }
                            },
                            {
                              "argumentTypes": null,
                              "id": 165,
                              "name": "_timestamp",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 108,
                              "src": "2711:10:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_uint256",
                                "typeString": "uint256"
                              }
                            }
                          ],
                          "expression": {
                            "argumentTypes": [
                              {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              },
                              {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              },
                              {
                                "typeIdentifier": "t_uint256",
                                "typeString": "uint256"
                              }
                            ],
                            "id": 162,
                            "name": "updateHash",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 320,
                            "src": "2678:10:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_function_internal_nonpayable$_t_bytes32_$_t_bytes32_$_t_uint256_$returns$__$",
                              "typeString": "function (bytes32,bytes32,uint256)"
                            }
                          },
                          "id": 166,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "kind": "functionCall",
                          "lValueRequested": false,
                          "names": [],
                          "nodeType": "FunctionCall",
                          "src": "2678:44:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_tuple$__$",
                            "typeString": "tuple()"
                          }
                        },
                        "id": 167,
                        "nodeType": "ExpressionStatement",
                        "src": "2678:44:0"
                      },
                      {
                        "expression": null,
                        "functionReturnParameters": 114,
                        "id": 168,
                        "nodeType": "Return",
                        "src": "2736:7:0"
                      }
                    ]
                  }
                },
                {
                  "condition": {
                    "argumentTypes": null,
                    "commonType": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    },
                    "id": 178,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftExpression": {
                      "argumentTypes": null,
                      "arguments": [
                        {
                          "argumentTypes": null,
                          "id": 172,
                          "name": "_tenantHash",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 104,
                          "src": "2828:11:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                          }
                        }
                      ],
                      "expression": {
                        "argumentTypes": [
                          {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                          }
                        ],
                        "id": 171,
                        "name": "userTenantHashExists",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 427,
                        "src": "2807:20:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_function_internal_view$_t_bytes32_$returns$_t_bool_$",
                          "typeString": "function (bytes32) view returns (bool)"
                        }
                      },
                      "id": 173,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "kind": "functionCall",
                      "lValueRequested": false,
                      "names": [],
                      "nodeType": "FunctionCall",
                      "src": "2807:33:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "nodeType": "BinaryOperation",
                    "operator": "&&",
                    "rightExpression": {
                      "argumentTypes": null,
                      "id": 177,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "lValueRequested": false,
                      "nodeType": "UnaryOperation",
                      "operator": "!",
                      "prefix": true,
                      "src": "2844:32:0",
                      "subExpression": {
                        "argumentTypes": null,
                        "arguments": [
                          {
                            "argumentTypes": null,
                            "id": 175,
                            "name": "_userAddress",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 106,
                            "src": "2863:12:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            }
                          }
                        ],
                        "expression": {
                          "argumentTypes": [
                            {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            }
                          ],
                          "id": 174,
                          "name": "userAddressExists",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 408,
                          "src": "2845:17:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_function_internal_view$_t_address_$returns$_t_bool_$",
                            "typeString": "function (address) view returns (bool)"
                          }
                        },
                        "id": 176,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "2845:31:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      },
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "src": "2807:69:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 192,
                  "nodeType": "IfStatement",
                  "src": "2803:224:0",
                  "trueBody": {
                    "id": 191,
                    "nodeType": "Block",
                    "src": "2878:149:0",
                    "statements": [
                      {
                        "assignments": [
                          180
                        ],
                        "declarations": [
                          {
                            "constant": false,
                            "id": 180,
                            "name": "oldAddress",
                            "nodeType": "VariableDeclaration",
                            "scope": 209,
                            "src": "2892:18:0",
                            "stateVariable": false,
                            "storageLocation": "default",
                            "typeDescriptions": {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            },
                            "typeName": {
                              "id": 179,
                              "name": "address",
                              "nodeType": "ElementaryTypeName",
                              "src": "2892:7:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              }
                            },
                            "value": null,
                            "visibility": "internal"
                          }
                        ],
                        "id": 184,
                        "initialValue": {
                          "argumentTypes": null,
                          "baseExpression": {
                            "argumentTypes": null,
                            "id": 181,
                            "name": "tenantHashMapping",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 102,
                            "src": "2913:17:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                              "typeString": "mapping(bytes32 => address)"
                            }
                          },
                          "id": 183,
                          "indexExpression": {
                            "argumentTypes": null,
                            "id": 182,
                            "name": "_tenantHash",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 104,
                            "src": "2931:11:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            }
                          },
                          "isConstant": false,
                          "isLValue": true,
                          "isPure": false,
                          "lValueRequested": false,
                          "nodeType": "IndexAccess",
                          "src": "2913:30:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        },
                        "nodeType": "VariableDeclarationStatement",
                        "src": "2892:51:0"
                      },
                      {
                        "expression": {
                          "argumentTypes": null,
                          "arguments": [
                            {
                              "argumentTypes": null,
                              "id": 186,
                              "name": "oldAddress",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 180,
                              "src": "2971:10:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              }
                            },
                            {
                              "argumentTypes": null,
                              "id": 187,
                              "name": "_userAddress",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 106,
                              "src": "2983:12:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              }
                            }
                          ],
                          "expression": {
                            "argumentTypes": [
                              {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              },
                              {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              }
                            ],
                            "id": 185,
                            "name": "updateAddress",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 369,
                            "src": "2957:13:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_function_internal_nonpayable$_t_address_$_t_address_$returns$__$",
                              "typeString": "function (address,address)"
                            }
                          },
                          "id": 188,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "kind": "functionCall",
                          "lValueRequested": false,
                          "names": [],
                          "nodeType": "FunctionCall",
                          "src": "2957:39:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_tuple$__$",
                            "typeString": "tuple()"
                          }
                        },
                        "id": 189,
                        "nodeType": "ExpressionStatement",
                        "src": "2957:39:0"
                      },
                      {
                        "expression": null,
                        "functionReturnParameters": 114,
                        "id": 190,
                        "nodeType": "Return",
                        "src": "3010:7:0"
                      }
                    ]
                  }
                },
                {
                  "condition": {
                    "argumentTypes": null,
                    "commonType": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    },
                    "id": 199,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftExpression": {
                      "argumentTypes": null,
                      "arguments": [
                        {
                          "argumentTypes": null,
                          "id": 194,
                          "name": "_tenantHash",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 104,
                          "src": "3098:11:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                          }
                        }
                      ],
                      "expression": {
                        "argumentTypes": [
                          {
                            "typeIdentifier": "t_bytes32",
                            "typeString": "bytes32"
                          }
                        ],
                        "id": 193,
                        "name": "userTenantHashExists",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 427,
                        "src": "3077:20:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_function_internal_view$_t_bytes32_$returns$_t_bool_$",
                          "typeString": "function (bytes32) view returns (bool)"
                        }
                      },
                      "id": 195,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "kind": "functionCall",
                      "lValueRequested": false,
                      "names": [],
                      "nodeType": "FunctionCall",
                      "src": "3077:33:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "nodeType": "BinaryOperation",
                    "operator": "&&",
                    "rightExpression": {
                      "argumentTypes": null,
                      "arguments": [
                        {
                          "argumentTypes": null,
                          "id": 197,
                          "name": "_userAddress",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 106,
                          "src": "3132:12:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        }
                      ],
                      "expression": {
                        "argumentTypes": [
                          {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        ],
                        "id": 196,
                        "name": "userAddressExists",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 408,
                        "src": "3114:17:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_function_internal_view$_t_address_$returns$_t_bool_$",
                          "typeString": "function (address) view returns (bool)"
                        }
                      },
                      "id": 198,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "kind": "functionCall",
                      "lValueRequested": false,
                      "names": [],
                      "nodeType": "FunctionCall",
                      "src": "3114:31:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "src": "3077:68:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 207,
                  "nodeType": "IfStatement",
                  "src": "3073:159:0",
                  "trueBody": {
                    "id": 206,
                    "nodeType": "Block",
                    "src": "3147:85:0",
                    "statements": [
                      {
                        "expression": {
                          "argumentTypes": null,
                          "arguments": [
                            {
                              "argumentTypes": null,
                              "id": 201,
                              "name": "_tenantHash",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 104,
                              "src": "3177:11:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              }
                            },
                            {
                              "argumentTypes": null,
                              "id": 202,
                              "name": "_timestamp",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 108,
                              "src": "3190:10:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_uint256",
                                "typeString": "uint256"
                              }
                            }
                          ],
                          "expression": {
                            "argumentTypes": [
                              {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              },
                              {
                                "typeIdentifier": "t_uint256",
                                "typeString": "uint256"
                              }
                            ],
                            "id": 200,
                            "name": "updateTimestamp",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 388,
                            "src": "3161:15:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_function_internal_nonpayable$_t_bytes32_$_t_uint256_$returns$__$",
                              "typeString": "function (bytes32,uint256)"
                            }
                          },
                          "id": 203,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "kind": "functionCall",
                          "lValueRequested": false,
                          "names": [],
                          "nodeType": "FunctionCall",
                          "src": "3161:40:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_tuple$__$",
                            "typeString": "tuple()"
                          }
                        },
                        "id": 204,
                        "nodeType": "ExpressionStatement",
                        "src": "3161:40:0"
                      },
                      {
                        "expression": null,
                        "functionReturnParameters": 114,
                        "id": 205,
                        "nodeType": "Return",
                        "src": "3215:7:0"
                      }
                    ]
                  }
                }
              ]
            },
            "documentation": null,
            "id": 209,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": false,
            "modifiers": [
              {
                "arguments": null,
                "id": 113,
                "modifierName": {
                  "argumentTypes": null,
                  "id": 112,
                  "name": "onlyOwner",
                  "nodeType": "Identifier",
                  "overloadedDeclarations": [],
                  "referencedDeclaration": 33,
                  "src": "2088:9:0",
                  "typeDescriptions": {
                    "typeIdentifier": "t_modifier$__$",
                    "typeString": "modifier ()"
                  }
                },
                "nodeType": "ModifierInvocation",
                "src": "2088:9:0"
              }
            ],
            "name": "setTenant",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 111,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 104,
                  "name": "_tenantHash",
                  "nodeType": "VariableDeclaration",
                  "scope": 209,
                  "src": "1983:19:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                  },
                  "typeName": {
                    "id": 103,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "1983:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bytes32",
                      "typeString": "bytes32"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 106,
                  "name": "_userAddress",
                  "nodeType": "VariableDeclaration",
                  "scope": 209,
                  "src": "2012:20:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 105,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "2012:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 108,
                  "name": "_timestamp",
                  "nodeType": "VariableDeclaration",
                  "scope": 209,
                  "src": "2042:18:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_uint256",
                    "typeString": "uint256"
                  },
                  "typeName": {
                    "id": 107,
                    "name": "uint256",
                    "nodeType": "ElementaryTypeName",
                    "src": "2042:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_uint256",
                      "typeString": "uint256"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 110,
                  "name": "_tenantId",
                  "nodeType": "VariableDeclaration",
                  "scope": 209,
                  "src": "2070:16:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_string_memory_ptr",
                    "typeString": "string"
                  },
                  "typeName": {
                    "id": 109,
                    "name": "string",
                    "nodeType": "ElementaryTypeName",
                    "src": "2070:6:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_string_storage_ptr",
                      "typeString": "string"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "1973:114:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 114,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "2105:0:0"
            },
            "scope": 428,
            "src": "1955:1283:0",
            "stateMutability": "nonpayable",
            "superFunction": null,
            "visibility": "public"
          },
          {
            "body": {
              "id": 256,
              "nodeType": "Block",
              "src": "3376:487:0",
              "statements": [
                {
                  "condition": {
                    "argumentTypes": null,
                    "id": 223,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "nodeType": "UnaryOperation",
                    "operator": "!",
                    "prefix": true,
                    "src": "3421:32:0",
                    "subExpression": {
                      "argumentTypes": null,
                      "arguments": [
                        {
                          "argumentTypes": null,
                          "id": 221,
                          "name": "_userAddress",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 213,
                          "src": "3440:12:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        }
                      ],
                      "expression": {
                        "argumentTypes": [
                          {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        ],
                        "id": 220,
                        "name": "userAddressExists",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 408,
                        "src": "3422:17:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_function_internal_view$_t_address_$returns$_t_bool_$",
                          "typeString": "function (address) view returns (bool)"
                        }
                      },
                      "id": 222,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "kind": "functionCall",
                      "lValueRequested": false,
                      "names": [],
                      "nodeType": "FunctionCall",
                      "src": "3422:31:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bool",
                        "typeString": "bool"
                      }
                    },
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 227,
                  "nodeType": "IfStatement",
                  "src": "3418:74:0",
                  "trueBody": {
                    "id": 226,
                    "nodeType": "Block",
                    "src": "3455:37:0",
                    "statements": [
                      {
                        "expression": {
                          "argumentTypes": null,
                          "hexValue": "66616c7365",
                          "id": 224,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": true,
                          "kind": "bool",
                          "lValueRequested": false,
                          "nodeType": "Literal",
                          "src": "3476:5:0",
                          "subdenomination": null,
                          "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                          },
                          "value": "false"
                        },
                        "functionReturnParameters": 219,
                        "id": 225,
                        "nodeType": "Return",
                        "src": "3469:12:0"
                      }
                    ]
                  }
                },
                {
                  "assignments": [
                    229
                  ],
                  "declarations": [
                    {
                      "constant": false,
                      "id": 229,
                      "name": "currentUser",
                      "nodeType": "VariableDeclaration",
                      "scope": 257,
                      "src": "3502:23:0",
                      "stateVariable": false,
                      "storageLocation": "memory",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                        "typeString": "struct IdentityStore.User"
                      },
                      "typeName": {
                        "contractScope": null,
                        "id": 228,
                        "name": "User",
                        "nodeType": "UserDefinedTypeName",
                        "referencedDeclaration": 94,
                        "src": "3502:4:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_struct$_User_$94_storage_ptr",
                          "typeString": "struct IdentityStore.User"
                        }
                      },
                      "value": null,
                      "visibility": "internal"
                    }
                  ],
                  "id": 233,
                  "initialValue": {
                    "argumentTypes": null,
                    "baseExpression": {
                      "argumentTypes": null,
                      "id": 230,
                      "name": "tenantAddressMapping",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 98,
                      "src": "3528:20:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                        "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                      }
                    },
                    "id": 232,
                    "indexExpression": {
                      "argumentTypes": null,
                      "id": 231,
                      "name": "_userAddress",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 213,
                      "src": "3549:12:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "isConstant": false,
                    "isLValue": true,
                    "isPure": false,
                    "lValueRequested": false,
                    "nodeType": "IndexAccess",
                    "src": "3528:34:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_struct$_User_$94_storage",
                      "typeString": "struct IdentityStore.User storage ref"
                    }
                  },
                  "nodeType": "VariableDeclarationStatement",
                  "src": "3502:60:0"
                },
                {
                  "condition": {
                    "argumentTypes": null,
                    "commonType": {
                      "typeIdentifier": "t_bytes32",
                      "typeString": "bytes32"
                    },
                    "id": 241,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftExpression": {
                      "argumentTypes": null,
                      "arguments": [
                        {
                          "argumentTypes": null,
                          "expression": {
                            "argumentTypes": null,
                            "id": 235,
                            "name": "currentUser",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 229,
                            "src": "3619:11:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                              "typeString": "struct IdentityStore.User memory"
                            }
                          },
                          "id": 236,
                          "isConstant": false,
                          "isLValue": true,
                          "isPure": false,
                          "lValueRequested": false,
                          "memberName": "tenantId",
                          "nodeType": "MemberAccess",
                          "referencedDeclaration": 93,
                          "src": "3619:20:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_string_memory",
                            "typeString": "string memory"
                          }
                        }
                      ],
                      "expression": {
                        "argumentTypes": [
                          {
                            "typeIdentifier": "t_string_memory",
                            "typeString": "string memory"
                          }
                        ],
                        "id": 234,
                        "name": "keccak256",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 523,
                        "src": "3609:9:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_function_sha3_pure$__$returns$_t_bytes32_$",
                          "typeString": "function () pure returns (bytes32)"
                        }
                      },
                      "id": 237,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "kind": "functionCall",
                      "lValueRequested": false,
                      "names": [],
                      "nodeType": "FunctionCall",
                      "src": "3609:31:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                      }
                    },
                    "nodeType": "BinaryOperation",
                    "operator": "!=",
                    "rightExpression": {
                      "argumentTypes": null,
                      "arguments": [
                        {
                          "argumentTypes": null,
                          "id": 239,
                          "name": "_tenantId",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 211,
                          "src": "3654:9:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_string_memory_ptr",
                            "typeString": "string memory"
                          }
                        }
                      ],
                      "expression": {
                        "argumentTypes": [
                          {
                            "typeIdentifier": "t_string_memory_ptr",
                            "typeString": "string memory"
                          }
                        ],
                        "id": 238,
                        "name": "keccak256",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 523,
                        "src": "3644:9:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_function_sha3_pure$__$returns$_t_bytes32_$",
                          "typeString": "function () pure returns (bytes32)"
                        }
                      },
                      "id": 240,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": false,
                      "kind": "functionCall",
                      "lValueRequested": false,
                      "names": [],
                      "nodeType": "FunctionCall",
                      "src": "3644:20:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                      }
                    },
                    "src": "3609:55:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 245,
                  "nodeType": "IfStatement",
                  "src": "3606:97:0",
                  "trueBody": {
                    "id": 244,
                    "nodeType": "Block",
                    "src": "3666:37:0",
                    "statements": [
                      {
                        "expression": {
                          "argumentTypes": null,
                          "hexValue": "66616c7365",
                          "id": 242,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": true,
                          "kind": "bool",
                          "lValueRequested": false,
                          "nodeType": "Literal",
                          "src": "3687:5:0",
                          "subdenomination": null,
                          "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                          },
                          "value": "false"
                        },
                        "functionReturnParameters": 219,
                        "id": 243,
                        "nodeType": "Return",
                        "src": "3680:12:0"
                      }
                    ]
                  }
                },
                {
                  "condition": {
                    "argumentTypes": null,
                    "commonType": {
                      "typeIdentifier": "t_uint256",
                      "typeString": "uint256"
                    },
                    "id": 249,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftExpression": {
                      "argumentTypes": null,
                      "expression": {
                        "argumentTypes": null,
                        "id": 246,
                        "name": "currentUser",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 229,
                        "src": "3759:11:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                          "typeString": "struct IdentityStore.User memory"
                        }
                      },
                      "id": 247,
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": false,
                      "memberName": "timestamp",
                      "nodeType": "MemberAccess",
                      "referencedDeclaration": 91,
                      "src": "3759:21:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_uint256",
                        "typeString": "uint256"
                      }
                    },
                    "nodeType": "BinaryOperation",
                    "operator": "<",
                    "rightExpression": {
                      "argumentTypes": null,
                      "id": 248,
                      "name": "_minTimestamp",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 215,
                      "src": "3783:13:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_uint256",
                        "typeString": "uint256"
                      }
                    },
                    "src": "3759:37:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 253,
                  "nodeType": "IfStatement",
                  "src": "3756:79:0",
                  "trueBody": {
                    "id": 252,
                    "nodeType": "Block",
                    "src": "3798:37:0",
                    "statements": [
                      {
                        "expression": {
                          "argumentTypes": null,
                          "hexValue": "66616c7365",
                          "id": 250,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": true,
                          "kind": "bool",
                          "lValueRequested": false,
                          "nodeType": "Literal",
                          "src": "3819:5:0",
                          "subdenomination": null,
                          "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                          },
                          "value": "false"
                        },
                        "functionReturnParameters": 219,
                        "id": 251,
                        "nodeType": "Return",
                        "src": "3812:12:0"
                      }
                    ]
                  }
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "hexValue": "74727565",
                    "id": 254,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": true,
                    "kind": "bool",
                    "lValueRequested": false,
                    "nodeType": "Literal",
                    "src": "3852:4:0",
                    "subdenomination": null,
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    },
                    "value": "true"
                  },
                  "functionReturnParameters": 219,
                  "id": 255,
                  "nodeType": "Return",
                  "src": "3845:11:0"
                }
              ]
            },
            "documentation": null,
            "id": 257,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": true,
            "modifiers": [],
            "name": "isValid",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 216,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 211,
                  "name": "_tenantId",
                  "nodeType": "VariableDeclaration",
                  "scope": 257,
                  "src": "3270:16:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_string_memory_ptr",
                    "typeString": "string"
                  },
                  "typeName": {
                    "id": 210,
                    "name": "string",
                    "nodeType": "ElementaryTypeName",
                    "src": "3270:6:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_string_storage_ptr",
                      "typeString": "string"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 213,
                  "name": "_userAddress",
                  "nodeType": "VariableDeclaration",
                  "scope": 257,
                  "src": "3297:20:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 212,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "3297:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 215,
                  "name": "_minTimestamp",
                  "nodeType": "VariableDeclaration",
                  "scope": 257,
                  "src": "3327:21:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_uint256",
                    "typeString": "uint256"
                  },
                  "typeName": {
                    "id": 214,
                    "name": "uint256",
                    "nodeType": "ElementaryTypeName",
                    "src": "3327:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_uint256",
                      "typeString": "uint256"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "3260:89:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 219,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 218,
                  "name": "",
                  "nodeType": "VariableDeclaration",
                  "scope": 257,
                  "src": "3370:4:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bool",
                    "typeString": "bool"
                  },
                  "typeName": {
                    "id": 217,
                    "name": "bool",
                    "nodeType": "ElementaryTypeName",
                    "src": "3370:4:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "3369:6:0"
            },
            "scope": 428,
            "src": "3244:619:0",
            "stateMutability": "view",
            "superFunction": null,
            "visibility": "public"
          },
          {
            "body": {
              "id": 319,
              "nodeType": "Block",
              "src": "3981:680:0",
              "statements": [
                {
                  "expression": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "arguments": [
                          {
                            "argumentTypes": null,
                            "id": 268,
                            "name": "_oldHash",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 259,
                            "src": "4021:8:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            }
                          }
                        ],
                        "expression": {
                          "argumentTypes": [
                            {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            }
                          ],
                          "id": 267,
                          "name": "userTenantHashExists",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 427,
                          "src": "4000:20:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_function_internal_view$_t_bytes32_$returns$_t_bool_$",
                            "typeString": "function (bytes32) view returns (bool)"
                          }
                        },
                        "id": 269,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "4000:30:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      },
                      {
                        "argumentTypes": null,
                        "hexValue": "4f6c64206861736820646f6573206e6f742065786973742e",
                        "id": 270,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": true,
                        "kind": "string",
                        "lValueRequested": false,
                        "nodeType": "Literal",
                        "src": "4032:26:0",
                        "subdenomination": null,
                        "typeDescriptions": {
                          "typeIdentifier": "t_stringliteral_b8700c17c6c187693f3b5aed9e32b4020bef3af87a53f2dfbedfc5d2ef1b0560",
                          "typeString": "literal_string \"Old hash does not exist.\""
                        },
                        "value": "Old hash does not exist."
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        },
                        {
                          "typeIdentifier": "t_stringliteral_b8700c17c6c187693f3b5aed9e32b4020bef3af87a53f2dfbedfc5d2ef1b0560",
                          "typeString": "literal_string \"Old hash does not exist.\""
                        }
                      ],
                      "id": 266,
                      "name": "require",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [
                        532,
                        533
                      ],
                      "referencedDeclaration": 533,
                      "src": "3992:7:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                        "typeString": "function (bool,string memory) pure"
                      }
                    },
                    "id": 271,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "3992:67:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 272,
                  "nodeType": "ExpressionStatement",
                  "src": "3992:67:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "id": 277,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "nodeType": "UnaryOperation",
                        "operator": "!",
                        "prefix": true,
                        "src": "4077:31:0",
                        "subExpression": {
                          "argumentTypes": null,
                          "arguments": [
                            {
                              "argumentTypes": null,
                              "id": 275,
                              "name": "_newHash",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 261,
                              "src": "4099:8:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              }
                            }
                          ],
                          "expression": {
                            "argumentTypes": [
                              {
                                "typeIdentifier": "t_bytes32",
                                "typeString": "bytes32"
                              }
                            ],
                            "id": 274,
                            "name": "userTenantHashExists",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 427,
                            "src": "4078:20:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_function_internal_view$_t_bytes32_$returns$_t_bool_$",
                              "typeString": "function (bytes32) view returns (bool)"
                            }
                          },
                          "id": 276,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "kind": "functionCall",
                          "lValueRequested": false,
                          "names": [],
                          "nodeType": "FunctionCall",
                          "src": "4078:30:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                          }
                        },
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      },
                      {
                        "argumentTypes": null,
                        "hexValue": "4e6577206861736820697320616c726561647920726567697374657265642e",
                        "id": 278,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": true,
                        "kind": "string",
                        "lValueRequested": false,
                        "nodeType": "Literal",
                        "src": "4110:33:0",
                        "subdenomination": null,
                        "typeDescriptions": {
                          "typeIdentifier": "t_stringliteral_0ba289e2ad90e453db834a95ce678dd3931ad19c254b07b01da7cb9c678d4148",
                          "typeString": "literal_string \"New hash is already registered.\""
                        },
                        "value": "New hash is already registered."
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        },
                        {
                          "typeIdentifier": "t_stringliteral_0ba289e2ad90e453db834a95ce678dd3931ad19c254b07b01da7cb9c678d4148",
                          "typeString": "literal_string \"New hash is already registered.\""
                        }
                      ],
                      "id": 273,
                      "name": "require",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [
                        532,
                        533
                      ],
                      "referencedDeclaration": 533,
                      "src": "4069:7:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                        "typeString": "function (bool,string memory) pure"
                      }
                    },
                    "id": 279,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "4069:75:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 280,
                  "nodeType": "ExpressionStatement",
                  "src": "4069:75:0"
                },
                {
                  "assignments": [
                    282
                  ],
                  "declarations": [
                    {
                      "constant": false,
                      "id": 282,
                      "name": "currentAddress",
                      "nodeType": "VariableDeclaration",
                      "scope": 320,
                      "src": "4154:22:0",
                      "stateVariable": false,
                      "storageLocation": "default",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      },
                      "typeName": {
                        "id": 281,
                        "name": "address",
                        "nodeType": "ElementaryTypeName",
                        "src": "4154:7:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      },
                      "value": null,
                      "visibility": "internal"
                    }
                  ],
                  "id": 286,
                  "initialValue": {
                    "argumentTypes": null,
                    "baseExpression": {
                      "argumentTypes": null,
                      "id": 283,
                      "name": "tenantHashMapping",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 102,
                      "src": "4179:17:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                        "typeString": "mapping(bytes32 => address)"
                      }
                    },
                    "id": 285,
                    "indexExpression": {
                      "argumentTypes": null,
                      "id": 284,
                      "name": "_oldHash",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 259,
                      "src": "4197:8:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                      }
                    },
                    "isConstant": false,
                    "isLValue": true,
                    "isPure": false,
                    "lValueRequested": false,
                    "nodeType": "IndexAccess",
                    "src": "4179:27:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "nodeType": "VariableDeclarationStatement",
                  "src": "4154:52:0"
                },
                {
                  "assignments": [
                    288
                  ],
                  "declarations": [
                    {
                      "constant": false,
                      "id": 288,
                      "name": "oldUserInfo",
                      "nodeType": "VariableDeclaration",
                      "scope": 320,
                      "src": "4216:23:0",
                      "stateVariable": false,
                      "storageLocation": "memory",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                        "typeString": "struct IdentityStore.User"
                      },
                      "typeName": {
                        "contractScope": null,
                        "id": 287,
                        "name": "User",
                        "nodeType": "UserDefinedTypeName",
                        "referencedDeclaration": 94,
                        "src": "4216:4:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_struct$_User_$94_storage_ptr",
                          "typeString": "struct IdentityStore.User"
                        }
                      },
                      "value": null,
                      "visibility": "internal"
                    }
                  ],
                  "id": 292,
                  "initialValue": {
                    "argumentTypes": null,
                    "baseExpression": {
                      "argumentTypes": null,
                      "id": 289,
                      "name": "tenantAddressMapping",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 98,
                      "src": "4242:20:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                        "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                      }
                    },
                    "id": 291,
                    "indexExpression": {
                      "argumentTypes": null,
                      "id": 290,
                      "name": "currentAddress",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 282,
                      "src": "4263:14:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "isConstant": false,
                    "isLValue": true,
                    "isPure": false,
                    "lValueRequested": false,
                    "nodeType": "IndexAccess",
                    "src": "4242:36:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_struct$_User_$94_storage",
                      "typeString": "struct IdentityStore.User storage ref"
                    }
                  },
                  "nodeType": "VariableDeclarationStatement",
                  "src": "4216:62:0"
                },
                {
                  "assignments": [
                    294
                  ],
                  "declarations": [
                    {
                      "constant": false,
                      "id": 294,
                      "name": "newUserInfo",
                      "nodeType": "VariableDeclaration",
                      "scope": 320,
                      "src": "4288:23:0",
                      "stateVariable": false,
                      "storageLocation": "memory",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                        "typeString": "struct IdentityStore.User"
                      },
                      "typeName": {
                        "contractScope": null,
                        "id": 293,
                        "name": "User",
                        "nodeType": "UserDefinedTypeName",
                        "referencedDeclaration": 94,
                        "src": "4288:4:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_struct$_User_$94_storage_ptr",
                          "typeString": "struct IdentityStore.User"
                        }
                      },
                      "value": null,
                      "visibility": "internal"
                    }
                  ],
                  "id": 301,
                  "initialValue": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "id": 296,
                        "name": "_newHash",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 261,
                        "src": "4319:8:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bytes32",
                          "typeString": "bytes32"
                        }
                      },
                      {
                        "argumentTypes": null,
                        "id": 297,
                        "name": "_timestamp",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 263,
                        "src": "4329:10:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_uint256",
                          "typeString": "uint256"
                        }
                      },
                      {
                        "argumentTypes": null,
                        "expression": {
                          "argumentTypes": null,
                          "id": 298,
                          "name": "oldUserInfo",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 288,
                          "src": "4341:11:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                            "typeString": "struct IdentityStore.User memory"
                          }
                        },
                        "id": 299,
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": false,
                        "memberName": "tenantId",
                        "nodeType": "MemberAccess",
                        "referencedDeclaration": 93,
                        "src": "4341:20:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_string_memory",
                          "typeString": "string memory"
                        }
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_bytes32",
                          "typeString": "bytes32"
                        },
                        {
                          "typeIdentifier": "t_uint256",
                          "typeString": "uint256"
                        },
                        {
                          "typeIdentifier": "t_string_memory",
                          "typeString": "string memory"
                        }
                      ],
                      "id": 295,
                      "name": "User",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 94,
                      "src": "4314:4:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_type$_t_struct$_User_$94_storage_ptr_$",
                        "typeString": "type(struct IdentityStore.User storage pointer)"
                      }
                    },
                    "id": 300,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "structConstructorCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "4314:48:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_struct$_User_$94_memory",
                      "typeString": "struct IdentityStore.User memory"
                    }
                  },
                  "nodeType": "VariableDeclarationStatement",
                  "src": "4288:74:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 306,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftHandSide": {
                      "argumentTypes": null,
                      "baseExpression": {
                        "argumentTypes": null,
                        "id": 302,
                        "name": "tenantAddressMapping",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 98,
                        "src": "4415:20:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                          "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                        }
                      },
                      "id": 304,
                      "indexExpression": {
                        "argumentTypes": null,
                        "id": 303,
                        "name": "currentAddress",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 282,
                        "src": "4436:14:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      },
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": true,
                      "nodeType": "IndexAccess",
                      "src": "4415:36:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_storage",
                        "typeString": "struct IdentityStore.User storage ref"
                      }
                    },
                    "nodeType": "Assignment",
                    "operator": "=",
                    "rightHandSide": {
                      "argumentTypes": null,
                      "id": 305,
                      "name": "newUserInfo",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 294,
                      "src": "4454:11:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                        "typeString": "struct IdentityStore.User memory"
                      }
                    },
                    "src": "4415:50:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_struct$_User_$94_storage",
                      "typeString": "struct IdentityStore.User storage ref"
                    }
                  },
                  "id": 307,
                  "nodeType": "ExpressionStatement",
                  "src": "4415:50:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 311,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "nodeType": "UnaryOperation",
                    "operator": "delete",
                    "prefix": true,
                    "src": "4522:34:0",
                    "subExpression": {
                      "argumentTypes": null,
                      "baseExpression": {
                        "argumentTypes": null,
                        "id": 308,
                        "name": "tenantHashMapping",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 102,
                        "src": "4529:17:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                          "typeString": "mapping(bytes32 => address)"
                        }
                      },
                      "id": 310,
                      "indexExpression": {
                        "argumentTypes": null,
                        "id": 309,
                        "name": "_oldHash",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 259,
                        "src": "4547:8:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bytes32",
                          "typeString": "bytes32"
                        }
                      },
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": true,
                      "nodeType": "IndexAccess",
                      "src": "4529:27:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 312,
                  "nodeType": "ExpressionStatement",
                  "src": "4522:34:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 317,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftHandSide": {
                      "argumentTypes": null,
                      "baseExpression": {
                        "argumentTypes": null,
                        "id": 313,
                        "name": "tenantHashMapping",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 102,
                        "src": "4610:17:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                          "typeString": "mapping(bytes32 => address)"
                        }
                      },
                      "id": 315,
                      "indexExpression": {
                        "argumentTypes": null,
                        "id": 314,
                        "name": "_newHash",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 261,
                        "src": "4628:8:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bytes32",
                          "typeString": "bytes32"
                        }
                      },
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": true,
                      "nodeType": "IndexAccess",
                      "src": "4610:27:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "nodeType": "Assignment",
                    "operator": "=",
                    "rightHandSide": {
                      "argumentTypes": null,
                      "id": 316,
                      "name": "currentAddress",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 282,
                      "src": "4640:14:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "src": "4610:44:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "id": 318,
                  "nodeType": "ExpressionStatement",
                  "src": "4610:44:0"
                }
              ]
            },
            "documentation": null,
            "id": 320,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": false,
            "modifiers": [],
            "name": "updateHash",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 264,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 259,
                  "name": "_oldHash",
                  "nodeType": "VariableDeclaration",
                  "scope": 320,
                  "src": "3898:16:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                  },
                  "typeName": {
                    "id": 258,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "3898:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bytes32",
                      "typeString": "bytes32"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 261,
                  "name": "_newHash",
                  "nodeType": "VariableDeclaration",
                  "scope": 320,
                  "src": "3925:16:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                  },
                  "typeName": {
                    "id": 260,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "3925:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bytes32",
                      "typeString": "bytes32"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 263,
                  "name": "_timestamp",
                  "nodeType": "VariableDeclaration",
                  "scope": 320,
                  "src": "3952:18:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_uint256",
                    "typeString": "uint256"
                  },
                  "typeName": {
                    "id": 262,
                    "name": "uint256",
                    "nodeType": "ElementaryTypeName",
                    "src": "3952:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_uint256",
                      "typeString": "uint256"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "3888:83:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 265,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "3981:0:0"
            },
            "scope": 428,
            "src": "3869:792:0",
            "stateMutability": "nonpayable",
            "superFunction": null,
            "visibility": "internal"
          },
          {
            "body": {
              "id": 368,
              "nodeType": "Block",
              "src": "4757:478:0",
              "statements": [
                {
                  "assignments": [
                    330
                  ],
                  "declarations": [
                    {
                      "constant": false,
                      "id": 330,
                      "name": "existingUser",
                      "nodeType": "VariableDeclaration",
                      "scope": 369,
                      "src": "4767:24:0",
                      "stateVariable": false,
                      "storageLocation": "memory",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                        "typeString": "struct IdentityStore.User"
                      },
                      "typeName": {
                        "contractScope": null,
                        "id": 329,
                        "name": "User",
                        "nodeType": "UserDefinedTypeName",
                        "referencedDeclaration": 94,
                        "src": "4767:4:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_struct$_User_$94_storage_ptr",
                          "typeString": "struct IdentityStore.User"
                        }
                      },
                      "value": null,
                      "visibility": "internal"
                    }
                  ],
                  "id": 334,
                  "initialValue": {
                    "argumentTypes": null,
                    "baseExpression": {
                      "argumentTypes": null,
                      "id": 331,
                      "name": "tenantAddressMapping",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 98,
                      "src": "4794:20:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                        "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                      }
                    },
                    "id": 333,
                    "indexExpression": {
                      "argumentTypes": null,
                      "id": 332,
                      "name": "oldUserAddress",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 322,
                      "src": "4815:14:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "isConstant": false,
                    "isLValue": true,
                    "isPure": false,
                    "lValueRequested": false,
                    "nodeType": "IndexAccess",
                    "src": "4794:36:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_struct$_User_$94_storage",
                      "typeString": "struct IdentityStore.User storage ref"
                    }
                  },
                  "nodeType": "VariableDeclarationStatement",
                  "src": "4767:63:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "id": 339,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "lValueRequested": false,
                        "nodeType": "UnaryOperation",
                        "operator": "!",
                        "prefix": true,
                        "src": "4857:34:0",
                        "subExpression": {
                          "argumentTypes": null,
                          "arguments": [
                            {
                              "argumentTypes": null,
                              "id": 337,
                              "name": "newUserAddress",
                              "nodeType": "Identifier",
                              "overloadedDeclarations": [],
                              "referencedDeclaration": 324,
                              "src": "4876:14:0",
                              "typeDescriptions": {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              }
                            }
                          ],
                          "expression": {
                            "argumentTypes": [
                              {
                                "typeIdentifier": "t_address",
                                "typeString": "address"
                              }
                            ],
                            "id": 336,
                            "name": "userAddressExists",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 408,
                            "src": "4858:17:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_function_internal_view$_t_address_$returns$_t_bool_$",
                              "typeString": "function (address) view returns (bool)"
                            }
                          },
                          "id": 338,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": false,
                          "kind": "functionCall",
                          "lValueRequested": false,
                          "names": [],
                          "nodeType": "FunctionCall",
                          "src": "4858:33:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                          }
                        },
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      },
                      {
                        "argumentTypes": null,
                        "hexValue": "5468657265277320616c726561647920616e206163636f756e74207469656420746f20746869732061646472657373",
                        "id": 340,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": true,
                        "kind": "string",
                        "lValueRequested": false,
                        "nodeType": "Literal",
                        "src": "4893:49:0",
                        "subdenomination": null,
                        "typeDescriptions": {
                          "typeIdentifier": "t_stringliteral_d9560d649baa3d7d7d6686d1da4373048e51f0d0b91e83baff65cef3893b4f78",
                          "typeString": "literal_string \"There's already an account tied to this address\""
                        },
                        "value": "There's already an account tied to this address"
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        },
                        {
                          "typeIdentifier": "t_stringliteral_d9560d649baa3d7d7d6686d1da4373048e51f0d0b91e83baff65cef3893b4f78",
                          "typeString": "literal_string \"There's already an account tied to this address\""
                        }
                      ],
                      "id": 335,
                      "name": "require",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [
                        532,
                        533
                      ],
                      "referencedDeclaration": 533,
                      "src": "4849:7:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                        "typeString": "function (bool,string memory) pure"
                      }
                    },
                    "id": 341,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "4849:94:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 342,
                  "nodeType": "ExpressionStatement",
                  "src": "4849:94:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "arguments": [
                      {
                        "argumentTypes": null,
                        "arguments": [
                          {
                            "argumentTypes": null,
                            "id": 345,
                            "name": "oldUserAddress",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 322,
                            "src": "4979:14:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            }
                          }
                        ],
                        "expression": {
                          "argumentTypes": [
                            {
                              "typeIdentifier": "t_address",
                              "typeString": "address"
                            }
                          ],
                          "id": 344,
                          "name": "userAddressExists",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 408,
                          "src": "4961:17:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_function_internal_view$_t_address_$returns$_t_bool_$",
                            "typeString": "function (address) view returns (bool)"
                          }
                        },
                        "id": 346,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": false,
                        "kind": "functionCall",
                        "lValueRequested": false,
                        "names": [],
                        "nodeType": "FunctionCall",
                        "src": "4961:33:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        }
                      },
                      {
                        "argumentTypes": null,
                        "hexValue": "54686572652773206e6f206163636f756e74207469656420746f207468652061646472657373206f726967696e",
                        "id": 347,
                        "isConstant": false,
                        "isLValue": false,
                        "isPure": true,
                        "kind": "string",
                        "lValueRequested": false,
                        "nodeType": "Literal",
                        "src": "4996:47:0",
                        "subdenomination": null,
                        "typeDescriptions": {
                          "typeIdentifier": "t_stringliteral_9bce1635c23a28e7d2bc063a3170a795f5e51362f4736a79230f6fc9fa52d788",
                          "typeString": "literal_string \"There's no account tied to the address origin\""
                        },
                        "value": "There's no account tied to the address origin"
                      }
                    ],
                    "expression": {
                      "argumentTypes": [
                        {
                          "typeIdentifier": "t_bool",
                          "typeString": "bool"
                        },
                        {
                          "typeIdentifier": "t_stringliteral_9bce1635c23a28e7d2bc063a3170a795f5e51362f4736a79230f6fc9fa52d788",
                          "typeString": "literal_string \"There's no account tied to the address origin\""
                        }
                      ],
                      "id": 343,
                      "name": "require",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [
                        532,
                        533
                      ],
                      "referencedDeclaration": 533,
                      "src": "4953:7:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                        "typeString": "function (bool,string memory) pure"
                      }
                    },
                    "id": 348,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "kind": "functionCall",
                    "lValueRequested": false,
                    "names": [],
                    "nodeType": "FunctionCall",
                    "src": "4953:91:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 349,
                  "nodeType": "ExpressionStatement",
                  "src": "4953:91:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 355,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftHandSide": {
                      "argumentTypes": null,
                      "baseExpression": {
                        "argumentTypes": null,
                        "id": 350,
                        "name": "tenantHashMapping",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 102,
                        "src": "5055:17:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                          "typeString": "mapping(bytes32 => address)"
                        }
                      },
                      "id": 353,
                      "indexExpression": {
                        "argumentTypes": null,
                        "expression": {
                          "argumentTypes": null,
                          "id": 351,
                          "name": "existingUser",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 330,
                          "src": "5073:12:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                            "typeString": "struct IdentityStore.User memory"
                          }
                        },
                        "id": 352,
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": false,
                        "memberName": "tenantHash",
                        "nodeType": "MemberAccess",
                        "referencedDeclaration": 89,
                        "src": "5073:23:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bytes32",
                          "typeString": "bytes32"
                        }
                      },
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": true,
                      "nodeType": "IndexAccess",
                      "src": "5055:42:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "nodeType": "Assignment",
                    "operator": "=",
                    "rightHandSide": {
                      "argumentTypes": null,
                      "id": 354,
                      "name": "newUserAddress",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 324,
                      "src": "5100:14:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "src": "5055:59:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "id": 356,
                  "nodeType": "ExpressionStatement",
                  "src": "5055:59:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 361,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftHandSide": {
                      "argumentTypes": null,
                      "baseExpression": {
                        "argumentTypes": null,
                        "id": 357,
                        "name": "tenantAddressMapping",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 98,
                        "src": "5124:20:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                          "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                        }
                      },
                      "id": 359,
                      "indexExpression": {
                        "argumentTypes": null,
                        "id": 358,
                        "name": "newUserAddress",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 324,
                        "src": "5145:14:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      },
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": true,
                      "nodeType": "IndexAccess",
                      "src": "5124:36:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_storage",
                        "typeString": "struct IdentityStore.User storage ref"
                      }
                    },
                    "nodeType": "Assignment",
                    "operator": "=",
                    "rightHandSide": {
                      "argumentTypes": null,
                      "id": 360,
                      "name": "existingUser",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 330,
                      "src": "5163:12:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_memory_ptr",
                        "typeString": "struct IdentityStore.User memory"
                      }
                    },
                    "src": "5124:51:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_struct$_User_$94_storage",
                      "typeString": "struct IdentityStore.User storage ref"
                    }
                  },
                  "id": 362,
                  "nodeType": "ExpressionStatement",
                  "src": "5124:51:0"
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 366,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "nodeType": "UnaryOperation",
                    "operator": "delete",
                    "prefix": true,
                    "src": "5185:43:0",
                    "subExpression": {
                      "argumentTypes": null,
                      "baseExpression": {
                        "argumentTypes": null,
                        "id": 363,
                        "name": "tenantAddressMapping",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 98,
                        "src": "5192:20:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                          "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                        }
                      },
                      "id": 365,
                      "indexExpression": {
                        "argumentTypes": null,
                        "id": 364,
                        "name": "oldUserAddress",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 322,
                        "src": "5213:14:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_address",
                          "typeString": "address"
                        }
                      },
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": true,
                      "nodeType": "IndexAccess",
                      "src": "5192:36:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_struct$_User_$94_storage",
                        "typeString": "struct IdentityStore.User storage ref"
                      }
                    },
                    "typeDescriptions": {
                      "typeIdentifier": "t_tuple$__$",
                      "typeString": "tuple()"
                    }
                  },
                  "id": 367,
                  "nodeType": "ExpressionStatement",
                  "src": "5185:43:0"
                }
              ]
            },
            "documentation": null,
            "id": 369,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": false,
            "modifiers": [
              {
                "arguments": null,
                "id": 327,
                "modifierName": {
                  "argumentTypes": null,
                  "id": 326,
                  "name": "onlyOwner",
                  "nodeType": "Identifier",
                  "overloadedDeclarations": [],
                  "referencedDeclaration": 33,
                  "src": "4738:9:0",
                  "typeDescriptions": {
                    "typeIdentifier": "t_modifier$__$",
                    "typeString": "modifier ()"
                  }
                },
                "nodeType": "ModifierInvocation",
                "src": "4738:9:0"
              }
            ],
            "name": "updateAddress",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 325,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 322,
                  "name": "oldUserAddress",
                  "nodeType": "VariableDeclaration",
                  "scope": 369,
                  "src": "4690:22:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 321,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "4690:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 324,
                  "name": "newUserAddress",
                  "nodeType": "VariableDeclaration",
                  "scope": 369,
                  "src": "4714:22:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 323,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "4714:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "4689:48:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 328,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "4757:0:0"
            },
            "scope": 428,
            "src": "4667:568:0",
            "stateMutability": "nonpayable",
            "superFunction": null,
            "visibility": "internal"
          },
          {
            "body": {
              "id": 387,
              "nodeType": "Block",
              "src": "5326:92:0",
              "statements": [
                {
                  "expression": {
                    "argumentTypes": null,
                    "id": 385,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftHandSide": {
                      "argumentTypes": null,
                      "expression": {
                        "argumentTypes": null,
                        "baseExpression": {
                          "argumentTypes": null,
                          "id": 378,
                          "name": "tenantAddressMapping",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 98,
                          "src": "5336:20:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                            "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                          }
                        },
                        "id": 382,
                        "indexExpression": {
                          "argumentTypes": null,
                          "baseExpression": {
                            "argumentTypes": null,
                            "id": 379,
                            "name": "tenantHashMapping",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 102,
                            "src": "5357:17:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                              "typeString": "mapping(bytes32 => address)"
                            }
                          },
                          "id": 381,
                          "indexExpression": {
                            "argumentTypes": null,
                            "id": 380,
                            "name": "_tenantHash",
                            "nodeType": "Identifier",
                            "overloadedDeclarations": [],
                            "referencedDeclaration": 371,
                            "src": "5375:11:0",
                            "typeDescriptions": {
                              "typeIdentifier": "t_bytes32",
                              "typeString": "bytes32"
                            }
                          },
                          "isConstant": false,
                          "isLValue": true,
                          "isPure": false,
                          "lValueRequested": false,
                          "nodeType": "IndexAccess",
                          "src": "5357:30:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": false,
                        "nodeType": "IndexAccess",
                        "src": "5336:52:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_struct$_User_$94_storage",
                          "typeString": "struct IdentityStore.User storage ref"
                        }
                      },
                      "id": 383,
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": true,
                      "memberName": "timestamp",
                      "nodeType": "MemberAccess",
                      "referencedDeclaration": 91,
                      "src": "5336:62:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_uint256",
                        "typeString": "uint256"
                      }
                    },
                    "nodeType": "Assignment",
                    "operator": "=",
                    "rightHandSide": {
                      "argumentTypes": null,
                      "id": 384,
                      "name": "_timestamp",
                      "nodeType": "Identifier",
                      "overloadedDeclarations": [],
                      "referencedDeclaration": 373,
                      "src": "5401:10:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_uint256",
                        "typeString": "uint256"
                      }
                    },
                    "src": "5336:75:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_uint256",
                      "typeString": "uint256"
                    }
                  },
                  "id": 386,
                  "nodeType": "ExpressionStatement",
                  "src": "5336:75:0"
                }
              ]
            },
            "documentation": null,
            "id": 388,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": false,
            "modifiers": [
              {
                "arguments": null,
                "id": 376,
                "modifierName": {
                  "argumentTypes": null,
                  "id": 375,
                  "name": "onlyOwner",
                  "nodeType": "Identifier",
                  "overloadedDeclarations": [],
                  "referencedDeclaration": 33,
                  "src": "5307:9:0",
                  "typeDescriptions": {
                    "typeIdentifier": "t_modifier$__$",
                    "typeString": "modifier ()"
                  }
                },
                "nodeType": "ModifierInvocation",
                "src": "5307:9:0"
              }
            ],
            "name": "updateTimestamp",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 374,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 371,
                  "name": "_tenantHash",
                  "nodeType": "VariableDeclaration",
                  "scope": 388,
                  "src": "5266:19:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                  },
                  "typeName": {
                    "id": 370,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "5266:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bytes32",
                      "typeString": "bytes32"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                },
                {
                  "constant": false,
                  "id": 373,
                  "name": "_timestamp",
                  "nodeType": "VariableDeclaration",
                  "scope": 388,
                  "src": "5287:18:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_uint256",
                    "typeString": "uint256"
                  },
                  "typeName": {
                    "id": 372,
                    "name": "uint256",
                    "nodeType": "ElementaryTypeName",
                    "src": "5287:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_uint256",
                      "typeString": "uint256"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "5265:41:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 377,
              "nodeType": "ParameterList",
              "parameters": [],
              "src": "5326:0:0"
            },
            "scope": 428,
            "src": "5241:177:0",
            "stateMutability": "nonpayable",
            "superFunction": null,
            "visibility": "internal"
          },
          {
            "body": {
              "id": 407,
              "nodeType": "Block",
              "src": "5500:135:0",
              "statements": [
                {
                  "condition": {
                    "argumentTypes": null,
                    "commonType": {
                      "typeIdentifier": "t_bytes32",
                      "typeString": "bytes32"
                    },
                    "id": 400,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftExpression": {
                      "argumentTypes": null,
                      "expression": {
                        "argumentTypes": null,
                        "baseExpression": {
                          "argumentTypes": null,
                          "id": 395,
                          "name": "tenantAddressMapping",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 98,
                          "src": "5520:20:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_mapping$_t_address_$_t_struct$_User_$94_storage_$",
                            "typeString": "mapping(address => struct IdentityStore.User storage ref)"
                          }
                        },
                        "id": 397,
                        "indexExpression": {
                          "argumentTypes": null,
                          "id": 396,
                          "name": "userAddress",
                          "nodeType": "Identifier",
                          "overloadedDeclarations": [],
                          "referencedDeclaration": 390,
                          "src": "5541:11:0",
                          "typeDescriptions": {
                            "typeIdentifier": "t_address",
                            "typeString": "address"
                          }
                        },
                        "isConstant": false,
                        "isLValue": true,
                        "isPure": false,
                        "lValueRequested": false,
                        "nodeType": "IndexAccess",
                        "src": "5520:33:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_struct$_User_$94_storage",
                          "typeString": "struct IdentityStore.User storage ref"
                        }
                      },
                      "id": 398,
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": false,
                      "memberName": "tenantHash",
                      "nodeType": "MemberAccess",
                      "referencedDeclaration": 89,
                      "src": "5520:44:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_bytes32",
                        "typeString": "bytes32"
                      }
                    },
                    "nodeType": "BinaryOperation",
                    "operator": "==",
                    "rightExpression": {
                      "argumentTypes": null,
                      "hexValue": "30",
                      "id": 399,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": true,
                      "kind": "number",
                      "lValueRequested": false,
                      "nodeType": "Literal",
                      "src": "5568:1:0",
                      "subdenomination": null,
                      "typeDescriptions": {
                        "typeIdentifier": "t_rational_0_by_1",
                        "typeString": "int_const 0"
                      },
                      "value": "0"
                    },
                    "src": "5520:49:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 404,
                  "nodeType": "IfStatement",
                  "src": "5517:91:0",
                  "trueBody": {
                    "id": 403,
                    "nodeType": "Block",
                    "src": "5571:37:0",
                    "statements": [
                      {
                        "expression": {
                          "argumentTypes": null,
                          "hexValue": "66616c7365",
                          "id": 401,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": true,
                          "kind": "bool",
                          "lValueRequested": false,
                          "nodeType": "Literal",
                          "src": "5592:5:0",
                          "subdenomination": null,
                          "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                          },
                          "value": "false"
                        },
                        "functionReturnParameters": 394,
                        "id": 402,
                        "nodeType": "Return",
                        "src": "5585:12:0"
                      }
                    ]
                  }
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "hexValue": "74727565",
                    "id": 405,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": true,
                    "kind": "bool",
                    "lValueRequested": false,
                    "nodeType": "Literal",
                    "src": "5624:4:0",
                    "subdenomination": null,
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    },
                    "value": "true"
                  },
                  "functionReturnParameters": 394,
                  "id": 406,
                  "nodeType": "Return",
                  "src": "5617:11:0"
                }
              ]
            },
            "documentation": null,
            "id": 408,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": true,
            "modifiers": [],
            "name": "userAddressExists",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 391,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 390,
                  "name": "userAddress",
                  "nodeType": "VariableDeclaration",
                  "scope": 408,
                  "src": "5451:19:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_address",
                    "typeString": "address"
                  },
                  "typeName": {
                    "id": 389,
                    "name": "address",
                    "nodeType": "ElementaryTypeName",
                    "src": "5451:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "5450:21:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 394,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 393,
                  "name": "",
                  "nodeType": "VariableDeclaration",
                  "scope": 408,
                  "src": "5494:4:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bool",
                    "typeString": "bool"
                  },
                  "typeName": {
                    "id": 392,
                    "name": "bool",
                    "nodeType": "ElementaryTypeName",
                    "src": "5494:4:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "5493:6:0"
            },
            "scope": 428,
            "src": "5424:211:0",
            "stateMutability": "view",
            "superFunction": null,
            "visibility": "internal"
          },
          {
            "body": {
              "id": 426,
              "nodeType": "Block",
              "src": "5718:163:0",
              "statements": [
                {
                  "condition": {
                    "argumentTypes": null,
                    "commonType": {
                      "typeIdentifier": "t_address",
                      "typeString": "address"
                    },
                    "id": 419,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": false,
                    "lValueRequested": false,
                    "leftExpression": {
                      "argumentTypes": null,
                      "baseExpression": {
                        "argumentTypes": null,
                        "id": 415,
                        "name": "tenantHashMapping",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 102,
                        "src": "5781:17:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_mapping$_t_bytes32_$_t_address_$",
                          "typeString": "mapping(bytes32 => address)"
                        }
                      },
                      "id": 417,
                      "indexExpression": {
                        "argumentTypes": null,
                        "id": 416,
                        "name": "tenantHash",
                        "nodeType": "Identifier",
                        "overloadedDeclarations": [],
                        "referencedDeclaration": 410,
                        "src": "5799:10:0",
                        "typeDescriptions": {
                          "typeIdentifier": "t_bytes32",
                          "typeString": "bytes32"
                        }
                      },
                      "isConstant": false,
                      "isLValue": true,
                      "isPure": false,
                      "lValueRequested": false,
                      "nodeType": "IndexAccess",
                      "src": "5781:29:0",
                      "typeDescriptions": {
                        "typeIdentifier": "t_address",
                        "typeString": "address"
                      }
                    },
                    "nodeType": "BinaryOperation",
                    "operator": "==",
                    "rightExpression": {
                      "argumentTypes": null,
                      "hexValue": "30",
                      "id": 418,
                      "isConstant": false,
                      "isLValue": false,
                      "isPure": true,
                      "kind": "number",
                      "lValueRequested": false,
                      "nodeType": "Literal",
                      "src": "5814:1:0",
                      "subdenomination": null,
                      "typeDescriptions": {
                        "typeIdentifier": "t_rational_0_by_1",
                        "typeString": "int_const 0"
                      },
                      "value": "0"
                    },
                    "src": "5781:34:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "falseBody": null,
                  "id": 423,
                  "nodeType": "IfStatement",
                  "src": "5778:76:0",
                  "trueBody": {
                    "id": 422,
                    "nodeType": "Block",
                    "src": "5817:37:0",
                    "statements": [
                      {
                        "expression": {
                          "argumentTypes": null,
                          "hexValue": "66616c7365",
                          "id": 420,
                          "isConstant": false,
                          "isLValue": false,
                          "isPure": true,
                          "kind": "bool",
                          "lValueRequested": false,
                          "nodeType": "Literal",
                          "src": "5838:5:0",
                          "subdenomination": null,
                          "typeDescriptions": {
                            "typeIdentifier": "t_bool",
                            "typeString": "bool"
                          },
                          "value": "false"
                        },
                        "functionReturnParameters": 414,
                        "id": 421,
                        "nodeType": "Return",
                        "src": "5831:12:0"
                      }
                    ]
                  }
                },
                {
                  "expression": {
                    "argumentTypes": null,
                    "hexValue": "74727565",
                    "id": 424,
                    "isConstant": false,
                    "isLValue": false,
                    "isPure": true,
                    "kind": "bool",
                    "lValueRequested": false,
                    "nodeType": "Literal",
                    "src": "5870:4:0",
                    "subdenomination": null,
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    },
                    "value": "true"
                  },
                  "functionReturnParameters": 414,
                  "id": 425,
                  "nodeType": "Return",
                  "src": "5863:11:0"
                }
              ]
            },
            "documentation": null,
            "id": 427,
            "implemented": true,
            "isConstructor": false,
            "isDeclaredConst": true,
            "modifiers": [],
            "name": "userTenantHashExists",
            "nodeType": "FunctionDefinition",
            "parameters": {
              "id": 411,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 410,
                  "name": "tenantHash",
                  "nodeType": "VariableDeclaration",
                  "scope": 427,
                  "src": "5671:18:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bytes32",
                    "typeString": "bytes32"
                  },
                  "typeName": {
                    "id": 409,
                    "name": "bytes32",
                    "nodeType": "ElementaryTypeName",
                    "src": "5671:7:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bytes32",
                      "typeString": "bytes32"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "5670:20:0"
            },
            "payable": false,
            "returnParameters": {
              "id": 414,
              "nodeType": "ParameterList",
              "parameters": [
                {
                  "constant": false,
                  "id": 413,
                  "name": "",
                  "nodeType": "VariableDeclaration",
                  "scope": 427,
                  "src": "5713:4:0",
                  "stateVariable": false,
                  "storageLocation": "default",
                  "typeDescriptions": {
                    "typeIdentifier": "t_bool",
                    "typeString": "bool"
                  },
                  "typeName": {
                    "id": 412,
                    "name": "bool",
                    "nodeType": "ElementaryTypeName",
                    "src": "5713:4:0",
                    "typeDescriptions": {
                      "typeIdentifier": "t_bool",
                      "typeString": "bool"
                    }
                  },
                  "value": null,
                  "visibility": "internal"
                }
              ],
              "src": "5712:6:0"
            },
            "scope": 428,
            "src": "5641:240:0",
            "stateMutability": "view",
            "superFunction": null,
            "visibility": "internal"
          }
        ],
        "scope": 429,
        "src": "1687:4196:0"
      }
    ],
    "src": "0:5883:0"
  },
  "compiler": {
    "name": "solc",
    "version": "0.4.24+commit.e67f0147.Emscripten.clang"
  },
  "networks": {
    "1": {
      "events": {},
      "links": {},
      "address": "0xcc1f223f6b4b3fffe9cb4794653b685eb99df355",
      "transactionHash": "0x516939a050c4769e51b610d911d7fbc12af5b2e2833d7bc71df072c3c39c7827"
    },
    "1532373672105": {
      "events": {},
      "links": {},
      "address": "0x8972f5e0717e2b623b6856e091c53aae3ff0ba3c",
      "transactionHash": "0x3143c2d9c269f9af423e3e155b0783589f87b852350a5957d2fe9b21acd092fe"
    },
    "1532412098212": {
      "events": {},
      "links": {},
      "address": "0x5f01b078691e2f32a00d2b35661855628d5689d0",
      "transactionHash": "0x20081770d51c42086962e9778854afbc485296de0b149c738dd8909e3a2d6b2f"
    }
  },
  "schemaVersion": "2.0.1",
  "updatedAt": "2018-07-24T06:55:18.425Z"
}
"""
