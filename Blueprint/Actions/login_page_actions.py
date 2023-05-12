import os
from Blueprint.PageObject import login_page_locators as locators
from Libraries.DataProcessors.find_elements import *
from Libraries.DataProcessors.driver import Driver
from selenium import webdriver


class LoginPage(Driver):
    """This class represents the login page of a Blueprint application"""
    _instance = None
    header_locator = locators.HEADER_LOCATOR
    input_username_locator = locators.INPUT_LOCATOR
    input_password_locator = locators.PASSWORD_LOCATOR
    sign_in_button_locator = locators.SIGN_IN_BUTTON_LOCATOR
    title_locator = locators.TITLE_LOCATOR
    username_label_locator = locators.USERNAME_LABEL_LOCATOR
    password_label_locator = locators.PASSWORD_LABEL_LOCATOR
    URL_LOGIN = locators.URL  # Move to URL class

    def __new__(cls):
        """Creates a unique instance of the session. Returns the created instance of the class."""
        if not cls._instance:
            cls._instance = super(LoginPage, cls).__new__(cls)
            cls._instance.driver = getattr(webdriver, os.environ.get("BROWSER"))()
            cls._instance.driver.get(cls.URL_LOGIN)
            # cls. navigate_to_url(cls._instance.driver, cls.URL_LOGIN)
        return cls._instance

    def get_header(self) -> WebElement:
        """Finds and returns the header element of the page."""
        element = self.find_element.by_id("kc-header")
        print(element)
        return element

    def get_title(self) -> WebElement:
        """Finds and returns the title element of the page."""
        element = self.find_element.by_id(self.title_locator)
        return element

    def get_username_label(self) -> WebElement:
        """Finds and returns the label element for the username input field."""
        element = self.find_element.by_xpath(self.username_label_locator)
        return element

    def get_password_label(self) -> WebElement:
        """Finds and returns the label element for the password input field."""
        element = self.find_element.by_xpath(self.password_label_locator)
        return element

    def insert_user(self):
        """Inserts the value of the 'USER' environment variable into the username input field."""
        self.find_element.by_id(self.input_username_locator).send_keys(os.environ.get("USER"))

    def insert_password(self):
        """Inserts the value of the 'PASSWORD' environment variable into the password input field."""
        self.find_element.by_id(self.input_password_locator).send_keys(os.environ.get("PASSWORD"))

    def click_in_sign_button(self):
        """Clicks the sign-in button element"""
        self.find_element.by_id(self.sign_in_button_locator).click()

    def navigate_to_given_url(self, url):
        """Navigates to the given URL using the LoginPage instance"""
        self.browser.navigate_to_url(url)

    def close_open_browser(self):
        """Closes the provided browser driver instance"""
        self.browser.close_browser()
