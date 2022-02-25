import json
from mgz.model import parse_match, serialize
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
app = Flask(__name__)
api = Api(app)


class test(Resource):
    def get(self):
        with open('C:/Users/maxim/Games/Age of Empires 2 DE/76561199234805699/savegame/MP Replay v101.101.56005.0 @2022.01.14 162123 (1).aoe2record', 'rb') as h:
            match = parse_match(h)
            print('test')
        return {'data': 'salut'}, 200


class Analyse(Resource):
    def get(self):
        with open('C:/Users/maxim/Games/Age of Empires 2 DE/76561199234805699/savegame/MP Replay v101.101.56005.0 @2022.01.14 162123 (1).aoe2record', 'rb') as h:
            match = parse_match(h)
            print('test')
        return {'data': 'salut'}, 200


api.add_resource(Analyse, '/test')
if __name__ == '__main__':
    app.run()  # run our Flask app
