import subprocess
from time import sleep

from appium.webdriver.appium_service import AppiumService
from appium.webdriver.webdriver import WebDriver

from config.env import AppiumProps, AndroidCaps, PLATFORM
from appium import webdriver

appium_service = AppiumService()

_capabilities = {
    'IOS': {},

    'ANDROID': {
        'app': AndroidCaps.MOBILE_APP,
        'platformName': 'Android',
        'platformVersion': AndroidCaps.ANDROID_VERSION,
        'deviceName': AndroidCaps.ANDROID_DEVICE_NAME,
        'newCommandTimeout': AppiumProps.APPIUM_TIMEOUT,
        "automationName": "UiAutomator2",
        'autoGrantPermissions': True,
    },
}


def get_driver(no_reset: bool = True) -> WebDriver:
    """Create appium driver"""
    caps = _capabilities[PLATFORM]
    caps['noReset'] = no_reset

    return webdriver.Remote(
        command_executor=AppiumProps.APPIUM_SERVER,
        desired_capabilities=caps
    )