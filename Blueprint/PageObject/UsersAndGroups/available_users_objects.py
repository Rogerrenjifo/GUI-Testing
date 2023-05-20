from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.UsersAndGroups import available_users_locators as locators
from Libraries.Drivers.base_page import BasePage


class AvailableUsersObjects(BasePage):
    """This class represents the user page of a Blueprint application"""

    def __init__(self, driver):
        super().__init__(driver)
        self.__input_search_users = locators.INPUT_SEARCH_USERS
        self.__user_result = locators.USERNAME_RESULT
        self.__email_result = locators.EMAIL_RESULT
        self.__user_result_add_button = locators.USER_RESULT_ADD_BUTTON
        self.__new_user_button = locators.NEW_USER_BUTTON
        self.__input_user_name = locators.INPUT_USER_NAME
        self.__cancel_create_user_button = locators.CANCEL_CREATE_USER_BUTTON
        self.__create_user_button = locators.CREATE_USER_BUTTON

    def get_input_search_users(self) -> WebElement:
        """Finds and returns the input element for searching users."""
        element = self.find_element.by_xpath(self.__input_search_users)
        return element

    def get_user_result(self, index: str) -> WebElement:
        """Finds and returns the user result element."""
        result_by_index = self.__user_result + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element

    def get_email_result_add_button(self, index: str) -> WebElement:
        """Finds and returns the add button element in the user result section."""
        result_by_index = self.__email_result + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element

    def get_user_result_add_button(self, index: str) -> WebElement:
        """Finds and returns the add button element in the user result section."""
        result_by_index = self.__user_result_add_button + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element

    def get_new_user_button(self) -> WebElement:
        """Finds and returns the new user button element."""
        element = self.find_element.by_xpath(self.__new_user_button)
        return element

    def get_input_user_name(self) -> WebElement:
        """Finds and returns the input element for username."""
        element = self.find_element.by_xpath(self.__input_user_name)
        return element

    def get_cancel_create_user_button(self) -> WebElement:
        """Finds and returns the cancel button element for creating a user."""
        element = self.find_element.by_xpath(self.__cancel_create_user_button)
        return element

    def get_create_user_button(self) -> WebElement:
        """Finds and returns the create button element for creating a user."""
        element = self.find_element.by_xpath(self.__create_user_button)
        return element
