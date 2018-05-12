from flask_login import LoginManager, current_user
from werkzeug.exceptions import abort

from db.models import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(username):
    return User.query.filter(User.username == username).first()


def check_user_is_admin(func):
    def _check_user_is_admin(*args, **kwargs):
        if current_user.is_admin:
            return func(*args, **kwargs)
        else:
            return abort(403)
    return _check_user_is_admin
