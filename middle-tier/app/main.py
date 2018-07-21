"""
"""

import sys
import requests
import jwt
import cryptography

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
    
    print ("before processing: url is: {0}".format(request.url))
    
    if "Authorization" not in request.headers:
        resp = app.make_response(jsonify(authErrorNoToken))
        resp.status = "401"
        resp.content_type = "application/json"
        return resp
    
    authHeader = request.headers['Authorization']
    
    if authHeader.startswith('Bearer '):
        access_token = authHeader[7:]
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
                algorithms=token_header['alg'],
                audience="https://graph.windows.net")
        except jwt.exceptions.ExpiredSignatureError:
            resp = app.make_response(jsonify(authErrorExpiredToken))
            resp.status = "401"
            resp.content_type = "application/json"
            return resp
        except:
            resp = app.make_response(jsonify(authErrorBadToken))
            resp.status = "401"
            resp.content_type = "application/json"
            return resp

        print (decoded_token)


todos = {
    '1' : 'first_todo',
    '2' : 'second_todo',
    '3' : 'third_todo'
}


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
