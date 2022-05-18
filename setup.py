from setuptools import setup, find_packages

PACKAGE_NAME = 'Demo'
PACKAGE_VERSION = '0.1'
INSTALL_REQUIRES = [
    'selene==2.0.0b2',
    'pytest',
    'allure-pytest',
    'PyHamcrest',
    'python-dotenv',
    'Faker',
    'addict',
    'Appium-Python-Client'
]
setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description=('Demo Test Project for appium',),
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES
)
