from flask import url_for
from flask.ext.login import current_user

from utils.tests import BaseTestCase
from db import db
from db.models import User


class LoginViewTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.username = 'user'
        self.password = 'pass'
        self.user = User(username=self.username, password=self.password)
        self.admin_username = 'admin'
        self.admin_password = 'admin_pass'
        self.admin = User(username=self.admin_username, password=self.admin_password, is_admin=True)
        db.session.add(self.user)
        db.session.add(self.admin)
        db.session.commit()

    def test_admin_can_log_in(self):
        """When user makes POST with correct credentials, he should get logged in."""
        with self.client:
            response = self.client.post(
                url_for('login'), data={'username': self.admin_username, 'password': self.admin_password}
            )
            self.assertEqual(response.status_code, 302)
            self.assertEqual(current_user, self.admin)

    def test_login_with_invalid_credentials(self):
        """When posting wrong credentials user should not be logged in."""
        response = self.client.post(
            url_for('login'), data={'username': self.admin_username, 'password': '1234'}
        )
        self.assertEqual(response.status_code, 401)

    def test_login_with_get_method(self):
        """Posting data with GET should be ignored and login form should be displayed"""
        response = self.client.get(
            url_for('login'), data={'username': self.admin_username, 'password': self.admin_password}
        )
        self.assertEqual(response.status_code, 200)

    def test_non_admin_does_not_have_access_to_admin_panel(self):
        """Authorized user who does not have is_admin set to True should not be able to gain access to admin panel."""
        with self.client:
            self.client.post(
                url_for('login'), data={'username': self.username, 'password': self.password}
            )
            response = self.client.get(url_for('admin_panel'))
            self.assertEqual(response.status_code, 403)
            self.assertEqual(current_user, self.user)
