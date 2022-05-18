from core.application.pages import accessibility_page
from core.testlib.matchers import check_that


def check_accessibility_page_items() -> None:
    check_that(accessibility_page.accessibility_node_provider_button.is_displayed(),
               message='Accessibility node provider is displayed')
    check_that(accessibility_page.accessibility_node_querying_button.is_displayed(),
               message='Accessibility node querying is displayed')
    check_that(accessibility_page.accessibility_service_button.is_displayed(),
               message='Accessibility service is displayed')
    check_that(accessibility_page.custom_view_button.is_displayed(), message='Custom view is displayed')