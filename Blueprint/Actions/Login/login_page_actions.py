import os
from Blueprint.PageObject.Login.login_page_objects import LoginPageObjects


class LoginPageActions(LoginPageObjects):
    """This class represents the login page of the Blueprint application"""

    def login(self, user: str = os.environ.get("USER"), password: str = os.environ.get("PASSWORD")):
        """Log in user with given credentials"""
        self.insert_username_or_email(user)
        self.insert_password(password)
        self.click_on_sign_in_button()

    def insert_username_or_email(self, user: str = os.environ.get("USER")):
        """Inserts the username got from env file"""
        self.get_username_element().send_keys(user)

    def insert_password(self, password: str = os.environ.get("PASSWORD")):
        """Inserts the password got from env file"""
        self.get_password_element().send_keys(password)

    def click_on_sign_in_button(self):
        """Clicks on the Sign-In button in the login page"""
        self.get_sign_in_button_element().click()
