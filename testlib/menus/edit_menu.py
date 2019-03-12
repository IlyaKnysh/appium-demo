from testlib.menus.common_menu import *

__author__ = 'knysh'

finish_edit_button = element({
    'ANDROID': by.id('camera.vuze.xr:id/finishEditingButton'),
    'IOS': by.accessibility_id('FINISH')
})

effects_button = element({
    'ANDROID': by.xpath('//android.widget.TextView[@text="EFFECTS" or @text="Effects"]'),
    'IOS': by.class_chain('**/XCUIElementTypeOther[$name CONTAINS[c] "iconEffectsWhite"$][-1]')
})