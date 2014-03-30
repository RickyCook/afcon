import unittest
from unittest.case import SkipTest

from afcon import app


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
        app.config['TESTING'] = True
        self.client = app.test_client()
