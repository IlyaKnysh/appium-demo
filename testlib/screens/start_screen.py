from testlib.screens.common_screen import *

__author__ = 'knysh'

camera_button = element({
    'ANDROID': by.id('camera.vuze.xr:id/button_camera_label'),
    'IOS': by.class_chain('**XCUIElementTypeOther/XCUIElementTypeStaticText[1]')
})

gallery_button = element({
    'ANDROID': by.id('camera.vuze.xr:id/button_gallery'),
    'IOS': by.accessibility_id('Gallery')
})

settings_button = element({
    'ANDROID': by.id('camera.vuze.xr:id/button_settings'),
    'IOS': by.class_chain('**/XCUIElementTypeOther[$name CONTAINS[c] "btnSettings"$][-1]')
})
