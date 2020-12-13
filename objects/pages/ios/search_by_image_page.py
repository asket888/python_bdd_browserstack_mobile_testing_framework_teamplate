from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from objects.base_page import BasePage


class IosSearchByImagePage(BasePage):

    # static xpath. used as is
    __SEARCH_BY_IMAGE_SCAN_AND_SOLVE_BUTTON = (MobileBy.IOS_PREDICATE, 'label == "SCAN & SOLVE"')
    __SEARCH_BY_IMAGE_BY_TEXT_BUTTON = (By.XPATH, '//XCUIElementTypeImage[@name="icon_keyboard"]/..')

    def check_if_scan_and_solve_button_is_presented(self):
        """
        Check if Search by Image page is presented
        """
        return self.if_element_displayed(by_locator=self.__SEARCH_BY_IMAGE_SCAN_AND_SOLVE_BUTTON)

    def click_search_by_text_button(self):
        """
        Click [Search by text] button on main page
        """
        self.click(by_locator=self.__SEARCH_BY_IMAGE_BY_TEXT_BUTTON)
