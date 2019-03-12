from testlib.screens.common_screen import *
from testlib.utils import locator_for_platform

__author__ = 'knysh'

select_media_checkboxes = elements({
    'ANDROID': by.xpath(
        '//android.view.ViewGroup/android.widget.CheckBox[preceding-sibling::android.widget.ImageView]'),
    'IOS': by.predicate('type == "XCUIElementTypeButton" AND name=="uncheck"')
})

select_all_button = element({
    'ANDROID': by.xpath(
        '//android.widget.CheckBox[@resource-id="camera.vuze.xr:id/select_button" and contains(@text, "Select")]'),
    'IOS': by.accessibility_id('Select All')
})

deselect_all_button = element({
    'ANDROID': by.xpath(
        '//android.widget.CheckBox[@resource-id="camera.vuze.xr:id/select_button" and contains(@text, "Deselect")]'),
    'IOS': by.predicate('type =="XCUIElementTypeButton" and name CONTAINS "Deselect All"')
})

cancel_button = element({
    'ANDROID': by.id('camera.vuze.xr:id/action_mode_close_button'),
    'IOS': by.accessibility_id('Cancel')
})

delete_button = element({
    'ANDROID': by.id('camera.vuze.xr:id/deleteButton'),
    'IOS': by.accessibility_id('delete')
})

info_button = element({
    'ANDROID': by.id('camera.vuze.xr:id/infoButton'),
    'IOS': by.accessibility_id('info')
})

share_button = element({
    'ANDROID': by.id('camera.vuze.xr:id/shareButton'),
    'IOS': by.accessibility_id('share')
})


def get_media_checkbox(selene_element):
    return selene_element.element(locator_for_platform({
        'IOS': by.name('uncheck'),
        'ANDROID': by.xpath('.//android.widget.CheckBox')}))
