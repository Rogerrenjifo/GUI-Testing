from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.MainMenu import main_menu_locators as locators
from Libraries.Drivers.base_page import BasePage


class MainMenuObjects(BasePage):
    """This class represents the Main Menu of the Blueprint application"""

    def __init__(self):
        super().__init__()
        self.__first_flow_result = locators.FIRST_FLOW_RESULT
        self.__first_project_result = locators.FIRST_PROJECT_RESULT
        self.__flows_button = locators.FLOWS_BUTTON
        self.__my_inbox_button = locators.MY_INBOX_BUTTON
        self.__projects_button = locators.PROJECTS_BUTTON
        self.__projects_results = locators.PROJECT_RESULTS
        self.__reports_button = locators.REPORTS_BUTTON
        self.__search_flows = locators.SEARCH_INPUT_FLOWS
        self.__search_projects = locators.SEARCH_INPUT_PROJECTS
        self.__users_and_groups_button = locators.USERS_AND_GROUPS_BUTTON
        self.__new_flow_button = locators.NEW_FLOW_BUTTON

    def get_my_inbox_button(self) -> WebElement:
        """Finds and returns the 'My Inbox' button element on the page."""
        element = self.find_element.by_xpath(self.__my_inbox_button)
        return element

    def get_projects_button(self) -> WebElement:
        """Finds and returns the 'Projects' button element on the page."""
        element = self.find_element.by_xpath(self.__projects_button)
        return element

    def get_reports_button(self) -> WebElement:
        """Finds and returns the 'Reports' button element on the page."""
        element = self.find_element.by_xpath(self.__reports_button)
        return element

    def get_flows_button(self) -> WebElement:
        """Finds and returns the 'Flows' button element on the page."""
        element = self.find_element.by_xpath(self.__flows_button)
        return element

    def get_users_and_groups_button(self) -> WebElement:
        """Finds and returns the 'Users and Groups' button element on the page."""
        element = self.find_element.by_xpath(self.__users_and_groups_button)
        return element

    def get_search_projects_input(self) -> WebElement:
        """Finds and returns the search input element for projects on the page"""
        element = self.find_element.by_xpath(self.__search_projects)
        return element

    def get_search_flows_input(self) -> WebElement:
        """Finds and returns the search input element for flows on the page."""
        element = self.find_element.by_xpath(self.__search_flows)
        return element

    def get_first_project_result(self) -> WebElement:
        """Finds and returns the first project result element on the page."""
        element = self.find_element.by_xpath(self.__first_project_result)
        return element

    def get_first_flow_result(self) -> WebElement:
        """Finds and returns the first flow result element on the page."""
        element = self.find_element.by_xpath(self.__first_flow_result)
        return element

    def get_new_flow_button(self) -> WebElement:
        """Finds and returns the new flow button element on the page."""
        element = self.find_element.by_xpath(self.__new_flow_button)
        return element
