import inspect

import allure
from hamcrest import assert_that
from hamcrest.core.matcher import Matcher
from selene.conditions import exist
from selene.wait import wait_for
from selenium.common.exceptions import TimeoutException

from testlib.utils import repeat_check, format_exception

__author__ = 'knysh'


def check_that(actual, matcher, message='', prestep=None, timeout=None, repeat=None):
    """Wrapper over 'assert_that' to add step in allure report."""
    with allure.step("Check that " + message):
        if inspect.ismethod(actual):
            """Execute check with selene conditions"""
            repeat_check(actual, matcher, timeout=timeout, prestep=prestep, repeat=repeat)
        else:
            try:
                """Execute regular check"""
                if isinstance(matcher, Matcher):
                    assert_that(actual, matcher, message)
                else:
                    assert_that(actual, matcher)
            except AssertionError as e:
                e.args = format_exception(e)  # format regex for repr
                raise e


def is_element_exist(element, timeout=0):
    try:
        wait_for(element, exist, timeout=timeout)
        return True
    except TimeoutException:
        return False
