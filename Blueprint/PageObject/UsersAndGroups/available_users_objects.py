from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.UsersAndGroups import available_users_locators as locators
from Libraries.Drivers.base_page import BasePage


class AvailableUsersObjects(BasePage):
    """This class represents the user page of a Blueprint application"""

    def get_input_search_users(self) -> WebElement:
        """Finds and returns the input element for searching users."""
        element = self.find_element.by_xpath(locators.INPUT_SEARCH_USERS)
        return element

    def get_user_result(self, index: str) -> WebElement:
        """Finds and returns the user result element."""
        result_by_index = locators.USERNAME_RESULT + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element

    def get_email_result_add_button(self, index: str) -> WebElement:
        """Finds and returns the add button element in the user result section."""
        result_by_index = locators.EMAIL_RESULT + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element

    def get_user_result_add_button(self, index: str) -> WebElement:
        """Finds and returns the add button element in the user result section."""
        result_by_index = locators.USER_RESULT_ADD_BUTTON + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element

    def get_new_user_button(self) -> WebElement:
        """Finds and returns the new user button element."""
        element = self.find_element.by_xpath(locators.NEW_USER_BUTTON)
        return element

    def get_input_user_name(self) -> WebElement:
        """Finds and returns the input element for username."""
        element = self.find_element.by_xpath(locators.INPUT_USER_NAME)
        return element

    def get_cancel_create_user_button(self) -> WebElement:
        """Finds and returns the cancel button element for creating a user."""
        element = self.find_element.by_xpath(locators.CANCEL_CREATE_USER_BUTTON)
        return element

    def get_create_user_button(self) -> WebElement:
        """Finds and returns the create button element for creating a user."""
        element = self.find_element.by_xpath(locators.CREATE_USER_BUTTON)
        return element
