import os
import sys
import tempfile
import unittest
from unittest.case import SkipTest

import sqlalchemy
from sqlalchemy.exc import ProgrammingError

from afcon import app

def _db_uri_parts():
        """
        Split the DB URI
        """
        return app.config['SQLALCHEMY_DATABASE_URI'].split('/')

def db_uri_for(db_name):
    """
    Get a DB URI for the current sever with the given database
    """
    return '/'.join(_db_uri_parts()[:-1] + [db_name])

def _create_db(db_name):
        """
        Create a new database
        """
        template_conn.execute('commit')
        template_conn.execute('create database {}'.format(db_name))

def _drop_db(db_name):
    """
    Drop a database
    """
    template_conn.execute('commit')
    try:
        template_conn.execute('drop database {}'.format(db_name))
    except ProgrammingError as e:
        pass

def reset_db():
    _drop_db('afcon_test')
    _create_db('afcon_test')

engine = sqlalchemy.create_engine(db_uri_for('template1'))
template_conn = engine.connect()

def requires_database(func):
    """
    Decorator to skip tests that require a database
    """
    def decorated(*args, **kwargs):
        if template_conn.closed:
            raise SkipTest("Database connection closed")

        original_db_uri = app.config['SQLALCHEMY_DATABASE_URI']
        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri_for('afcon_test')

        try:
            reset_db()
        except ProgrammingError as e:
            raise SkipTest("Database could not be created")

        # Avoid circular reference
        from afcon.manager import manager
        manager.handle(sys.argv[0], ['db', 'upgrade'])

        rv = func(*args, **kwargs)

        # Reset DB URI
        app.config['SQLALCHEMY_DATABASE_URI'] = original_db_uri

        return rv

    return decorated


class FlaskTestMixin(object):
    """
    Base test case for Flask tests
    """
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
