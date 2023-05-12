from Blueprint.Locators.Login import login_page_locators as locators
from Libraries.Drivers.base_page import BasePage


class LoginPageObjects(BasePage):
    """This class represents the login page of a Blueprint application"""
    _instance = None

    def __init__(self, driver):
        super().__init__(driver)
        self.header = locators.HEADER_LOCATOR
        self.input_username = locators.INPUT_LOCATOR
        self.input_password = locators.PASSWORD_LOCATOR
        self.sign_in_button = locators.SIGN_IN_BUTTON_LOCATOR
        self.title = locators.TITLE_LOCATOR
        self.username_label = locators.USERNAME_LABEL_LOCATOR
        self.password_label = locators.PASSWORD_LABEL_LOCATOR
        self.URL_LOGIN = locators.URL  # Move to URL class
