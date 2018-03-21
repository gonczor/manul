import sys
import unittest

from flask import Flask
from flask_restful import Api

from api.views import HelloWorld
from urls import register_urls


def create_app():
    app = Flask(__name__)
    app = register_urls(app)
    api = Api(app)
    api.add_resource(HelloWorld, '/api/v1/hello')
    return                                                                                                              app


if __name__ == '__main__':
    rest_app = create_app()
    if 'test' not in sys.argv:
        rest_app.run(debug=True)
    else:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner().run(suite)
