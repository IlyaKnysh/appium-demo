from hamcrest import equal_to
from selene.conditions import clickable, visible, enabled, exist

from config.driver_config import PLATFORM
from testlib.matchers import check_that
from testlib.popups import delete_popup
from testlib.screens import selection_mode_screen, gallery_screen
from testlib.screens.selection_mode_screen import get_media_checkbox
from testlib.utils import match_by_regex


class SelectionMode:

    @staticmethod
    def check_no_select_screen_title_valid():
        check_that(selection_mode_screen.screen_title.text,
                   equal_to('Select items' if PLATFORM == 'IOS' else '0 items selected'),
                   'Inscription "Select items" is displayed')

    @staticmethod
    def check_select_all_screen_title_valid():
        check_that(selection_mode_screen.screen_title.text, match_by_regex('\d* (items|item) selected'),
                   'Inscription "\d* items selected" is displayed')

    @staticmethod
    def check_cancel_button_clickable():
        check_that(selection_mode_screen.cancel_button.should, clickable, 'Cancel button is displayed and active')

    @staticmethod
    def check_select_all_button_clickable():
        check_that(selection_mode_screen.select_all_button.should, clickable,
                   '"Select All" button is displayed and active')

    @staticmethod
    def check_all_elements_checked():
        check_that(len(selection_mode_screen.select_media_checkboxes) == len(gallery_screen.media_list),
                   'All media elements has checkboxes')

    @staticmethod
    def check_element_status(element, checked=False):
        if checked:
            if PLATFORM == 'ANDROID':
                check_that(get_media_checkbox(element).get_attribute('checked') == 'true',
                           f'Checkbox is checked for {element}')
            if PLATFORM == 'IOS':
                check_that(get_media_checkbox(element).get_attribute('value') == '1',
                           f'Checkbox is checked for {element}')
        else:
            if PLATFORM == 'ANDROID':
                check_that(element.get_attribute('checked') == 'false', f'Checkbox is unchecked for {element}')
            if PLATFORM == 'IOS':
                check_that(element.get_attribute('value'), equal_to(None), f'Checkbox is unchecked for {element}')

    @staticmethod
    def check_delete_button_visible():
        check_that(selection_mode_screen.delete_button.should, visible, 'Delete button is displayed')

    @staticmethod
    def check_delete_button_disabled():
        check_that(selection_mode_screen.delete_button.should_not, enabled, 'Delete button is disabled')

    @staticmethod
    def check_delete_button_clickable():
        check_that(selection_mode_screen.delete_button.should, clickable, 'Delete button is displayed and active')

    @staticmethod
    def check_info_button_visible():
        check_that(selection_mode_screen.info_button.should, visible, 'Info button is displayed')

    @staticmethod
    def check_info_button_disabled():
        check_that(selection_mode_screen.info_button.should_not, enabled, 'Info button is disabled')

    @staticmethod
    def check_share_button_visible():
        check_that(selection_mode_screen.share_button.should, visible, 'Share button is displayed')

    @staticmethod
    def check_share_button_disabled():
        check_that(selection_mode_screen.share_button.should_not, enabled, 'Share button is disabled')

    @staticmethod
    def check_deselect_all_button_clickable():
        check_that(selection_mode_screen.deselect_all_button.should, clickable,
                   '"Deselect all" button is displayed and active')

    @staticmethod
    def check_popup_delete_button_visible():
        check_that(delete_popup.delete_button.should, visible, 'Delete button in pop-up is displayed')


class GalleryContent:

    @staticmethod
    def check_empty_placeholder_exist():
        check_that(gallery_screen.empty_placeholder.should, exist, 'Placeholder for empty gallery is displayed')

    @staticmethod
    def check_empty_gallery_title_valid():
        check_that(gallery_screen.empty_gallery_title.get_attribute(
            'value') if PLATFORM == 'IOS' else gallery_screen.empty_gallery_title.text,
                   match_by_regex('The gallery is empty' if PLATFORM == 'IOS' else 'Gallery is empty'),
                   'Valid title for empty gallery is displayed')

    @staticmethod
    def check_empty_gallery_info_valid():
        check_that(gallery_screen.empty_gallery_info.get_attribute(
            'value') if PLATFORM == 'IOS' else gallery_screen.empty_gallery_info.text, match_by_regex(
            'Once (captured|downloaded) - Your XR (moments|experiences) will appear here'),
                   'Valid info for empty gallery is displayed')

    @staticmethod
    def check_gallery_screen_title_valid():
        check_that(gallery_screen.screen_title.text, equal_to('Gallery'), 'Gallery label is displayed')

    @staticmethod
    def check_phone_tab_visible():
        check_that(gallery_screen.phone_tab.should, visible, 'Gallery is displayed')

    @staticmethod
    def check_date_labels_visible():
        check_that(gallery_screen.date_labels[0].should, visible, 'Title of day is displayed')
