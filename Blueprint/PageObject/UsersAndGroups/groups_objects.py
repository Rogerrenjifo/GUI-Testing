from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.UsersAndGroups import groups_locators as locators
from Libraries.Drivers.base_page import BasePage


class GroupsObjects(BasePage):
    """This class represents the groups page of a Blueprint application"""

    def __init__(self, driver):
        super().__init__(driver)
        self.__input_search_groups = locators.INPUT_SEARCH_GROUPS
        self.__first_group_result = locators.FIRST_GROUP_RESULT
        self.__first_group_result_dropdown_menu = locators.FIRST_GROUP_RESULT_DROPDOWN_MENU
        self.__first_group_result_edit_button = locators.FIRST_GROUP_RESULT_EDIT_BUTTON
        self.__first_group_result_delete_button = locators.FIRST_GROUP_RESULT_DELETE_BUTTON
        self.__new_group_button = locators.NEW_GROUP_BUTTON
        self.__input_group_name = locators.INPUT_GROUP_NAME
        self.__cancel_create_group_button = locators.CANCEL_CREATE_GROUP_BUTTON
        self.__create_group_button = locators.CREATE_GROUP_BUTTON

    def get_input_search_groups(self) -> WebElement:
        """Finds and returns the input field for searching groups."""
        element = self.find_element.by_xpath(self.__input_search_groups)
        return element

    def get_first_group_result(self) -> WebElement:
        """Finds and returns the first group result on the page."""
        element = self.find_element.by_xpath(self.__first_group_result)
        return element

    def get_first_group_result_dropdown_menu(self) -> WebElement:
        """Finds and returns the dropdown menu button for the first group result."""
        element = self.find_element.by_xpath(self.__first_group_result_dropdown_menu)
        return element

    def get_first_group_result_edit_button(self) -> WebElement:
        """Finds and returns the edit button for the first group result."""
        element = self.find_element.by_xpath(self.__first_group_result_edit_button)
        return element

    def get_first_group_result_delete_button(self) -> WebElement:
        """Finds and returns the delete button for the first group result."""
        element = self.find_element.by_xpath(self.__first_group_result_delete_button)
        return element

    def get_new_group_button(self) -> WebElement:
        """Finds and returns the 'New Group' button on the page."""
        element = self.find_element.by_xpath(self.__new_group_button)
        return element

    def get_input_group_name(self) -> WebElement:
        """Finds and returns the input field for entering the group name."""
        element = self.find_element.by_xpath(self.__input_group_name)
        return element

    def get_cancel_create_group_button(self) -> WebElement:
        """Finds and returns the 'Cancel' button for creating a new group."""
        element = self.find_element.by_xpath(self.__cancel_create_group_button)
        return element

    def get_create_group_button(self) -> WebElement:
        """Finds and returns the 'Create' button for creating a new group."""
        element = self.find_element.by_xpath(self.__create_group_button)
        return element
