from appium.webdriver.common.mobileby import MobileBy

from objects.base_page import BasePage


class IosUserProfilePage(BasePage):

    # dynamic xpath template. should be transformed to (By.XPATH, "xpath") before use
    __USER_PROFILE_PAGE_NICKNAME_TEMPLATE = "{nick_name}"

    def check_if_user_nickname_is_presented(self):
        """
        Get user name from the page
        """
        user = self.get_env_user()
        expected_nick_name = user["login"]
        nick_name_locator = (
            MobileBy.ACCESSIBILITY_ID,
            self.__USER_PROFILE_PAGE_NICKNAME_TEMPLATE.format(nick_name=expected_nick_name),
        )
        return self.if_element_displayed(by_locator=nick_name_locator)
