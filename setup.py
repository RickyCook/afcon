import os

from setuptools import setup

PROJECT_ROOT = os.environ.get('OPENSHIFT_REPO_DIR',
                              os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(PROJECT_ROOT, 'requirements.txt')) as file_:
    requirements = [req.strip() for req in file_]

setup(
    name='AFCon',
    version='0.1',
    description='',
    author='Ricky Cook',
    author_email='mail@thatpanda.com',
    url='https://github.com/RickyCook/afcon',
    install_requires=requirements,
 )
