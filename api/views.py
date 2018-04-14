import datetime

from flask import g, jsonify
from flask_restful import Resource

from app.auth import auth


class ServerTime(Resource):
    def get(self):
        time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        return {'time': time}


class GetToken(Resource):
    @auth.login_required
    def post(self):
        token = g.user.generate_token()
        return jsonify({'token': token.decode('ascii')})


class TestLogin(Resource):
    @auth.login_required
    def get(self):
        return {'response': 'SUCCESS'}
