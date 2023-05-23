from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.UsersAndGroups import selected_users_locators as locators
from Libraries.Drivers.base_page import BasePage


class SelectedUsersObjects(BasePage):
    """This class represents the selected users page of a Blueprint application"""

    def get_input_search_selected(self) -> WebElement:
        """Finds and returns the input element for searching selected users."""
        element = self.find_element.by_xpath(locators.INPUT_SEARCH_SELECTED)
        return element

    def get_selected_username_result(self, index: str) -> WebElement:
        """Finds and returns the username result element in the selected users section."""
        result_by_index = locators.SELECTED_USERNAME_RESULT + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element

    def get_selected_email_result(self, index: str) -> WebElement:
        """Finds and returns the email result element in the selected users section."""
        result_by_index = locators.SELECTED_EMAIL_RESULT + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element

    def get_selected_user_remove_button(self, index: str) -> WebElement:
        """Finds and returns the remove button element for a selected user."""
        result_by_index = locators.SELECTED_USER_REMOVE_BUTTON + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element
