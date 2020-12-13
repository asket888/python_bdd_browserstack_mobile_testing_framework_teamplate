from appium.webdriver.common.mobileby import MobileBy

from objects.base_page import BasePage


class IosQuestionPage(BasePage):

    # static xpath. used as is
    __QUESTION_PAGE_QUESTION_DETAILS = (MobileBy.ACCESSIBILITY_ID, "ewQuestionDetailsView")

    def check_if_question_page_is_presented(self):
        """
        Check if question page is presented
        """
        return self.if_element_displayed(by_locator=self.__QUESTION_PAGE_QUESTION_DETAILS)
