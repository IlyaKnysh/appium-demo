from testlib.screens.common_screen import *
from testlib.utils import element

__author__ = 'knysh'

edit_button = element({
    'ANDROID': by.xpath('//*[contains(@text,"EDIT")]'),
    'IOS': by.name('EDIT')
})

directors_cut_button = element({
    'ANDROID': by.xpath('//android.widget.TextView[contains(@text,"DIRECTOR")]'),
    'IOS': by.class_chain('**/XCUIElementTypeOther[$name CONTAINS[c] "DIRECTOR"$][-1]')
})
