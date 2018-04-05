import sys
import unittest

from flask import Flask
from flask_restful import Api

from app.settings import settings
from app.urls import register_urls as register_app_urls
from api.urls import register_urls as register_api_urls


def create_app():
    app = Flask(__name__)
    api = Api(app)
    register_app_urls(app)
    register_api_urls(api)
    return app


if __name__ == '__main__':
    rest_app = create_app()
    if 'test' not in sys.argv:
        rest_app.run(debug=settings['debug'], host=settings['host'])
    else:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner().run(suite)
