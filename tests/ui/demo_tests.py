import allure
import pytest
from testlib.steps.main_steps import MainSteps
from testlib.steps.validation_steps import ContentValidationSteps

__author__ = 'knysh'


@pytest.mark.parametrize('driver', [{'noReset': False}], indirect=True,
                         ids=lambda x: [f'{str(k)}: {str(v)}' for k, v in x.items()][0])
@allure.story('Selection mode screen with select all')
@allure.feature('Gallery')
def test_selection_mode_screen_all_select(driver):
    steps = MainSteps()
    content_steps = ContentValidationSteps()
    steps.open_gallery()
    steps.tap_select_button()
    steps.tap_select_all_button()
    content_steps.check_selection_mode_all_select()

    steps.tap_deselect_all_button()

    content_steps.check_selection_mode_no_select()


@allure.story('Bitrate settings screen')
@allure.feature('Settings')
def test_bitrate_screen():
    steps = MainSteps()
    content_steps = ContentValidationSteps()
    steps.open_settings_screen()
    steps.open_broadcast_settings_screen()
    steps.open_bitrate_settings_screen()
    content_steps.check_bitrate_screen()


@allure.story('Delete all media')
@allure.feature('Gallery')
def test_delete_all_media():
    steps = MainSteps()
    content_steps = ContentValidationSteps()
    steps.open_gallery()
    steps.tap_select_button()
    steps.tap_select_all_button()
    steps.delete_media()

    content_steps.check_empty_gallery_screen()


@pytest.mark.parametrize('driver', [{'noReset': False}], indirect=True,
                         ids=lambda x: [f'{str(k)}: {str(v)}' for k, v in x.items()][0])
@pytest.mark.parametrize('video_mode', ['photo_180'], ids=lambda x: f'{x}')
@allure.story('Edit effects menu')
@allure.feature('Edit media')
def test_edit_effects_menu(driver, video_mode):
    steps = MainSteps()
    content_steps = ContentValidationSteps()
    steps.open_gallery()
    steps.open_180_photo()
    steps.open_edit_media_screen()
    steps.select_effects()

    content_steps.check_effects_menu()
