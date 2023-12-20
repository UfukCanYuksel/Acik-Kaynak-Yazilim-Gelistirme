from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pandas as pd
import requests

app = Flask(__name__)
api = Api(app)

class GetAllData(Resource):
    def get(self):

        url = 'https://cat-fact.herokuapp.com/facts'

        resp = requests.get(url)
        data = resp.json()


        return {'data': data}, 200

api.add_resource(GetAllData, '/facts')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
    app.run()
