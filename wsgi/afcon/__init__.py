import logging

from afcon import settings


logging.basicConfig(**settings.LOGGING_CONFIG)
LOGGER = logging.getLogger()

if settings.GEAR_UUID:
    logger.info('Running on OpenShift')