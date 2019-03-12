from appium.webdriver.common.mobileby import MobileBy
from selene.support import by

__author__ = 'knysh'


def accessibility_id(_id):
    return MobileBy.ACCESSIBILITY_ID, _id


def id(_id):
    return MobileBy.ID, _id


def image(_image):
    return MobileBy.IMAGE, _image


def class_chain(_chain):
    return MobileBy.IOS_CLASS_CHAIN, _chain


def predicate(_predicate):
    return MobileBy.IOS_PREDICATE, _predicate


def link(_link):
    return MobileBy.LINK_TEXT, _link


def name(_name):
    return MobileBy.NAME, _name


def class_name(_class_name):
    return MobileBy.CLASS_NAME, _class_name


css = by.css
xpath = by.xpath
