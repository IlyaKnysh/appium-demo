from setuptools import setup, find_packages

__author__ = 'knysh'

PACKAGE_NAME = 'demo'
PACKAGE_VERSION = '0.1'
INSTALL_REQUIRES = [
    'selene==1.0.0a13',
    'Appium-Python-Client == 0.31',
    'pytest == 3.8.1',
    'allure-pytest',
    'allure-python-commons',
    'PyHamcrest == 1.9.0'
]
setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description=('Demo Test Suite for Android and iOS applications',),
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
)
