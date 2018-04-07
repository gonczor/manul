from db import db
from utils.password import hash_password


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=True)

    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = hash_password(password)
        self.is_admin = is_admin

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username
