from selenium.webdriver.common.by import By

from objects.base_page import BasePage


class AndriodSearchByTextPage(BasePage):

    # static xpath. used as is
    __SEARCH_BY_TEXT_FIELD = (By.ID, "search_input")
    __SEARCH_BY_TEXT_SEARCH_RESULTS_HEADER = (By.ID, "search_results_header")
    __SEARCH_BY_TEXT_SEARCH_RESULTS = (By.ID, "search_results_snippet")
    __SEARCH_BY_TEXT_FIRST_QUESTION_LINK = (
        By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView[@resource-id='search_results']/android."
        "widget.LinearLayout[1]/android.widget.TextView",
    )
    __SEARCH_BY_TEXT_ASK_QUESTION_BUTTON = (
        By.XPATH,
        "//android.widget.FrameLayout[@resource-id='ask_container']/android.widget.ImageView",
    )

    def fill_search_by_text_field(self, text: str):
        """
        Type symbols in search by text filed
        """
        self.fill(by_locator=self.__SEARCH_BY_TEXT_FIELD, value=text)

    def check_if_search_results_block_is_presented(self):
        """
        Check if Search results block is presented
        """
        return self.if_element_displayed(by_locator=self.__SEARCH_BY_TEXT_SEARCH_RESULTS_HEADER)

    def get_all_search_results(self):
        """
        Check if all search results contain search keyword
        """
        return self.get_all_elements_attributes(by_locator=self.__SEARCH_BY_TEXT_SEARCH_RESULTS, attribute_name="text")

    def click_first_question_link(self):
        """
        Click on first in the list question link
        """
        self.click(self.__SEARCH_BY_TEXT_FIRST_QUESTION_LINK)

    def click_ask_question_button(self):
        """
        Click "Ask question" button
        """
        self.hide_keyboard()
        self.click(self.__SEARCH_BY_TEXT_ASK_QUESTION_BUTTON)
