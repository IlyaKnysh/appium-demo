from selene.conditions import clickable

from testlib.matchers import check_that
from testlib.screens import common_screen


class BaseAssert:

    @staticmethod
    def check_back_button_clickable(prestep=None, timeout=None, repeat=None):
        check_that(common_screen.back_button.should, clickable, 'Back button is displayed and active', prestep=prestep,
                   timeout=timeout, repeat=repeat)
