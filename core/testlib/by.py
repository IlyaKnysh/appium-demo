from appium.webdriver.common.mobileby import MobileBy
from selene.support import by

__author__ = 'knysh'


def accessibility_id(_id: str) -> tuple:
    return MobileBy.ACCESSIBILITY_ID, _id


def id(_id: str) -> tuple:
    return MobileBy.ID, _id


def image(_image: str) -> tuple:
    return MobileBy.IMAGE, _image


def class_chain(_chain: str) -> tuple:
    return MobileBy.IOS_CLASS_CHAIN, _chain


def predicate(_predicate: str) -> tuple:
    return MobileBy.IOS_PREDICATE, _predicate


def link(_link: str) -> tuple:
    return MobileBy.LINK_TEXT, _link


def name(_name: str):
    return MobileBy.NAME, _name


def class_name(_class_name: str):
    return MobileBy.CLASS_NAME, _class_name


css = by.css
xpath = by.xpath
