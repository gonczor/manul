from unittest import TestCase

from db import db


class BaseTestCase(TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()
