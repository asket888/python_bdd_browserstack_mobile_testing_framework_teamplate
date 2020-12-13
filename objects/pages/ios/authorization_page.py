from appium.webdriver.common.mobileby import MobileBy

from objects.base_page import BasePage


class IosLoginPage(BasePage):

    # static xpath. used as is
    __LOGIN_PAGE_USERNAME_FIELD = (MobileBy.IOS_PREDICATE, 'value == "Username or email"')
    __LOGIN_PAGE_PASSWORD_FIELD = (MobileBy.IOS_PREDICATE, 'value == "Password"')
    __LOGIN_PAGE_LOG_IN_BUTTON = (MobileBy.IOS_PREDICATE, 'value == "LOG IN"')
    __LOGIN_PAGE_CHANGE_MARKET_BUTTON = (MobileBy.IOS_PREDICATE, 'label == "Change here"')

    def login_with_correct_parameters(self):
        """
        Login to application with correct parameters
        """
        user = self.get_env_user()
        login = user["login"]
        password = user["password"]
        self.fill(by_locator=self.__LOGIN_PAGE_USERNAME_FIELD, value=login)
        self.fill(by_locator=self.__LOGIN_PAGE_PASSWORD_FIELD, value=password)
        self.click(by_locator=self.__LOGIN_PAGE_LOG_IN_BUTTON)

    def click_change_market_button(self):
        """
        Click change market button
        """
        self.click(by_locator=self.__LOGIN_PAGE_CHANGE_MARKET_BUTTON)
