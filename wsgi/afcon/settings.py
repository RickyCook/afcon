import logging

GEAR_UUID = getattr(os.environ, 'OPENSHIFT_GEAR_UUID', None)
IS_OPENSHIFT = GEAR_UUID is not None

DB_CONNECTION = getattr(os.environ,
                        'OPENSHIFT_POSTGRESQL_DB_URL',
                        'sqlite:///afcon.db',
                        )

LOGGING_CONFIG = {
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
}
if IS_OPENSHIFT:
    LOGGING_CONFIG['level'] = logging.INFO
else:
    LOGGING_CONFIG['level'] = logging.DEBUG