from unittest import TestCase

import main
from db import db


class BaseTestCase(TestCase):
    def setUp(self):
        app = main.create_app(test=True)
        app.testing = True
        app.app_context = app.test_request_context()
        app.app_context.push()
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.drop_all()
