from . import db
from utils.password import hash_password


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    @classmethod
    def create_user(cls, username, password, is_admin=False):
        return cls(
            username=username,
            password=hash_password(password),
            is_admin=is_admin
        )
