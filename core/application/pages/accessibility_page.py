from core.testlib import by
from core.testlib.utils import element

accessibility_node_provider_button = element({
    'ANDROID': by.xpath('//android.widget.TextView[@content-desc="Accessibility Node Provider"]'),
    'IOS': by.accessibility_id('')
})

accessibility_node_querying_button = element({
    'ANDROID': by.xpath('//android.widget.TextView[@content-desc="Accessibility Node Querying"]'),
    'IOS': by.accessibility_id('')
})

accessibility_service_button = element({
    'ANDROID': by.xpath('//android.widget.TextView[@content-desc="Accessibility Service"]'),
    'IOS': by.accessibility_id('')
})

custom_view_button = element({
    'ANDROID': by.xpath('//android.widget.TextView[@content-desc="Custom View"]'),
    'IOS': by.accessibility_id('')
})
