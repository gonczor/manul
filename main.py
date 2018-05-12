import sys
import unittest

from flask import Flask
from flask_restful import Api

from api.urls import register_urls as register_api_urls
from core.urls import register_urls as register_app_urls

from commands import createsuperuser
from db import db
import setup


def create_app():
    # Hack to create auth
    import core.auth  # flake8: noqa
    # Create objects used in project
    app = Flask(__name__)
    app.config.update(SECRET_KEY=setup.secret_key)
    api = Api(app)

    # Register urls
    register_app_urls(app)
    register_api_urls(api)

    # Set up used objects
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manul.db'
    db.init_app(app)
    db.create_engine('sqlite:///manul.db')

    app.app_context().push()
    core.auth.login_manager.init_app(app)
    core.auth.login_manager.login_view = 'login'
    return app


if __name__ == '__main__':
    rest_app = create_app()
    if 'test' in sys.argv:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner().run(suite)
    elif 'createdb' in sys.argv:
        db.create_all()
    elif 'dropdb' in sys.argv:
        db.drop_all()
    elif 'createsuperuser' in sys.argv:
        createsuperuser.execute()
    else:
        rest_app.run(debug=True)
