import unittest

from flask import testing

from afcon.tests.util import FlaskTestMixin, requires_database


class TestUserList(FlaskTestMixin, unittest.TestCase):
    """
    Test the misc functions of the UsersList resource
    """
    def test_list_not_allowed(self):
        """
        Listing of users should give a 405
        """
        res = self.client.get('/users/')
        self.assertEqual(res[1], '405 METHOD NOT ALLOWED')