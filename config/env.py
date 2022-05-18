import os

from selene import config as _selene_config
from dotenv import load_dotenv

load_dotenv()  # load sys vars from .env file


def get(key: str, default: any = None) -> str:
    return os.environ.get(key=key, default=default)


PROJECT_DIRECTORY = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEST_REPORTS_DIR = os.environ.get("TEST_REPORTS_DIR", os.path.join(PROJECT_DIRECTORY, "tests/screenshots"))
SCREEN_PATH = os.path.join(TEST_REPORTS_DIR,
                           "screen_{}.png".format(str(_selene_config.counter)).replace('count(', '').replace(')', ''))

PLATFORM = get('PLATFORM', 'ANDROID')

_APP_NAME = {
    'IOS': get('IOS_APP_NAME', 'test_app.ipa'),
    'ANDROID': get('ANDROID_APP_NAME', 'test_app.apk')
}.get(PLATFORM)
_DEFAULT_APP_PATH = str(os.path.join(PROJECT_DIRECTORY, f"resources/app/{_APP_NAME}"))


class AndroidCaps:
    ANDROID_VERSION = get('ANDROID_VERSION', '11')
    ANDROID_DEVICE_NAME = get('ANDROID_DEVICE_NAME', 's10e')
    MOBILE_APP = get('MOBILE_APP', _DEFAULT_APP_PATH)


class AppiumProps:
    APPIUM_TIMEOUT = int(get('APPIUM_TIMEOUT', 60))
    APPIUM_SERVER = get('APPIUM_SERVER', f'http://localhost:4723/wd/hub')
