from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.MainMenu import main_menu_locators as locators
from Libraries.Drivers.base_page import BasePage


class MainMenuObjects(BasePage):
    """This class represents the Main Menu of the Blueprint application"""

    def __init__(self):
        super().__init__()

    def get_my_inbox_button(self) -> WebElement:
        """Finds and returns the 'My Inbox' button element on the page."""
        element = self.find_element.by_xpath(locators.MY_INBOX_BUTTON)
        return element

    def get_projects_button(self) -> WebElement:
        """Finds and returns the 'Projects' button element on the page."""
        element = self.find_element.by_xpath(locators.PROJECTS_BUTTON)
        return element

    def get_reports_button(self) -> WebElement:
        """Finds and returns the 'Reports' button element on the page."""
        element = self.find_element.by_xpath(locators.REPORTS_BUTTON)
        return element

    def get_flows_button(self) -> WebElement:
        """Finds and returns the 'Flows' button element on the page."""
        element = self.find_element.by_xpath(locators.FLOWS_BUTTON)
        return element

    def get_users_and_groups_button(self) -> WebElement:
        """Finds and returns the 'Users and Groups' button element on the page."""
        element = self.find_element.by_xpath(locators.USERS_AND_GROUPS_BUTTON)
        return element

    def get_search_projects_input(self) -> WebElement:
        """Finds and returns the search input element for projects on the page"""
        element = self.find_element.by_xpath(locators.SEARCH_INPUT_PROJECTS)
        return element

    def get_search_flows_input(self) -> WebElement:
        """Finds and returns the search input element for flows on the page."""
        element = self.find_element.by_xpath(locators.SEARCH_INPUT_FLOWS)
        return element

    def get_project_result(self, index: str) -> WebElement:
        """Finds and returns a project result element on the page by index."""
        result_by_index = locators.PROJECT_RESULT + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element

    def get_flow_result(self, index: str) -> WebElement:
        """Finds and returns a flow result element on the page by index."""
        result_by_index = locators.FLOW_RESULT + "[" + index + "]"
        element = self.find_element.by_xpath(result_by_index)
        return element

    def get_new_flow_button(self) -> WebElement:
        """Finds and returns the new flow button element on the page."""
        element = self.find_element.by_xpath(locators.NEW_FLOW_BUTTON)
        return element

    def get_no_data_match_found_message(self) -> WebElement:
        """Finds and returns the no data match found message on the page."""
        element = self.find_element.by_xpath(locators.NO_DATA_MATCH_FOUND)
        return element

    def get_create_flow_dialog(self) -> WebElement:
        """Finds and returns the Create Flow dialog on the page."""
        element = self.find_element.by_xpath(locators.CREATE_FLOW_DIALOG)
        return element

    def get_main_menu_container(self) -> WebElement:
        """Finds and returns the new main menu container."""
        element = self.find_element.by_xpath(locators.MAIN_MENU_CONTAINER)
        return element
