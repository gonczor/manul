import sys
import unittest

from flask import Flask
from flask_restful import Api

from api.urls import register_urls as register_api_urls
from core.urls import register_urls as register_app_urls
import core.auth

from commands import createsuperuser
from db import db
import setup


def create_app():
    # Hack to create auth
    # Create objects used in project
    app = Flask(__name__)
    app.config.update(SECRET_KEY=setup.secret_key)
    api = Api(app)

    # Register urls
    register_app_urls(app)
    register_api_urls(api)

    # Set up used objects
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manul.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    db.create_engine('sqlite:///manul.db')

    app.app_context().push()
    core.auth.login_manager.init_app(app)
    core.auth.login_manager.login_view = 'login'
    return app


if __name__ == '__main__':
    if 'test' in sys.argv:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner().run(suite)
    elif 'createdb' in sys.argv:
        rest_app = create_app()
        db.create_all()
    elif 'dropdb' in sys.argv:
        rest_app = create_app()
        db.drop_all()
    elif 'createsuperuser' in sys.argv:
        rest_app = create_app()
        createsuperuser.execute()
    else:
        rest_app = create_app()
        rest_app.run(debug=True)
