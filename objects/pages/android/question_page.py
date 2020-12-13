from selenium.webdriver.common.by import By

from objects.base_page import BasePage


class AndroidQuestionPage(BasePage):

    # static xpath. used as is
    __QUESTION_PAGE_CONFIRM_BUTTON = (By.ID, "question_header")
    __QUESTION_PAGE_SUBJECT_TEXT = (By.ID, "question_header_subject")
    __QUESTION_PAGE_QUESTION_TEXT = (By.ID, "question_content")
    __QUESTION_PAGE_AUTHOR_TEXT = (By.ID, "author_description")

    def check_if_question_page_is_presented(self):
        """
        Check if question page is presented
        """
        return self.if_element_displayed(by_locator=self.__QUESTION_PAGE_CONFIRM_BUTTON)

    def get_question_subject(self):
        """
        Get question subject from Question page
        """
        return self.get_element_attribute(by_locator=self.__QUESTION_PAGE_SUBJECT_TEXT, attribute_name="text")

    def get_question_text(self):
        """
        Get question text from Question page
        """
        return self.get_element_attribute(by_locator=self.__QUESTION_PAGE_QUESTION_TEXT, attribute_name="text")

    def get_actual_and_expected_question_author(self):
        """
        Get question author nickname from Question page
        """
        user = self.get_env_user()
        expected_nick_name = user["login"]
        actual_nick_name = self.get_element_attribute(
            by_locator=self.__QUESTION_PAGE_AUTHOR_TEXT, attribute_name="text"
        )

        return expected_nick_name, actual_nick_name
