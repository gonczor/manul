import datetime
import json

from flask import request
from flask_restful import Resource


class ServerTime(Resource):
    def get(self):
        time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        return {'time': time}


class Login(Resource):
    def post(self):
        login_data = json.loads(request.data)
        return login_data
