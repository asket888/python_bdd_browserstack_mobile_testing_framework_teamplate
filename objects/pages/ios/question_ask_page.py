from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from objects.base_page import BasePage

from utils.data_generator_util import get_random_string


class IosAskQuestionPage(BasePage):

    # static xpath. used as is
    __ASK_QUESTION_PAGE = (MobileBy.IOS_PREDICATE, 'name == "ASK QUESTION" AND type == "XCUIElementTypeNavigationBar"')
    __ASK_QUESTION_ASKED_QUESTION_PAGE = (MobileBy.IOS_PREDICATE, 'label == "task_details_view"')
    __ASK_QUESTION_POPUP_CONFIRM_BUTTON = (MobileBy.ACCESSIBILITY_ID, "ASK YOUR QUESTION")
    __ASK_QUESTION_SUBJECT_BUTTON = (MobileBy.IOS_PREDICATE, 'label == "SUBJECT"')
    __ASK_QUESTION_SUBJECT_TEXT = (By.XPATH, '//XCUIElementTypeButton[@name="Back"]/..')
    __ASK_QUESTION_TEXT_FIELD = (
        By.XPATH,
        '//XCUIElementTypeNavigationBar[@name="ASK QUESTION"]/..//XCUIElementTypeTextView',
    )
    __ASK_QUESTION_ASK_QUESTION_BUTTON = (
        MobileBy.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeStaticText[`label == "ASK QUESTION"`][2]',
    )

    # dynamic xpath template. should be transformed to (By.XPATH, "xpath") before use
    __ASK_QUESTION_SUBJECT_BUTTON_TEMPLATE = "{subject_name}"

    def check_if_ask_question_page_is_presented(self):
        """
        Check if ask question page is presented
        """
        return self.if_element_displayed(by_locator=self.__ASK_QUESTION_PAGE)

    def check_if_asked_question_page_is_presented(self):
        """
        Check if asked question page is presented
        """
        return self.if_element_displayed(by_locator=self.__ASK_QUESTION_ASKED_QUESTION_PAGE)

    def fill_text_field_on_ask_question_page(self, text: str, symbols_num: int):
        """
        Fill ask question field by chosen number of symbols
        """
        question_text = f"{text} {get_random_string(length=symbols_num)}\n"
        self.clear(by_locator=self.__ASK_QUESTION_TEXT_FIELD)
        self.fill(by_locator=self.__ASK_QUESTION_TEXT_FIELD, value=question_text)

    def select_subject(self, subject_name: str):
        """
        Select subject
        """
        subject_locator = (
            MobileBy.ACCESSIBILITY_ID,
            self.__ASK_QUESTION_SUBJECT_BUTTON_TEMPLATE.format(subject_name=subject_name),
        )
        self.click(by_locator=self.__ASK_QUESTION_SUBJECT_BUTTON)
        self.click(by_locator=subject_locator)

    def click_submit_button(self):
        """
        Click ask question button
        """
        self.click(by_locator=self.__ASK_QUESTION_ASK_QUESTION_BUTTON)

    def click_ask_community_on_who_you_want_to_ask_popup(self):
        """
        Click ask question button
        """
        self.click(by_locator=self.__ASK_QUESTION_POPUP_CONFIRM_BUTTON)
