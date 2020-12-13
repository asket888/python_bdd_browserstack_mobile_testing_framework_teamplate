from appium.webdriver.common.mobileby import MobileBy

from objects.base_page import BasePage


class AndriodMainMenuSection(BasePage):

    # dynamic xpath template. should be transformed to (By.XPATH, "xpath") before use
    __MAIN_MENU_TAB_TEMPLATE = "{tab_name}"

    def click_navigation_tab(self, tab_name: str):
        """
        Click tab on the main page (Ask, Answer or Me)
        """
        tab_locator = (MobileBy.ACCESSIBILITY_ID, self.__MAIN_MENU_TAB_TEMPLATE.format(tab_name=tab_name))
        self.click(by_locator=tab_locator)
