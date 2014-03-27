import unittest
from unittest.case import SkipTest

from flask.testing import FlaskClient

from afcon import app


RETURN_CODE = {
    403: '403 UNAUTHORIZED',
    405: '405 METHOD NOT ALLOWED',
}

def requires_database(func):
    """
    Decorator to skip tests that require a database
    """
    def decorated(*args, **kwargs):
        # TODO don't skip all tests
        # Create new database
        # Migrate to current schema version
        raise SkipTest("Database required")
        return func(*args, **kwargs)

    return decorated


class FlaskTestMixin(object):
    """
    Base test case for Flask tests
    """
    def setUp(self):
        self.client = FlaskClient(app)
