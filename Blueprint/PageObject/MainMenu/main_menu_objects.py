from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.MainMenu import main_menu_locators as locators
from Libraries.Drivers.base_page import BasePage


class MainMenuObjects(BasePage):
    """This class represents the Main Menu of the Blueprint application"""

    def __init__(self, driver):
        super().__init__(driver)
        self.__my_inbox_button = locators.MY_INBOX_BUTTON
        self.__projects_button = locators.PROJECTS_BUTTON
        self.__reports_button = locators.REPORTS_BUTTON
        self.__flows_button = locators.FLOWS_BUTTON
        self.__users_and_groups_button = locators.USERS_AND_GROUPS_BUTTON
        self.__projects_results = locators.PROJECT_RESULTS

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

    def get_projects_results(self):
        elements = self.find_elements.by_xpath(self.__projects_results)
        titles = []
        for element in elements:
            project_title = element.get_attribute("title")
            titles.append(project_title)
        print(titles)
