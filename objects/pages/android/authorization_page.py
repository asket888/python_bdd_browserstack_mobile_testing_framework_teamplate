from selenium.webdriver.common.by import By

from objects.base_page import BasePage


class AndroidLoginPage(BasePage):

    # static xpath. used as is
    __LOGIN_PAGE_USERNAME_FIELD = (
        By.XPATH,
        '//android.widget.LinearLayout[@resource-id="login_username"]/android.widget'
        '.FrameLayout/android.widget.EditText',
    )
    __LOGIN_PAGE_PASSWORD_FIELD = (
        By.XPATH,
        '//android.widget.LinearLayout[@resource-id="login_password"]/android.widget'
        '.FrameLayout/android.widget.EditText',
    )
    __LOGIN_PAGE_LOG_IN_BUTTON = (By.ID, "login_button")

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
