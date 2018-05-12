from itsdangerous import TimedJSONWebSignatureSerializer as TokenSerializer
from itsdangerous import (BadSignature, SignatureExpired)

from db import db
from setup import secret_key
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

    def generate_token(self, expiration_time=600):
        serializer = self._get_serializer(expiration_time)
        return serializer.dumps({'id': self.id})

    @classmethod
    def verify_token(cls, token):
        serializer = cls._get_serializer()
        try:
            data = serializer.loads(token)
        except BadSignature:
            return None
        except SignatureExpired:
            return None
        else:
            return cls.query.get(data['id'])

    @staticmethod
    def _get_serializer(expiration_time=None):
        """
        :param expiration_time: optional argument indicating expiration time. used with generate_token()
        :return (TimedJSONWebSignatureSerializer):
        """
        return TokenSerializer(secret_key, expires_in=expiration_time)
