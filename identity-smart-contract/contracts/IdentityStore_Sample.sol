pragma solidity ^0.4.24;


/**
 * @title Ownable
 * @dev The Ownable contract has an owner address, and provides basic authorization control
 * functions, this simplifies the implementation of "user permissions".
 */
contract Ownable {
  address public owner;


  event OwnershipRenounced(address indexed previousOwner);
  event OwnershipTransferred(
    address indexed previousOwner,
    address indexed newOwner
  );


  /**
   * @dev The Ownable constructor sets the original `owner` of the contract to the sender
   * account.
   */
  constructor() public {
    owner = msg.sender;
  }

  /**
   * @dev Throws if called by any account other than the owner.
   */
  modifier onlyOwner() {
    require(msg.sender == owner);
    _;
  }

  /**
   * @dev Allows the current owner to relinquish control of the contract.
   * @notice Renouncing to ownership will leave the contract without an owner.
   * It will not be possible to call the functions with the `onlyOwner`
   * modifier anymore.
   */
  function renounceOwnership() public onlyOwner {
    emit OwnershipRenounced(owner);
    owner = address(0);
  }

  /**
   * @dev Allows the current owner to transfer control of the contract to a newOwner.
   * @param _newOwner The address to transfer ownership to.
   */
  function transferOwnership(address _newOwner) public onlyOwner {
    _transferOwnership(_newOwner);
  }

  /**
   * @dev Transfers control of the contract to a newOwner.
   * @param _newOwner The address to transfer ownership to.
   */
  function _transferOwnership(address _newOwner) internal {
    require(_newOwner != address(0));
    emit OwnershipTransferred(owner, _newOwner);
    owner = _newOwner;
  }
}

contract IdentityStore is Ownable {
  
    struct User {
        bytes32 tenantHash;
        uint256 timestamp;
    }

    mapping(address => User) private tenantAddressMapping;
    mapping(bytes32 => address) private tenantHashMapping; 

    function setTenant(
        bytes32 _tenantHash,
        address _userAddress,
        uint256 _timestamp) onlyOwner public {

        require(!userAddressExists(_userAddress));
        require(!userTenantHashExists(_tenantHash));

        User memory newUser = User(_tenantHash, _timestamp);
        
        tenantAddressMapping[_userAddress] = newUser;
        tenantHashMapping[_tenantHash] = _userAddress;
    }

    function updateHash(
        bytes32 _oldHash, 
        bytes32 _newHash, 
        uint256 _timestamp) onlyOwner public {

        require(userTenantHashExists(_oldHash), "Old hash does not exist.");
        require(!userTenantHashExists(_newHash), "New hash is already registered.");
        address currentAddress = tenantHashMapping[_oldHash];
        User memory newUserInfo = User(_newHash, _timestamp);

        // update address mapping to user
        tenantAddressMapping[currentAddress] = newUserInfo;

        // delete old hash mapping to address
        delete tenantHashMapping[_oldHash];

        // add new hash mapping to address
        tenantHashMapping[_newHash] = currentAddress;
    }


    function userAddressExists(address userAddress) view public returns(bool) {       
        if(tenantAddressMapping[userAddress].timestamp == 0) {
            return false;
        }
        return true;
    }

    function userTenantHashExists(bytes32 tenantHash) view public returns(bool){
        if(tenantHashMapping[tenantHash] == 0) {
            return false;
        }
        return true;
    }

    function updateAddress (address oldUserAddress, address newUserAddress) public {
        User memory existingUser = tenantAddressMapping[oldUserAddress];
        
        require(!userAddressExists(newUserAddress));
        require(userAddressExists(oldUserAddress));

        tenantHashMapping[existingUser.tenantHash] = newUserAddress;
        tenantAddressMapping[newUserAddress] = existingUser;
        delete tenantAddressMapping[oldUserAddress];
    }


}