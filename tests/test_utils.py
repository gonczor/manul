from utils.tests import BaseTestCase
from utils.password import check_user_password
from db import db
from db.models import User


class PasswordCheckTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.username = 'user'
        self.password = 'pass'
        self.user = User.create_user(
            username=self.username,
            password=self.password
        )
        db.session.add(self.user)
        db.session.commit()

    def test_password_match(self):
        self.assertTrue(check_user_password(self.username, self.password))

    def test_password_not_match(self):
        self.assertFalse(check_user_password(self.username, 'not a password'))

    def test_for_not_existing_user(self):
        self.assertFalse(check_user_password('not a user', self.password))
