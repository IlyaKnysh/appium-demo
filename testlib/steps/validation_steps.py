import allure

from config.driver_config import PLATFORM
from testlib.screens import gallery_screen, selection_mode_screen
from testlib.steps.assert_steps.common_assert_steps import BaseAssert
from testlib.steps.assert_steps.gallery_assert_steps import SelectionMode, GalleryContent
from testlib.steps.assert_steps.preview_screen_assert_steps import Editor, Effects
from testlib.steps.assert_steps.settings_assert_steps import BitrateSettings, SettingsSlider


class ContentValidationSteps:

    @allure.step('Check elements on "Bitrate" screen')
    def check_bitrate_screen(self):
        BitrateSettings.check_bitrate_settings_screen_title_valid()

        BaseAssert.check_back_button_clickable()
        SettingsSlider.check_slider_current_value(pattern='\d* MBps')
        SettingsSlider.check_slider_max_value('15.0 MBps' if PLATFORM == 'IOS' else '15 MBps')
        SettingsSlider.check_slider_min_value('0.5 MBps' if PLATFORM == 'IOS' else '4 MBps')
        SettingsSlider.check_slider_clickable()

    @allure.step('Check elements in effects menu')
    def check_effects_menu(self):
        Editor.check_finish_button_not_exist(timeout=0)
        Editor.check_back_button_clickable()
        Effects.check_none_button_clickable()
        Effects.check_glow_button_clickable()
        Effects.check_poster_button_clickable()
        Effects.check_pixelate_button_clickable()
        Effects.check_pointillize_button_clickable()
        Effects.check_edges_button_clickable()
        Effects.check_lineart_button_clickable()

    @allure.step('Check elements state in selection mode with all selected elements')
    def check_selection_mode_all_select(self):
        SelectionMode.check_select_all_screen_title_valid()

        for media in gallery_screen.media_list:
            SelectionMode.check_element_status(media, checked=True)

        SelectionMode.check_deselect_all_button_clickable()

        SelectionMode.check_delete_button_clickable()

        SelectionMode.check_info_button_visible()
        SelectionMode.check_info_button_disabled()

        SelectionMode.check_share_button_visible()
        SelectionMode.check_info_button_disabled()

    @allure.step('Check elements state in selection mode with no selected elements')
    def check_selection_mode_no_select(self):

        GalleryContent.check_date_labels_visible()
        SelectionMode.check_no_select_screen_title_valid()
        SelectionMode.check_cancel_button_clickable()
        SelectionMode.check_select_all_button_clickable()
        SelectionMode.check_all_elements_checked()
        for element in selection_mode_screen.select_media_checkboxes:
            SelectionMode.check_element_status(element)
        SelectionMode.check_delete_button_visible()
        SelectionMode.check_delete_button_disabled()
        SelectionMode.check_info_button_visible()
        SelectionMode.check_info_button_disabled()
        SelectionMode.check_share_button_visible()
        SelectionMode.check_share_button_disabled()

    @allure.step('Check elements on empty gallery screen')
    def check_empty_gallery_screen(self):
        GalleryContent.check_empty_placeholder_exist()
        GalleryContent.check_empty_gallery_title_valid()
        GalleryContent.check_empty_gallery_info_valid()
        GalleryContent.check_gallery_screen_title_valid()