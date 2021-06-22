import unittest

import unittest
import json
from app import create_app
from main.models.user import db, User


class TestUser(unittest.TestCase):

    def set_up(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tear_down(self):
        self.app_context.pop()

    def test_get_user(self):
        # the test client can request a route
        response = self.app_context.get(
            '/user/%d' % self.user.id,
        )

        self.assertEqual(response.status_code, 200)
        user = json.loads(response.data.decode('utf-8'))
        self.assertEqual(user['email'], 'example@email.com')
