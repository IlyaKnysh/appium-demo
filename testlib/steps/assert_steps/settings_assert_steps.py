from selene.conditions import clickable

from testlib.matchers import check_that
from testlib.screens import settings_screen, common_slider_screen
from testlib.steps.assert_steps.common_assert_steps import BaseAssert
from testlib.utils import match_by_regex


class Settings(BaseAssert):

    @staticmethod
    def check_settings_screen_title_valid():
        check_that(settings_screen.screen_title.text, 'Settings', 'Settings screen title is valid')


class BroadcastSettings(BaseAssert):

    @staticmethod
    def check_broadcast_settings_screen_title_valid():
        check_that(settings_screen.screen_title.text, match_by_regex('Broadcast Settings'),
                   'Broadcast settings screen title is valid')


class BitrateSettings(BaseAssert):

    @staticmethod
    def check_bitrate_settings_screen_title_valid():
        check_that(settings_screen.screen_title.text, match_by_regex('Bitrate'),
                   'Bitrate settings screen title is valid')


class SettingsSlider:

    @staticmethod
    def check_slider_current_value(pattern='.*'):
        check_that(common_slider_screen.current_value.text, match_by_regex(pattern), 'Some selected value is displayed')

    @staticmethod
    def check_slider_min_value(pattern=None):
        check_that(common_slider_screen.min_value.text, match_by_regex(pattern),
                   f'{pattern} minimum value is displayed')

    @staticmethod
    def check_slider_max_value(pattern=None):
        check_that(common_slider_screen.max_value.text, match_by_regex(pattern),
                   f'{pattern} maximum value is displayed')

    @staticmethod
    def check_slider_clickable():
        check_that(common_slider_screen.slider.should, clickable, 'Slider is displayed and active')
