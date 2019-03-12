from testlib import by
from testlib.utils import element, elements

__author__ = 'knysh'

back_button = element({
    'ANDROID': by.xpath('//android.widget.ImageButton[@content-desc or @resource-id="camera.vuze.xr:id/backButton"]'),
    'IOS': by.class_chain('**/XCUIElementTypeButton[`name CONTAINS[c] "back"`][-1]')
})

screen_title = element({
    'ANDROID': by.xpath(
        '((//android.view.ViewGroup[contains(@resource-id, "bar")])[last()]//android.widget.TextView)[1]'),
    'IOS': by.xpath(
        '//XCUIElementTypeOther/XCUIElementTypeStaticText[preceding::XCUIElementTypeButton or following:: XCUIElementTypeButton]')
})
