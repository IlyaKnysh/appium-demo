from core.testlib import by
from core.testlib.utils import element

accessibility_button = element({
    'ANDROID': by.xpath('//android.widget.TextView[@content-desc="Accessibility"]'),
    'IOS': by.accessibility_id('')
})

