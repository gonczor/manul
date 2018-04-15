import json

from flask import g, request
from flask_httpauth import HTTPBasicAuth
from flask_login import LoginManager

from db.models import User
from utils.password import check_user_password

login_manager = LoginManager()
auth = HTTPBasicAuth()


@login_manager.user_loader
def load_user(username):
    return User.query.get(username)


@auth.verify_password
def authenticate_user():
    data = json.loads(request.data)
    token = data.get('token')
    if token is not None:
        user = User.verify_token(token)
        g.user = user
        return user
    else:
        return check_user_password(data['username'], data['password'])
