import os

from selene import config as _selene_config

from . import env

__author__ = 'knysh'

_selene_config.timeout = int(env.get('UI_TIMEOUT', 10))


PLATFORM = env.get('PLATFORM', 'ANDROID')

APPIUM_TIMEOUT = int(env.get('APPIUM_TIMEOUT', 60))
APPIUM_PORT = env.get('APPIUM_PORT', 4725)

SYSTEM_PORT = env.get('SYSTEM_PORT', 8200)
APPIUM_SERVER = env.get('APPIUM_SERVER', 'http://localhost:{}/wd/hub'.format(APPIUM_PORT))

APP_NAME = {
    'IOS': env.get('IOS_APP_NAME', 'test_app.ipa'),
    'ANDROID': env.get('ANDROID_APP_NAME', 'test_app.apk')
}.get(PLATFORM)

MEDIA_PATH = env.get('MEDIA_PATH', str(os.path.join(os.path.dirname(os.path.abspath(__file__)), fr"app/media")))
_DEFAULT_APP_PATH = str(os.path.join(os.path.dirname(os.path.abspath(__file__)), fr"app/{APP_NAME}"))
MOBILE_APP = env.get('MOBILE_APP', _DEFAULT_APP_PATH)

APP_PACKAGE = env.get('APP_PACKAGE', 'camera.vuze.xr.release')
ANDROID_VERSION = env.get('ANDROID_VERSION', '9')
ANDROID_DEVICE_NAME = env.get('ANDROID_DEVICE_NAME', 'G6')

WDA_PORT = int(env.get('WDA_PORT', 8101))
IOS_VERSION = env.get('IOS_VERSION', '11.2.5')
IOS_DEVICE_NAME = env.get('IOS_DEVICE_NAME', 'iPhone 5S')
IOS_DEVICE_UDID = env.get('IOS_DEVICE_UDID', 'UDID')
X_CODE_TEAM_ID = env.get('X_CODE_TEAM_ID', 'TEAM_ID')
