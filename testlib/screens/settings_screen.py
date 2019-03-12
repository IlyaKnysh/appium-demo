from testlib.screens.common_screen import *

__author__ = 'knysh'


def get_option(option_name):
    return element(({
        'ANDROID': by.xpath(f'//android.widget.TextView[contains(@text, "{option_name}")]'),
        'IOS': by.name(option_name)
    }))
