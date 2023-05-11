import os
from Blueprint.PageObject.login_page_locators import *
from Libraries.DataProcessors.find_elements import *
from Libraries.DataProcessors.browser import *
from selenium import webdriver


class LoginPage:
    """This class represents the login page of a Blueprint application"""
    _instance = None
    header_locator = HEADER_LOCATOR
    input_username_locator = INPUT_LOCATOR
    input_password_locator = PASSWORD_LOCATOR
    sign_in_button_locator = SIGN_IN_BUTTON_LOCATOR
    title_locator = TITLE_LOCATOR
    username_label_locator = USERNAME_LABEL_LOCATOR
    password_label_locator = PASSWORD_LABEL_LOCATOR
    URL_LOGIN = URL

    def __new__(cls):
        """Creates a unique instance of the session. Returns the created instance of the class."""
        if not cls._instance:
            cls._instance = super(LoginPage, cls).__new__(cls)
            cls._instance.driver = getattr(webdriver, os.environ.get("BROWSER"))()
            navigate_to_url(cls._instance.driver, cls.URL_LOGIN)
        return cls._instance

    def get_header(self) -> WebElement:
        """Finds and returns the header element of the page."""
        element = find_element(self.driver, By.ID, self.header_locator)
        return element

    def get_title(self) -> WebElement:
        """Finds and returns the title element of the page."""
        element = find_element_by_id(self.driver, self.title_locator)
        return element

    def get_username_label(self) -> WebElement:
        """Finds and returns the label element for the username input field."""
        element = find_element_by_xpath(self.driver, self.username_label_locator)
        return element

    def get_password_label(self) -> WebElement:
        """Finds and returns the label element for the password input field."""
        element = find_element_by_xpath(self.driver, self.password_label_locator)
        return element

    def insert_user(self):
        """Inserts the value of the 'USER' environment variable into the username input field."""
        find_element_by_id(self.driver, self.input_username_locator).send_keys(os.environ.get("USER"))

    def insert_password(self):
        """Inserts the value of the 'PASSWORD' environment variable into the password input field."""
        find_element_by_id(self.driver, self.input_password_locator).send_keys(os.environ.get("PASSWORD"))

    def click_in_sign_button(self):
        """Clicks the sign-in button element"""
        find_element_by_id(self.driver, self.sign_in_button_locator).click()

    def navigate_to_given_url(self, url):
        """Navigates to the given URL using the LoginPage instance"""
        navigate_to_url(self.driver, url)

    def close_open_browser(self):
        """Closes the provided browser driver instance"""
        close_browser(self.driver)
