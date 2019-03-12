from appium.webdriver.common.touch_action import TouchAction
from selene import factory
from selene.conditions import visible, clickable
from selene.wait import wait_for
from selenium.common.exceptions import TimeoutException

from config.driver_config import PLATFORM

__author__ = 'knysh'


def tap_and_hold(element, duration=2000):
    wait_for(element, clickable)
    actions = TouchAction(factory.get_shared_driver())
    actions.long_press(element, duration=duration).wait(1000).release().perform()


def scroll(el=None, move_to_element=None, from_x=None, from_y=None, to_x=None, to_y=None):
    actions = TouchAction(factory.get_shared_driver())
    actions.press(el=el, x=from_x, y=from_y).wait().move_to(el=move_to_element, x=to_x, y=to_y).release().perform()


def collect_elements(elements, move_to_element):
    """Collect elements using scroll"""
    try:
        elements[0].should(visible)
        elements_list = elements()
        counter = 0
        last_element = None
        last_iter_element = elements()[-1]

        if PLATFORM == 'IOS':
            """Implemented for elements UID search"""
            while last_element != last_iter_element and counter < 5:
                scroll(el=last_iter_element, move_to_element=move_to_element)
                new_elements_list = elements()
                total_elements_set = set(elements_list + new_elements_list)
                if len(set(elements_list)) == len(total_elements_set):
                    break
                else:
                    elements_list = list(total_elements_set)
                    last_element = last_iter_element
                    counter += 1

        elif PLATFORM == 'ANDROID':
            """Android has not UID's, so tests should be designed to avoid search without unique identifiers
            (E.G. set auto ID's or check elements refreshing by inner content)
            """
            elements_list = elements()

        return elements_list

    except TimeoutException:
        return []


def search_element_via_scroll(element, scroll_from_el=None, scroll_to_el=None, from_x=None, from_y=None, to_x=None,
                              to_y=None, collection=None, repeat=5):
    """Find element in collection using scroll"""
    counter = 0
    last_element = None
    if collection:
        last_element = collection()[-1]
    while True:
        try:
            wait_for(element, visible, timeout=0)
            return element
        except TimeoutException:
            scroll(el=scroll_from_el, move_to_element=scroll_to_el, from_x=from_x, from_y=from_y, to_x=to_x, to_y=to_y)
            if (last_element == collection()[-1] if collection else None) or counter == repeat:
                break
            if collection:
                last_element = collection()[-1]
            counter += 1
    raise AssertionError(f'Element by {element._locator.description} not found')
