from setuptools import setup, find_packages

setup(
    name='socketutils',
    version='0.0.1',
    packages=find_packages(exclude=['tests']),
    author='sergeyB',
    description='Wrapper for python sockets',
)
