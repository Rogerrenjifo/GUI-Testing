from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.UsersAndGroups import selected_users_locators as locators
from Libraries.Drivers.base_page import BasePage


class SelectedUsersObjects(BasePage):
    """This class represents the selected users page of a Blueprint application"""

    def __init__(self, driver):
        super().__init__(driver)
        self.__input_search_selected = locators.INPUT_SEARCH_SELECTED
        self.__selected_username_result = locators.SELECTED_USERNAME_RESULT
        self.__selected_email_result = locators.SELECTED_EMAIL_RESULT
        self.__selected_user_remove_button = locators.SELECTED_USER_REMOVE_BUTTON

    def get_input_search_selected(self) -> WebElement:
        """Finds and returns the input element for searching selected users."""
        element = self.find_element.by_xpath(self.__input_search_selected)
        return element

    def get_selected_username_result(self, index: str) -> WebElement:
        """Finds and returns the username result element in the selected users section."""
        result_by_index = self.__selected_username_result + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element

    def get_selected_email_result(self, index: str) -> WebElement:
        """Finds and returns the email result element in the selected users section."""
        result_by_index = self.__selected_email_result + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element

    def get_selected_user_remove_button(self, index: str) -> WebElement:
        """Finds and returns the remove button element for a selected user."""
        result_by_index = self.__selected_user_remove_button + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element
