from testlib.screens.common_screen import *

__author__ = 'knysh'

current_value = element({
    'ANDROID': by.id('camera.vuze.xr:id/selectedLabelTextView'),
    'IOS': by.class_chain('**/XCUIElementTypeOther[$name =="menuBgBoatVertical"$][-1]/XCUIElementTypeStaticText[1]')
})

min_value = element({
    'ANDROID': by.id('camera.vuze.xr:id/minLabelTextView'),
    'IOS': by.class_chain('**/XCUIElementTypeOther[$name =="menuBgBoatVertical"$][-1]/XCUIElementTypeStaticText[2]')
})

max_value = element({
    'ANDROID': by.id('camera.vuze.xr:id/maxLabelTextView'),
    'IOS': by.class_chain('**/XCUIElementTypeOther[$name =="menuBgBoatVertical"$][-1]/XCUIElementTypeStaticText[3]')
})

slider = element({
    'ANDROID': by.id('camera.vuze.xr:id/seekBar'),
    'IOS': by.class_name('XCUIElementTypeSlider')
})
