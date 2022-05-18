from __future__ import annotations

import time

import allure
from hamcrest import assert_that
from hamcrest.core.matcher import Matcher


def check_that(actual: any, matcher: Matcher | str = None, message: str = 'message', timeout: int = 10,
               polling: float = 0.1) -> None:
    """
    This function will wrap all assertions with a 'Check that ' in allure report as a step
    It's possible to use it both for immediate assertions - check_that(element.text, equal_to(1), 'Text is 1')
    and for assertions with retrier - check_that(lambda: element.text, equal_to(1), 'Text is 1')
    """
    __tracebackhide__ = True
    if not isinstance(matcher, Matcher) and not message:
        message = matcher  # to make possible following impl - check_that(element.is_displayed(), 'Button is shown')
    with allure.step("Check that " + message):
        if callable(actual):
            _assertion_retry(actual, matcher, message, timeout, polling)
        else:
            assert_that(actual, matcher, message)


def _assertion_retry(actual: any, matcher: Matcher | str = None, message: str = None, timeout: int = 10,
                     polling: float = 0.1) -> None:
    end_time = time.time() + timeout
    exception = None
    while time.time() < end_time:
        try:
            assert_that(actual(), matcher, message)
            return
        except Exception as ex:
            exception = ex
            time.sleep(polling)

    raise AssertionError(message, str(exception))


def check_that_periodically(actual: any, matcher: Matcher | str = None, message: str = None, timeout: int = 10,
                            polling: float = 0.1) -> None:
    """
    Function will check some assertion during some period of time
    """
    __tracebackhide__ = True
    end_time = time.time() + timeout
    with allure.step("Check periodically that " + message):
        while time.time() < end_time:
            check_that(actual, matcher, message)
            time.sleep(polling)
