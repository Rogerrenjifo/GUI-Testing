import os
from Blueprint.PageObject.Login.login_page_objects import LoginPageObjects
from Libraries.Drivers.find_elements import *


class LoginPageActions(LoginPageObjects):
    """This class represents the login page of a Blueprint application"""

    def get_header(self) -> WebElement:
        """Finds and returns the header element of the page."""
        element = self.find_element.by_id(self.header)
        return element

    def get_title(self) -> WebElement:
        """Finds and returns the title element of the page."""
        element = self.find_element.by_id(self.title)
        return element

    def get_username_label(self) -> WebElement:
        """Finds and returns the label element for the username input field."""
        element = self.find_element.by_xpath(self.username_label)
        return element

    def get_password_label(self) -> WebElement:
        """Finds and returns the label element for the password input field."""
        element = self.find_element.by_xpath(self.password_label)
        return element

    def insert_user(self):
        """Inserts the value of the 'USER' environment variable into the username input field."""
        self.find_element.by_id(self.input_username).send_keys(os.environ.get("USER"))

    def insert_password(self):
        """Inserts the value of the 'PASSWORD' environment variable into the password input field."""
        self.find_element.by_id(self.input_password).send_keys(os.environ.get("PASSWORD"))

    def click_in_sign_button(self):
        """Clicks the sign-in button element"""
        self.find_element.by_id(self.sign_in_button).click()
