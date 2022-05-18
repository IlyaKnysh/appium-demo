from faker import Faker
from selene.core.entity import Element, Collection
from selene.support.shared import browser

from config.env import PLATFORM

FAKE = Faker()


def get_random_str(n: int = 5) -> int:
    return FAKE.bothify(text='?' * n)


def get_random_int(min_value: int = 0, max_value: int = 9999) -> int:
    return FAKE.pyint(min_value, max_value)


def locator_for_platform(selectors):
    return selectors.get(PLATFORM, 'Undefined Selector')


def element(selectors: dict) -> Element:
    return browser.element(locator_for_platform(selectors))


def elements(selectors: dict) -> Collection:
    return browser.elements(locator_for_platform(selectors))
