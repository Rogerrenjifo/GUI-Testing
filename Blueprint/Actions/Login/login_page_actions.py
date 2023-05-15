import os
from Blueprint.PageObject.Login.login_page_objects import LoginPageObjects


class LoginPageActions(LoginPageObjects):
    """This class represents the login page of a Blueprint application"""

    def login(self, user: str = os.environ.get("USER"), password: str = os.environ.get("PASSWORD")):
        """Log in user with given credentials"""
        self.insert_username(user)
        self.insert_password(password)
        self.get_sign_in_button_element().click()

    def insert_username(self, user: str = os.environ.get("USER")):
        """Insert the username got from env file"""
        self.get_username_element().send_keys(user)

    def insert_password(self, password: str = os.environ.get("PASSWORD")):
        """Insert the password got from env file"""
        self.get_password_element().send_keys(password)

    def press_sign_button(self):
        """Press the sign button in the login page"""
        self.get_sign_in_button_element().click()
