from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.UsersAndGroups import groups_locators as locators
from Libraries.Drivers.base_page import BasePage


class GroupsObjects(BasePage):
    """This class represents the groups page of a Blueprint application"""

    def get_input_search_groups(self) -> WebElement:
        """Finds and returns the input field for searching groups."""
        element = self.find_element.by_xpath(locators.INPUT_SEARCH_GROUPS)
        return element

    def get_group_result(self, index: str) -> WebElement:
        """Finds and returns the first group result on the page."""
        result_by_index = locators.GROUP_RESULT + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element

    def get_group_result_dropdown_menu(self, index: str) -> WebElement:
        """Finds and returns the dropdown menu button for the first group result."""
        result_by_index = locators.GROUP_RESULT_DROPDOWN_MENU + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element

    def get_group_result_edit_button(self, index: str) -> WebElement:
        """Finds and returns the edit button for the first group result."""
        result_by_index = locators.GROUP_RESULT_EDIT_BUTTON + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element

    def get_group_result_delete_button(self, index: str) -> WebElement:
        """Finds and returns the delete button for the first group result."""
        result_by_index = locators.GROUP_RESULT_DELETE_BUTTON + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element

    def get_new_group_button(self) -> WebElement:
        """Finds and returns the 'New Group' button on the page."""
        element = self.find_element.by_xpath(locators.NEW_GROUP_BUTTON)
        return element

    def get_input_group_name(self) -> WebElement:
        """Finds and returns the input field for entering the group name."""
        element = self.find_element.by_xpath(locators.INPUT_GROUP_NAME)
        return element

    def get_cancel_create_group_button(self) -> WebElement:
        """Finds and returns the 'Cancel' button for creating a new group."""
        element = self.find_element.by_xpath(locators.CANCEL_CREATE_GROUP_BUTTON)
        return element

    def get_primary_group_button(self) -> WebElement:
        """Finds and returns the 'Create' button for creating a new group."""
        element = self.find_element.by_xpath(locators.PRIMARY_GROUP_BUTTON)
        return element
