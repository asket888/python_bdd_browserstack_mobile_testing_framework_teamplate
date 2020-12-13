from typing import Tuple, List, Dict

from behave.runner import Context
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from selenium.webdriver.remote import webelement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage:
    __IMPLICIT_TIMEOUT = 0
    __EXPLICIT_TIMEOUT = 10

    def __init__(self, context: Context):
        self.os = context.os
        self.env = context.env
        self.driver = context.driver
        self.driver.implicitly_wait(BasePage.__IMPLICIT_TIMEOUT)
        self.explicitly_wait = WebDriverWait(
            self.driver,
            BasePage.__EXPLICIT_TIMEOUT,
            ignored_exceptions=(NoSuchElementException, StaleElementReferenceException),
        )

    # element wait methods
    def __is_element_visible(self, by_locator: Tuple[By, str]):
        """
        Wait till element will appear in DOM model
        :param by_locator: tuple parameter with type of locator and its value (By.ID, "submit")
        """
        self.explicitly_wait.until(
            EC.presence_of_element_located(by_locator), message=f"'{by_locator}' element doesn't appear on the page"
        )

    def __is_element_clickable(self, by_locator: Tuple[By, str]):
        """
        Wait till element will appear in DOM model and will be clickable
        :param by_locator: tuple parameter with type of locator and its value (By.ID, "submit")
        """
        self.explicitly_wait.until(
            EC.element_to_be_clickable(by_locator), message=f"'{by_locator}' element is not clickable on the page"
        )

    # element status methods
    def if_element_displayed(self, by_locator: Tuple[By, str]) -> bool:
        """
        Check if element is presented on the page
        :param by_locator: tuple parameter with type of locator and its value (By.ID, "submit")
        :returns boolean parameter True if element is displayed
        """
        self.__is_element_visible(by_locator)
        return True

    def if_element_not_displayed(self, by_locator: Tuple[By, str]) -> bool:
        """
        Check if element is not presented on the page
        :param by_locator: tuple parameter with type of locator and its value (By.ID, "submit")
        :returns boolean parameter True if element is NOT displayed
        """
        try:
            self.driver.find_element(*by_locator)
        except NoSuchElementException:
            return True
        return False

    # elements set action methods
    def click(self, by_locator: Tuple[By, str]):
        """
        Click an element
        :param by_locator: tuple parameter with type of locator and its value (By.ID, "submit")
        """
        self.__is_element_clickable(by_locator)
        self.driver.find_element(*by_locator).click()

    def clear(self, by_locator: Tuple[By, str]):
        """
        Clear text field
        :param by_locator: tuple parameter with type of locator and its value (By.ID, "submit")
        """
        self.__is_element_visible(by_locator)
        self.driver.find_element(*by_locator).clear()

    def fill(self, by_locator: Tuple[By, str], value: str):
        """
        Type text in webelement
        :param by_locator: tuple parameter with type of locator and its value (By.ID, "submit")
        :param value: string to be typed
        """
        self.__is_element_visible(by_locator)
        self.driver.find_element(*by_locator).send_keys(value)

    def select(self, by_locator: Tuple[By, str]):
        """
        Click an element without checking if it's clickable (checkbox, option, div)
        :param by_locator: tuple parameter with type of locator and its value (By.ID, "submit")
        """
        self.__is_element_visible(by_locator)
        self.driver.find_element(*by_locator).click()

    # elements get action methods
    def get_element(self, by_locator: Tuple[By, str]) -> webelement:
        """
        Return one element as webelement
        :param by_locator: tuple parameter with type of locator and its value (By.ID, "submit")
        :returns text from an element
        """
        self.__is_element_visible(by_locator)
        return self.driver.find_element(*by_locator)

    def get_all_elements(self, by_locator: Tuple[By, str]) -> List[object]:
        """
        Return all elements with the same locator as a list of webelements
        :param by_locator: tuple parameter with type of locator and its value (By.ID, "submit")
        :returns list with all elements matched to locator
        """
        self.__is_element_visible(by_locator)
        return self.driver.find_elements(*by_locator)

    def get_element_attribute(self, by_locator: Tuple[By, str], attribute_name: str) -> str:
        """
        Return one element's attribute value
        :param by_locator: tuple parameter with type of locator and its value (By.ID, "submit")
        :param attribute_name: attribute to be found ("value", "name", "text")
        :returns attribute value as a string
        """
        self.__is_element_visible(by_locator)
        return self.driver.find_element(*by_locator).get_attribute(attribute_name)

    def get_all_elements_attributes(self, by_locator: Tuple[By, str], attribute_name: str) -> List:
        """
        Return all element's attribute values
        :param by_locator: tuple parameter with type of locator and its value (By.ID, "submit")
        :param attribute_name: attribute to be found ("value", "name", "text")
        :returns list with all element's attribute values
        """
        self.__is_element_visible(by_locator)
        elements = self.driver.find_elements(*by_locator)
        elements_attribute = [i.get_attribute(attribute_name) for i in elements]
        return elements_attribute

    # overall mobile actions
    def refresh_page(self):
        """
        Refresh current browser page
        """
        self.driver.refresh()

    def hide_keyboard(self):
        """
        Hide mobile virtual keyboard
        """
        self.driver.hide_keyboard()

    def execute_javascript(self, script: str) -> object:
        """
        Return javascript execution result
        :param script: javascript code that should be executed
        """
        return self.driver.execute_script(script)

    # environment data provider
    def get_env_user(self) -> Dict:
        """
        Get environment user data from config.json
        """
        return self.env["app"]["user"]
