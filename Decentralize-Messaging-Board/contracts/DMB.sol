pragma solidity ^0.4.24;

import "zeppelin-solidity/contracts/token/ERC721/ERC721Token.sol";
import "zeppelin-solidity/contracts/math/SafeMath.sol";
import "./lib/strings.sol";
// References: https://github.com/OpenZeppelin/openzeppelin-solidity/blob/v1.8.0/contracts/token/ERC721/ERC721Token.sol

contract DMB is ERC721Token ("DecentralizeMessagingBoard", "DMB") {
    using strings for *;
    using SafeMath for uint256;

    // These two are included in the open lib
    string internal name_ = "DecentralizeMessagingBoard";
    string internal symbol_ = "DMB";

    uint256 public erc721TokenId = 1; // default tokenId for helping people to create unique id
    mapping (uint256 => uint256) postIdTenantIdMap; //a map to trace postId => tenantId
    //hack mapping for address to tenantId
    mapping (address => uint256) addrTenantId;
    mapping (uint256 => string) tenantIdAffiliation;
    modifier isValid {
        require(true); //calling isValid  functino from Authenticator app
        _;
    }

    // constructor
    function DMB() public { 
        //Do some initialization
    }

    // Function to issue certificate to a receiver
    // _uri  : The string for the content of the post
    // names  : The names of the signers (is ';' delimetered string)
    function createNewPost(string _uri) isValid public {
        //New generated token Id
        uint256 newTokenId = erc721TokenId++;
        super._mint(msg.sender, newTokenId);
        super._setTokenURI(newTokenId, _uri);
        uint256 tenantId = addrTenantId[msg.sender]; //get it from the IdentityContract
        require(tenantId > 0);
        postIdTenantIdMap[newTokenId] = tenantId;        
    }

    //hack function to set the tenantId you want for the post
    function setTenantId(uint256 id, string affiliation) public{
        addrTenantId[msg.sender] = id;
        tenantIdAffiliation[id] = affiliation;
    }

    function getTokenTenantId(uint256 tokenId) public view returns(uint256){
        return postIdTenantIdMap[tokenId];
    }

    function getPostAuthorAffiliation(uint256 tokenId) public view returns(string){
        return tenantIdAffiliation[tokenId];
    }

}