from appium.webdriver.common.mobileby import MobileBy

from objects.base_page import BasePage


class IosMarketsListPage(BasePage):

    # static xpath. used as is
    __MARKET_PAGE_MARKET_NAME_BUTTON = (MobileBy.ACCESSIBILITY_ID, "CODETEST XF")
    __MARKET_PAGE_CONFIRM_BUTTON = (MobileBy.IOS_PREDICATE, 'label == "CONFIRM"')

    def change_to_test_market(self):
        """
        Select test market from the list
        """
        self.click(by_locator=self.__MARKET_PAGE_MARKET_NAME_BUTTON)
        self.click(by_locator=self.__MARKET_PAGE_CONFIRM_BUTTON)
