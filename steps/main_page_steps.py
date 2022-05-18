import allure

from core.application.pages import main_page


@allure.step('Open accessibility')
def open_accessibility() -> None:
    main_page.accessibility_button.click()
