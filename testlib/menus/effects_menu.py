from testlib.menus.common_menu import *

__author__ = 'knysh'

none_button = element({
    'ANDROID': by.xpath('//android.widget.TextView[@text="NONE"]'),
    'IOS': by.accessibility_id('NONE')
})

glow_button = element({
    'ANDROID': by.xpath('//android.widget.TextView[@text="GLOW"]'),
    'IOS': by.accessibility_id('GLOW')
})

poster_button = element({
    'ANDROID': by.xpath('//android.widget.TextView[@text="POSTER"]'),
    'IOS': by.accessibility_id('POSTER')
})

pixelate_button = element({
    'ANDROID': by.xpath('//android.widget.TextView[@text="PIXELATE"]'),
    'IOS': by.accessibility_id('PIXELATE')
})

pointillize_button = element({
    'ANDROID': by.xpath('//android.widget.TextView[@text="POINTILIZE"]'),
    'IOS': by.accessibility_id('POINTILLIZE')
})

edges_button = element({
    'ANDROID': by.xpath('//android.widget.TextView[@text="EDGES"]'),
    'IOS': by.accessibility_id('EDGES')
})

lineart_button = element({
    'ANDROID': by.xpath('//android.widget.TextView[@text="LINE ART"]'),
    'IOS': by.accessibility_id('LINEART')
})
