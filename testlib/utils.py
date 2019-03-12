import subprocess

from hamcrest import matches_regexp
from selene.support.jquery_style_selectors import s, ss

from config.driver_config import MEDIA_PATH, PLATFORM

__author__ = 'knysh'


def locator_for_platform(selectors):
    return selectors.get(PLATFORM, 'Undefined Selector')


def element(selectors):
    return s(locator_for_platform(selectors))


def elements(selectors):
    return ss(locator_for_platform(selectors))


def match_by_regex(text):
    return matches_regexp(text.replace(' ', '[\\S+\\n\\r\\s]+'))


def repeat_check(actual, matcher, timeout=0, prestep=None, repeat=None):
    count = 0
    repeat = 1 if repeat is None else repeat
    while count < repeat:
        try:
            if prestep:
                prestep()
            actual = actual(matcher, timeout=timeout)
            break
        except AssertionError as e:
            count += 1
            if count == repeat:
                raise e


def format_exception(e):
    return str(e.args[0]).replace('[\\S+\\n\\r\\s]+', ' ').replace('$', ''),


def update_media():
    """Push files to real device"""
    if PLATFORM == 'ANDROID':
        remote_target_path = '/storage/emulated/0/Pictures/VuzeXR/Original'
        subprocess.call('adb shell rm -r /storage/emulated/0/Pictures/VuzeXR', shell=True)
        subprocess.call(f'adb push {MEDIA_PATH}/photo_180.jpg {remote_target_path}/photo_180.jpg', shell=True)
        subprocess.call(f'adb push {MEDIA_PATH}/photo_360.jpg {remote_target_path}/photo_360.jpg', shell=True)
