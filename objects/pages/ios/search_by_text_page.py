from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from objects.base_page import BasePage


class IosSearchByTextPage(BasePage):

    # static xpath. used as is
    __SEARCH_BY_TEXT_SEARCH_FIELD = (MobileBy.ACCESSIBILITY_ID, "Type your question")
    __SEARCH_BY_TEXT_SEARCH_BUTTON = (MobileBy.ACCESSIBILITY_ID, "icon search")
    __SEARCH_BY_TEXT_SEARCH_RESULTS_HEADER = (MobileBy.IOS_PREDICATE, 'label == "Search results"')
    __SEARCH_BY_TEXT_ASK_QUESTION_BUTTON = (MobileBy.ACCESSIBILITY_ID, "icon plus")
    __SEARCH_BY_TEXT_SEARCH_RESULTS = (
        By.XPATH,
        '//XCUIElementTypeOther[@name="Search results"]/../XCUIElementTypeCell',
    )
    __SEARCH_BY_TEXT_FIRST_QUESTION_LINK = (
        By.XPATH,
        '//XCUIElementTypeOther[@name="Search results"]/../XCUIElementTypeCell[1]',
    )

    def fill_search_by_text_field(self, text: str):
        """
        Type symbols in search by text filed
        """
        self.fill(by_locator=self.__SEARCH_BY_TEXT_SEARCH_FIELD, value=text)
        self.click(by_locator=self.__SEARCH_BY_TEXT_SEARCH_BUTTON)

    def check_if_search_results_block_is_presented(self):
        """
        Check if Search results block is presented
        """
        return self.if_element_displayed(by_locator=self.__SEARCH_BY_TEXT_SEARCH_RESULTS_HEADER)

    def get_all_search_results(self):
        """
        Check if all search results contain search keyword
        """
        return self.get_all_elements_attributes(by_locator=self.__SEARCH_BY_TEXT_SEARCH_RESULTS, attribute_name="name")

    def click_first_question_link(self):
        """
        Click on first in the list question link
        """
        self.click(self.__SEARCH_BY_TEXT_FIRST_QUESTION_LINK)

    def click_ask_question_button(self):
        """
        Click "Ask question" button
        """
        self.click(self.__SEARCH_BY_TEXT_ASK_QUESTION_BUTTON)
