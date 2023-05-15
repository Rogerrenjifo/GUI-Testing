from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Login import login_page_locators as locators
from Libraries.Drivers.base_page import BasePage


class LoginPageObjects(BasePage):
    """This class represents the login page of a Blueprint application"""

    def __init__(self, driver):
        super().__init__(driver)
        self.__header = locators.HEADER_LOCATOR
        self.__input_username = locators.INPUT_LOCATOR
        self.__input_password = locators.PASSWORD_LOCATOR
        self.__sign_in_button = locators.SIGN_IN_BUTTON_LOCATOR
        self.__title = locators.TITLE_LOCATOR
        self.__username_label = locators.USERNAME_LABEL_LOCATOR
        self.__password_label = locators.PASSWORD_LABEL_LOCATOR
        self.__URL_LOGIN = locators.URL

    def get_header(self) -> WebElement:
        """Finds and returns the header element of the page."""
        element = self.find_element.by_id(self.__header)
        return element

    def get_title(self) -> WebElement:
        """Finds and returns the title element of the page."""
        element = self.find_element.by_id(self.__title)
        return element

    def get_username_label(self) -> WebElement:
        """Finds and returns the label element for the username input field."""
        element = self.find_element.by_xpath(self.__username_label)
        return element

    def get_password_label(self) -> WebElement:
        """Finds and returns the label element for the password input field."""
        element = self.find_element.by_xpath(self.__password_label)
        return element

    def get_username_element(self) -> WebElement:
        """Inserts the value of the 'USER' environment variable into the username input field."""
        element = self.find_element.by_id(self.__input_username)
        return element

    def get_password_element(self) -> WebElement:
        """Inserts the value of the 'PASSWORD' environment variable into the password input field."""
        element = self.find_element.by_id(self.__input_password)
        return element

    def get_sign_in_button_element(self) -> WebElement:
        """Clicks the sign-in button element"""
        element = self.find_element.by_id(self.__sign_in_button)
        return element
