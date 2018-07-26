"""
"""

import sys
import requests
import jwt
import cryptography
import hashlib
import sha3
import json

import interact_contract

from web3.auto import w3
from eth_account.messages import defunct_hash_message

from requests.auth import HTTPBasicAuth
from flask import Flask, json, jsonify, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend

from deploy_contract import create_contract

app = Flask(__name__)
api = Api(app)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

authErrorNoToken = { "code" : "Missing bearer token."}
authErrorBadToken = { "code" : "Your token is not valid."}
authErrorExpiredToken = { "code" : "Your token has expired."}
authErrorNoBody = { "code" : "Missing payload."}
invalidJsonInBody = { "code" : "Invalid JSON in body"}
authErrorClaimNotSupport = { "code" : "The there's an unsupported claim in the list of claims to extract"}
missingSignature = { "code" : "Missing signature"}
mismatchAddressSignature = { "code" : "Address doesn't match with signature"}

res = requests.get('https://login.microsoftonline.com/common/.well-known/openid-configuration')
jwk_uri = res.json()['jwks_uri']
res = requests.get(jwk_uri)
jwk_keys = res.json()
publicKeyMap = {}

@app.route("/", methods=['GET'])
@cross_origin()
def index():
    return message_response(200, "Welcome to MSFT identities on the Ethereum Blockchain")

@app.route("/deploy", methods=['POST'])
def deploy_contract():
    contract = create_contract(contract_definition, contract_address)
    print('contract:{0}'.format(contract))
    return app.make_response(jsonify(contract))
    

@app.route("/check/<tenantid>/<useraddress>", methods=['GET'])
@cross_origin()
def check(tenantid, useraddress):
    ret_val = interact_contract.is_valid(tenantid, useraddress)
    return message_response(200, ret_val)



@app.route("/signup", methods=['POST'])
@app.route("/signup/<secret>", methods=['POST']) # for testing to skip certain step, look below
@cross_origin()
def signup(secret=None):    
    print ("before processing: url is: {0}".format(request.url), file=sys.stderr)
    if not request.data:
        return message_response(401, authErrorNoBody)

    try:
        json_string = json.loads(request.data)
    except ValueError:
        return message_response(401, invalidJsonInBody)
        
    print("Validating")
    json_string = json.loads(request.data)
    registrationReq = json_string["registration"]
    
    address = registrationReq["address"]
    print("Address: " + address)
    signature = json_string["signature"]
    
    if not signature:
        print("could not find signature from payload.")
        return message_response(400, missingSignature)

    verified_address = verify_address(registrationReq, signature)
    if verified_address != address:
        return message_response(400, mismatchAddressSignature)
    
    if not registrationReq or not registrationReq["token"]:
        return message_response(401, invalidJsonInBody)

    access_token = registrationReq["token"]
    print(access_token)
    
    if not access_token:
        return message_response(401, authErrorNoToken)

    token_header = jwt.get_unverified_header(access_token)
    x5c = None

    # Iterate JWK keys and extract matching x5c chain
    for key in jwk_keys['keys']:
        if key['kid'] == token_header['kid']:
            x5c = key['x5c']

    print ("x5c is {0}".format(x5c[0]))

    if x5c[0] not in publicKeyMap.keys():
        cert = ''.join(['-----BEGIN CERTIFICATE-----\n', x5c[0], '\n-----END CERTIFICATE-----\n',])
        public_key = load_pem_x509_certificate(cert.encode(), default_backend()).public_key()
        publicKeyMap[x5c[0]] = public_key
        print ("public key constructed")
    else:
        public_key = publicKeyMap[x5c[0]]
        print ("Cached public key is used")

    try:
        decoded_token = jwt.decode(
            access_token,
            public_key,
            verify=True if secret != 'test' else False, # for debug
            algorithms=token_header['alg'],
            audience="79d908c3-6cc1-40c6-bbf1-9f7140e927fb")
    except jwt.exceptions.ExpiredSignatureError:
        print("expired signature")
        return message_response(401, authErrorExpiredToken)
    except:
        print("bad token")
        return message_response(401, authErrorBadToken)

    claimSet = registrationReq["options"]["claims"]
    # ignore the claimSet for now until we support more claim types
    if not claimSet or len(claimSet) != 1 or claimSet[0] != "tid":
        print("claims in the claims to extract list are not supported")
        return message_response(400, authErrorClaimNotSupport)
    
    tenantId = decoded_token["tid"]
    userObjectId = decoded_token["oid"]
    issuedAtTicks = decoded_token["iat"]

    print (decoded_token)
    print(tenantId)
    print(userObjectId)
    print(address)
    print(issuedAtTicks)
    userHash = sha3.sha3_256((tenantId + "_" + userObjectId).encode('utf-8')).hexdigest()
    print("hash: " + userHash)

    txn = interact_contract.setTenant(userHash, address, issuedAtTicks, tenantId)
    
    hexdecimal = "".join(["{:02X}".format(b) for b in txn['hash']])
    txHash = "0x{}".format(hexdecimal)

    return message_response(200, {'transactionHash': txHash})
    # return message_response(200, "success")


def message_response(status_code, message):
    resp = app.make_response(json.jsonify({
        "message" : message
    }))
    resp.status = str(status_code)
    resp.content_type = "application/json"
    return resp


def verify_address(registrationReq, signature):
    message = json.dumps(registrationReq, sort_keys=True, separators=(',', ':'))
    print("message:" + message)
    message_hash = defunct_hash_message(text=message)
    print("message hash:" + str(message_hash))
    address = w3.eth.account.recoverHash(message_hash, signature=signature)
    print("address:" + address)
    return address


class Metadata(Resource):
    
    def get(self):
        resp = app.make_response(jsonify(''))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp


api.add_resource(Metadata, '/signup')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
