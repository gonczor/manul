from flask import g
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
def authenticate_user(token_or_username, password):
    user = User.verify_token(token_or_username)
    if user is None:
        return check_user_password(token_or_username, password)
    else:
        g.user = user
        return user
