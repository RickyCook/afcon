import unittest

from flask import testing

from afcon.tests.util import FlaskTestMixin, requires_database


class TestGetUser(FlaskTestMixin, unittest.TestCase):
    """
    Test display of a user
    """
    @requires_database
    def test_correct(self):
        """
        Make sure that listing a single user works as expected
        """
        # TODO Setup the user mail@pand.as
        # TODO Login as user mail@pand.as
        res = self.client.get('/users/mail@pand.as')
        # TODO Validate user

    @requires_database
    def test_guest_unauth(self):
        """
        Make sure that guest listing a single user is 403
        """
        # TODO Setup the user mail@pand.as
        res = self.client.get('/users/mail@pand.as')
        self.assertEqual(res.status_code, 403)

    @requires_database
    def test_user_unauth(self):
        """
        Make sure that guest listing a single user is 403
        """
        # TODO Setup the user mail@pand.as
        # TODO Setup the user mail@dog.es
        # TODO Login as user mail@pand.as
        res = self.client.get('/users/mail@dog.es')
        self.assertEqual(res.status_code, 403)

    @requires_database
    def test_no_user(self):
        """
        Make sure that we DON'T 404, which leaks info
        """
        res = self.client.get('/users/no@such.user')
        self.assertEqual(res.status_code, 403)


class TestUserList(FlaskTestMixin, unittest.TestCase):
    """
    Test the misc functions of the UsersList resource
    """
    def test_list_not_allowed(self):
        """
        Listing of users should give a 405
        """
        res = self.client.get('/users/')
        self.assertEqual(res.status_code, 405)
