from selenium.webdriver.common.by import By

from objects.base_page import BasePage

from utils.data_generator_util import get_random_string


class AndroidAskQuestionPage(BasePage):

    # static xpath. used as is
    __ASK_QUESTION_PAGE = (By.ID, "ask_question_header")
    __ASK_QUESTION_PAGE_TEXT_FIELD = (By.ID, "ask_question_content_text")
    __ASK_QUESTION_PAGE_ASK_QUESTION_BUTTON = (By.ID, "toolbar_action_button")
    __ASK_QUESTION_FIRST_PAGE_SUBJECT_BUTTON = (
        By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView[@resource-id='picker_selectable_list']/"
        "android.widget.LinearLayout[1]",
    )

    def check_if_ask_question_page_is_presented(self):
        """
        Check if ask question page is presented
        """
        return self.if_element_displayed(by_locator=self.__ASK_QUESTION_PAGE)

    def fill_text_field_on_ask_question_page(self, text: str, symbols_num: int):
        """
        Fill ask question field by chosen number of symbols
        """
        question_text = f"{text} {get_random_string(length=symbols_num)}\n"
        self.clear(by_locator=self.__ASK_QUESTION_PAGE_TEXT_FIELD)
        self.fill(by_locator=self.__ASK_QUESTION_PAGE_TEXT_FIELD, value=question_text)

    def click_submit_button(self):
        """
        Click ask question button
        """
        self.click(by_locator=self.__ASK_QUESTION_PAGE_ASK_QUESTION_BUTTON)

    def click_subject_button(self):
        """
        Click first subject button
        """
        self.click(by_locator=self.__ASK_QUESTION_FIRST_PAGE_SUBJECT_BUTTON)
