import os

from setuptools import setup

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

setup(
    name='AFCon',
    version='0.1',
    description='',
    author='Ricky Cook',
    author_email='mail@thatpanda.com',
    url='https://github.com/RickyCook/afcon',
    install_requires=open(
        '%s/requirements.txt' % (
            os.environ.get('OPENSHIFT_REPO_DIR', PROJECT_ROOT)
        )
    ).readlines(),
 )
