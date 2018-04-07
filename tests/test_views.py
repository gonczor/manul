from main import create_app
from utils.tests import BaseTestCase


class TestCaseViews(BaseTestCase):
    def setUp(self):
        super().setUp()
        app = create_app()
        app.testing = True
        self.client = app.test_client()

    def test_hello_world(self):
        response = self.client.get('/')
        self.assertIsNotNone(response)
