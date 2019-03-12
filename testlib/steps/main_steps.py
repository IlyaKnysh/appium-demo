import allure

from testlib.matchers import is_element_exist
from testlib.menus import edit_menu
from testlib.popups import delete_popup
from testlib.screens import start_screen, gallery_screen, preview_screen, selection_mode_screen, settings_screen
from testlib.steps.assert_steps.gallery_assert_steps import GalleryContent, SelectionMode
from testlib.steps.assert_steps.preview_screen_assert_steps import Editor
from testlib.steps.assert_steps.settings_assert_steps import BitrateSettings, BroadcastSettings, Settings

__author__ = 'knysh'


class MainSteps:

    @allure.step('Open camera dashboard')
    def open_camera_dashboard(self):
        start_screen.camera_button.click()

    @allure.step('Open gallery screen')
    def open_gallery(self):
        start_screen.gallery_button.click()
        GalleryContent.check_phone_tab_visible()

    @allure.step('Tap "Select" button')
    def tap_select_button(self):
        gallery_screen.select_button.click()

    @allure.step('Tap "Select all" button')
    def tap_select_all_button(self):
        selection_mode_screen.select_all_button.click()

    @allure.step('Tap "Select all" button')
    def tap_deselect_all_button(self):
        selection_mode_screen.deselect_all_button.click()

    @allure.step('Delete selected video')
    def delete_media(self):
        selection_mode_screen.delete_button.click()
        SelectionMode.check_popup_delete_button_visible()
        delete_popup.delete_button.click()

    @allure.step('Open 180 photo')
    def open_180_photo(self):
        gallery_screen.photo_180_list[0].click()

    @allure.step('Tap director\'s cut button')
    def open_directors_cut(self):
        preview_screen.directors_cut_button.click()

    @allure.step('Open edit media screen')
    def open_edit_media_screen(self):
        if is_element_exist(preview_screen.directors_cut_button, timeout=2):
            self.open_directors_cut()
        if is_element_exist(preview_screen.edit_button, timeout=2):
            preview_screen.edit_button.click()
        Editor.check_finish_button_visible()

    @allure.step('Select effects')
    def select_effects(self):
        edit_menu.effects_button.click()
        Editor.check_back_button_clickable()

    @allure.step('Open settings screen')
    def open_settings_screen(self):
        start_screen.settings_button.click()
        Settings.check_settings_screen_title_valid()

    @allure.step('Open broadcast settings screen')
    def open_broadcast_settings_screen(self):
        settings_screen.get_option('Broadcast Settings').click()
        BroadcastSettings.check_broadcast_settings_screen_title_valid()

    @allure.step('Open bitrate settings screen')
    def open_bitrate_settings_screen(self):
        settings_screen.get_option('Bitrate').click()
        BitrateSettings.check_bitrate_settings_screen_title_valid()


