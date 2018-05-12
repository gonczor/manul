import json

from flask import request
from flask_httpauth import HTTPBasicAuth

from db.models import User
from utils.password import check_user_password

auth = HTTPBasicAuth()


@auth.verify_password
def authenticate_user(*_):
    data = json.loads(request.data)
    token = data.get('token')
    if token is not None:
        user = User.verify_token(token)
        return user
    else:
        return check_user_password(data['username'], data['password'])
