from selenium.webdriver.common.by import By

from objects.base_page import BasePage


class AndriodSearchByImagePage(BasePage):

    # static xpath. used as is
    __SEARCH_BY_IMAGE_SCAN_AND_SOLVE_BUTTON = (By.ID, "home_camera_start")
    __SEARCH_BY_IMAGE_BY_TEXT_BUTTON = (
        By.XPATH,
        "//android.widget.LinearLayout[@resource-id='page_indicator_icon_container']/android."
        "widget.ImageView[1]",
    )

    def check_if_search_by_image_page_is_presented(self):
        """
        Check if Search by Image page is presented
        """
        return self.if_element_displayed(by_locator=self.__SEARCH_BY_IMAGE_SCAN_AND_SOLVE_BUTTON)

    def click_search_by_text_button(self):
        """
        Click [Search by text] button on main page
        """
        self.click(by_locator=self.__SEARCH_BY_IMAGE_BY_TEXT_BUTTON)
