from testlib import by
from testlib.utils import element, elements

__author__ = 'knysh'

editor_menu_back_button = element({
    'ANDROID': by.id('camera.vuze.xr:id/menuBack'),
    'IOS': by.accessibility_id('btnGrayNext')
})

menu_options = elements({
    'ANDROID': by.xpath('//android.widget.TextView[position()>1]'),
    'IOS': by.class_name('XCUIElementTypeCell')
})