from selenium.webdriver.common.by import By

from objects.base_page import BasePage


class AndroidUserProfilePage(BasePage):

    # static xpath. used as is
    __USER_PROFILE_PAGE_NICKNAME = (By.ID, "tv_profile_nick")

    def get_actual_and_expected_user_nicknames(self):
        """
        Check if correct user nck name is presented on the page
        """
        user = self.get_env_user()
        expected_nick_name = user["login"]
        actual_nick_name = self.get_element_attribute(
            by_locator=self.__USER_PROFILE_PAGE_NICKNAME, attribute_name="text"
        )
        return expected_nick_name, actual_nick_name
