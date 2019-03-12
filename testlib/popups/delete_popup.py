from testlib.popups.common_popup import *

__author__ = 'knysh'

cancel_button = element({
    'ANDROID': by.id('camera.vuze.xr:id/removeOrCopyCancelBeforeStartButton'),
    'IOS': by.accessibility_id('CANCEL')
})

delete_button = element({
    'ANDROID': by.id('camera.vuze.xr:id/removeOrCopyConfirmButton'),
    'IOS': by.accessibility_id('DELETE')
})

main_text = element({
    'ANDROID': by.id('camera.vuze.xr:id/removeOrCopyClarificationText'),
    'IOS': by.xpath(
        '//XCUIElementTypeOther/XCUIElementTypeStaticText[following-sibling:: XCUIElementTypeButton[@name="DELETE"]][2]')
})

thumbnail = element({
    'ANDROID': by.id('camera.vuze.xr:id/removeOrCopyFilesStackView'),
    'IOS': by.class_chain('**/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')
})

header = element({
    'ANDROID': by.id('camera.vuze.xr:id/removeOrCopyConfirmQuestionText'),
    'IOS': by.xpath('//XCUIElementTypeStaticText[following-sibling:: XCUIElementTypeButton[@name="DELETE"]][1]')
})
