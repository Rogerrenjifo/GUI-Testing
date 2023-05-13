import os
from Blueprint.PageObject.Login.login_page_objects import LoginPageObjects


class LoginPageActions(LoginPageObjects):
    """This class represents the login page of a Blueprint application"""

    def login(self):
        """Logs a user with given credentials"""
        self.get_username_element().send_keys(os.environ.get("USER"))
        self.get_password_element().send_keys(os.environ.get("PASSWORD"))
        self.get_sign_button_element().click()

    def insert_username(self):
        self.get_username_element().send_keys(os.environ.get("USER"))

    def insert_password(self):
        self.get_password_element().send_keys(os.environ.get("PASSWORD"))

    def press_sign_button(self):
        self.get_sign_button_element().click()
