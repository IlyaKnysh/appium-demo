import allure

from steps import accessibility_page_steps
from steps import main_page_steps


@allure.description('mp-1')
@allure.title('Check accessibility page options')
@allure.tag('Accessibility Page')
def test_accessibility_options():
    main_page_steps.open_accessibility()

    accessibility_page_steps.check_accessibility_page_items()
