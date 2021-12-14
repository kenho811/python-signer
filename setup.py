from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='eosio_signer',
    version=os.getenv('BUILD_VERSION', 'develop'),
    description='Python library for EOSIO signing',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='',
    author_email='',
    url='https://github.com/b1-as/py-eosio-signer',
    packages=find_packages(),
    test_suite='pytest',
    install_requires=[
        'base58>=1.0.3',
        'ecdsa',
    ]
)
