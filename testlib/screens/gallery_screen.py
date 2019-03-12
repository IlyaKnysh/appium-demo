from testlib.screens.common_screen import *

__author__ = 'knysh'

select_button = element({
    'ANDROID': by.id('camera.vuze.xr:id/selectItem'),
    'IOS': by.accessibility_id('Select')
})

phone_tab = element({
    'ANDROID': by.accessibility_id('Phone'),
    'IOS': by.accessibility_id('PHONE')
})

date_labels = elements({
    'ANDROID': by.id('camera.vuze.xr:id/headerTextView'),
    'IOS': by.xpath(
        '//XCUIElementTypeCollectionView//XCUIElementTypeStaticText[@name and not(preceding::XCUIElementTypeImage)]')
})

media_list = elements({
    'ANDROID': by.xpath(
        '//android.widget.ImageView[@resource-id="camera.vuze.xr:id/thumbnailImageView"]/parent::android.view.ViewGroup'),
    'IOS': by.predicate('type == "XCUIElementTypeCell" and visible == True')
})

photo_180_list = elements({
    'ANDROID': by.xpath(
        '//android.widget.ImageView[@content-desc="180__" and not(following-sibling::android.widget.TextView)]/parent::android.view.ViewGroup'),
    'IOS': by.xpath(
        '//XCUIElementTypeImage[@name="dashboardCameraStatus180" and not(following-sibling::XCUIElementTypeStaticText)]/parent:: XCUIElementTypeOther[count(XCUIElementTypeImage[not(@name)])=4]')
})

empty_placeholder = element({
    'ANDROID': by.id('camera.vuze.xr:id/emptyImageView'),
    'IOS': by.accessibility_id('theGalleryIsEmpty')
})

empty_gallery_title = element({
    'ANDROID': by.id('camera.vuze.xr:id/emptyTitleTextView'),
    'IOS': by.class_chain('**/XCUIElementTypeOther[$name == "theGalleryIsEmpty"$][-1]/XCUIElementTypeStaticText[1]')
})

empty_gallery_info = element({
    'ANDROID': by.id('camera.vuze.xr:id/emptyMessageImageView'),
    'IOS': by.class_chain('**/XCUIElementTypeOther[$name == "theGalleryIsEmpty"$][-1]/XCUIElementTypeStaticText[2]')
})
