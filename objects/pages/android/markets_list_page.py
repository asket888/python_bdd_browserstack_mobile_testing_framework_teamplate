from selenium.webdriver.common.by import By

from objects.base_page import BasePage


class AndroidMarketsListPage(BasePage):

    # static xpath. used as is
    __MARKET_PAGE_MARKET_NAME_BUTTON = (By.XPATH, "//android.widget.LinearLayout[13]")
    __MARKET_PAGE_CONFIRM_BUTTON = (By.ID, "primary_cta")

    def go_to_test_market(self):
        """
        Select market from the list
        """
        self.click(by_locator=self.__MARKET_PAGE_MARKET_NAME_BUTTON)
        self.click(by_locator=self.__MARKET_PAGE_CONFIRM_BUTTON)
