import allure
import pytest
from selene.support.shared import browser

from core.testlib import driver as driver_setup
from core.testlib.driver import appium_service
from core.testlib.logger import LOGGER


@pytest.fixture(scope='session', autouse=True)
def create_appium_server():
    appium_service.start()

    yield

    appium_service.stop()


@pytest.fixture(scope='function', autouse=True)
def driver():
    ui_driver = driver_setup.get_driver()
    browser.config.driver = ui_driver

    yield ui_driver

    ui_driver.quit()


def pytest_exception_interact(node, call, report):
    """Attach screenshot if test failed"""
    if report.failed:
        try:
            with open(browser.config.last_screenshot, 'rb') as screen:
                allure.attach(screen.read(), 'screen', allure.attachment_type.PNG)
        except TypeError:
            LOGGER.info('No screenshots for the issue')
