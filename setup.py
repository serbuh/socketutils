from setuptools import setup, find_packages

setup(
    name='socketutils',
    version='0.0.4',
    packages=find_packages(exclude=['tests']),
    author='sergeyB',
    description='Wrapper for python sockets',
)
