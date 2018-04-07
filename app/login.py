from flask_login import LoginManager

from db.models import User


login_manager = LoginManager()


@login_manager.user_loader
def load_user(username):
    return User.query.get(username)
