import subprocess
from time import sleep

from appium import webdriver as appium_driver

import config

__author__ = 'knysh'

_capabilities = {
    'IOS': {
        'platformName': 'iOS',
        'platformVersion': config.driver_config.IOS_VERSION,
        'deviceName': config.driver_config.IOS_DEVICE_NAME,
        'app': config.driver_config.MOBILE_APP,
        'newCommandTimeout': config.driver_config.APPIUM_TIMEOUT,
        'xcodeOrgId': config.driver_config.X_CODE_TEAM_ID,
        'xcodeSigningId': 'iPhone Developer',
        'udid': config.driver_config.IOS_DEVICE_UDID,
        'wdaLocalPort': config.driver_config.WDA_PORT,
        'fullReset': False,
    },

    'ANDROID': {
        'app': config.driver_config.MOBILE_APP,
        'platformName': 'Android',
        'platformVersion': config.driver_config.ANDROID_VERSION,
        'deviceName': config.driver_config.ANDROID_DEVICE_NAME,
        'newCommandTimeout': config.driver_config.APPIUM_TIMEOUT,
        'systemPort': config.driver_config.SYSTEM_PORT,
        "automationName": "UiAutomator2",
        "browserName": "",
        "unlockType": "password",
        "unlockKey": "4444",
        'autoGrantPermissions': True,
    },
}


def get_driver(no_reset=True):
    """Create appium driver"""
    caps = _capabilities[config.driver_config.PLATFORM]
    caps['noReset'] = no_reset

    return appium_driver.Remote(
        command_executor=config.driver_config.APPIUM_SERVER,
        desired_capabilities=caps
    )


def start_appium_server():
    count = 0
    if subprocess.call(f'netstat -anl|grep LISTEN|grep "*.{config.driver_config.APPIUM_PORT}"',
                       shell=True):
        """Start appium server if it's not started yet"""
        subprocess.Popen(['appium', '-p', f'{config.driver_config.APPIUM_PORT}'])
        print('Started appium server...')

    while count < 5:
        """Wait for appium server start"""

        if subprocess.call(f'netstat -anl|grep LISTEN|grep "*.{config.driver_config.APPIUM_PORT}"', shell=True):
            print('...check if appium server is ready...')
            sleep(1)
            count += 1

        else:
            print('...appium server ready')
            break


def close_appium_server():
    subprocess.call(f'kill $(lsof -t -i:{config.driver_config.APPIUM_PORT})', shell=True)  # kill appium
    subprocess.call(f'kill $(lsof -t -i:{config.driver_config.WDA_PORT})', shell=True)  # kill WDA
    subprocess.call(f'kill $(lsof -t -i:{config.driver_config.SYSTEM_PORT})', shell=True)  # kill UiAutomator2
