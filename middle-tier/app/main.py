"""
"""

import sys
import requests
import jwt
import cryptography
import hashlib

from web3.auto import w3
from eth_account.messages import defunct_hash_message

from requests.auth import HTTPBasicAuth
from flask import Flask, json, jsonify, request
from flask_restful import Resource, Api
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend

app = Flask(__name__)
api = Api(app)

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

@app.route("/")
def index():
    return "Welcome to MSFT identities on the Ethereum Blockchain"

@app.before_request
def before_request():
    
    print ("before processing: url is: {0}".format(request.url), file=sys.stderr)
    if not request.data:
        resp = app.make_response(jsonify(authErrorNoBody))
        resp.status = "401"
        resp.content_type = "application/json"
        return resp
    try:
        json_string = json.loads(request.data)
    except ValueError:
        resp = app.make_response(jsonify(invalidJsonInBody))
        resp.status = "401"
        resp.content_type = "application/json"
        return resp
    registrationReq = json_string["registration"]
    if not registrationReq or not registrationReq["token"]:
        resp = app.make_response(jsonify(invalidJsonInBody))
        resp.status = "401"
        resp.content_type = "application/json"
        return resp

    access_token = registrationReq["token"]
    print(access_token)
    
    if not access_token:
        resp = app.make_response(jsonify(authErrorNoToken))
        resp.status = "401"
        resp.content_type = "application/json"
        return resp

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
            # verify=False, # for debug
            algorithms=token_header['alg'],
            audience="79d908c3-6cc1-40c6-bbf1-9f7140e927fb")
    except jwt.exceptions.ExpiredSignatureError:
        print("expired signature")
        resp = app.make_response(jsonify(authErrorExpiredToken))
        resp.status = "401"
        resp.content_type = "application/json"
        return resp
    except:
        resp = app.make_response(jsonify(authErrorBadToken))
        print("bad token")
        resp.status = "401"
        resp.content_type = "application/json"
        return resp

    claimSet = registrationReq["options"]["claims"]
    # ignore the claimSet for now until we support more claim types
    if not claimSet or len(claimSet) != 1 or claimSet[0] != "tid":
        resp = app.make_response(jsonify(authErrorClaimNotSupport))
        print("claims in the claims to extract list are not supported")
        resp.status = "400"
        resp.content_type = "application/json"
        return resp
    
    tenantId = decoded_token["tid"]
    userObjectId = decoded_token["oid"]
    address = registrationReq["address"]
    issuedAtTicks = decoded_token["iat"]

    print (decoded_token)
    print(tenantId)
    print(userObjectId)
    print(address)
    print(issuedAtTicks)
    userHash = hashlib.sha256((tenantId + "_" + userObjectId).encode()).hexdigest()
    print("hash: " + userHash)

    signature = json_string["signature"]
    if not signature:
        resp = app.make_response(jsonify(missingSignature))
        print("could not find signature from payload.")
        resp.status = "400"
        resp.content_type = "application/json"
        return resp

    verified_address = verify_address(registrationReq, signature)
    if verified_address != address:
        resp = app.make_response(jsonify(mismatchAddressSignature))
        print("signature doesn't match address.")
        resp.status = "400"
        resp.content_type = "application/json"
        return resp

    resp = app.make_response("success")
    resp.status = "200"
    return resp

todos = {
    '1' : 'first_todo',
    '2' : 'second_todo',
    '3' : 'third_todo'
}

def verify_address(registrationReq, signature):
    message = json.dumps(registrationReq)
    print("message:" + message)
    message_hash = defunct_hash_message(text=message)
    print("message hash:" + str(message_hash))
    address = w3.eth.account.recoverHash(message_hash, signature=signature)
    print("address:" + address)
    return address


class Metadata(Resource):
    
    def get(self):
        resp = app.make_response(jsonify(sampleResponse))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp


class TodoSimple(Resource):
    
    def get(self, todo_id):
        return {todo_id: todos.get(todo_id)}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

    def delete(self, todo_id):
        if todos[todo_id] is not None:
            del todos[todo_id]
            return {}
        

api.add_resource(TodoSimple, '/todo/<string:todo_id>')
api.add_resource(Metadata, '/todo/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
