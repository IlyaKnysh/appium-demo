import os
import shutil

import allure
import pytest
from selene import factory

from config.driver_config import PLATFORM
from config.env import SCREEN_PATH, TEST_REPORTS_DIR
from testlib import driver as driver_setup
from testlib.utils import update_media
from testlib.steps.main_steps import MainSteps

__author__ = 'knysh'


@pytest.fixture(autouse=True)
def report_dir():
    """Create directory for reports"""
    shutil.rmtree(TEST_REPORTS_DIR, ignore_errors=True)
    shutil.rmtree(os.path.join(TEST_REPORTS_DIR, 'screenshots'), ignore_errors=True)
    os.makedirs(TEST_REPORTS_DIR)

    return TEST_REPORTS_DIR


@pytest.yield_fixture(scope='session', autouse=True)
def create_appium_server():
    driver_setup.start_appium_server()

    yield

    driver_setup.close_appium_server()


@pytest.yield_fixture(scope='function', autouse=True)
def driver(request):
    if hasattr(request, 'param') and request.param.get('noReset') is False:
        """Transfer capability from test parameters"""
        no_reset = request.param.get('noReset')
        ui_driver = driver_setup.get_driver(no_reset)
        factory.set_shared_driver(ui_driver)
        update_media()
    else:
        ui_driver = driver_setup.get_driver()
        factory.set_shared_driver(ui_driver)

    yield ui_driver

    ui_driver.quit()


def pytest_exception_interact(node, call, report):
    """Attach screenshot if test failed"""
    if report.failed:
        node.funcargs['driver'].save_screenshot(SCREEN_PATH)
        with open(SCREEN_PATH, 'rb') as screen:
            allure.attach(screen.read(), 'screen', allure.attachment_type.PNG)


def pytest_runtest_call(item):
    """Execute some actions before test by mark"""
    if PLATFORM == 'ANDROID' and 'camera' in [mark.name for mark in item.own_markers]:
        steps = MainSteps()
        steps.open_camera_dashboard()
