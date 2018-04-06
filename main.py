import sys
import unittest

from flask import Flask
from flask_restful import Api

from app.urls import register_urls as register_app_urls
from api.urls import register_urls as register_api_urls
from db import db

from helpers import createsuperuser


def create_app():
    app = Flask(__name__)
    api = Api(app)
    register_app_urls(app)
    register_api_urls(api)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manul.db'
    db.init_app(app)
    db.create_engine('sqlite:///manul.db')
    app.app_context().push()
    return app


if __name__ == '__main__':
    rest_app = create_app()
    if 'test' in sys.argv:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner().run(suite)
    elif 'createdb' in sys.argv:
        db.create_all()
    elif 'createsuperuser' in sys.argv:
        createsuperuser.execute()
    else:
        rest_app.run(debug=True)
