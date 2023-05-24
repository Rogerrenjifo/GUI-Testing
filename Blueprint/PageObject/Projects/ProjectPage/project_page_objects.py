from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Projects.ProjectPage import project_page_locators as locators
from Blueprint.PageObject.Projects.ProjectPage.projects_table_objects import ProjectTableObjects
from Blueprint.PageObject.Projects.ProjectPage.delete_dialog import DeleteDialogObjects
from Libraries.Drivers.base_page import BasePage
from typing import List


class ProjectPageObjects(BasePage):
    """This class represents the Project Page of a Blueprint application"""

    def __init__(self):
        super().__init__()
        self.projects_table = ProjectTableObjects()
        self.delete_dialog = DeleteDialogObjects()
        self.__select_row_pagination = locators.SELECT_ROW_PAGINATION

    @staticmethod
    def generate_locator_by_project_id(locator_template: str, project_id) -> str:
        """Generates the locators according to the project id"""
        locator = locator_template.replace("<<value>>", project_id)
        return locator

    def get_project_name(self) -> WebElement:
        """Finds and returns the project name element of the page."""
        element = self.find_element.by_xpath(locators.PROJECT_NAME)
        return element

    def get_project_new_request_button(self) -> WebElement:
        """Finds and returns the new request button element of the page."""
        element = self.find_element.by_xpath(locators.PROJECT_NEW_REQUEST_BUTTON)
        return element

    def get_table_row(self, project_id: str) -> dict:
        """Finds and returns the table row element of the page according to the project id."""
        project = {
            "project_row": self.projects_table.get_table_row_by_project_id(project_id),
            "project_checkbox": self.projects_table.get_project_checkbox_by_project_id(project_id),
            "project_title": self.projects_table.get_project_title_by_project_id(project_id),
            "project_current_step": self.projects_table
            .get_project_current_step_by_project_id(project_id),
            "project_owner": self.projects_table.get_project_owner_by_project_id(project_id),
            "project_creator": self.projects_table.get_project_creator_by_project_id(project_id),
            "project_date_created": self.projects_table
            .get_project_date_created_by_project_id(project_id),
            "project_closure_date": self.projects_table
            .get_project_closure_date_by_project_id(project_id),
            "project_actions_button": self.projects_table.get_project_action_by_project_id(project_id),
            "project_actions_delete": self.projects_table
            .get_project_action_delete_by_project_id(project_id)
        }
        return project

    def get_all_table_rows_page(self) -> List[dict]:
        """Finds and returns all the table rows element of the page."""
        project_ids = self.projects_table.get_all_project_ids()
        all_projects_page = []
        for project_id in project_ids:
            project_row = self.get_table_row(project_id.text)
            project_row["id"] = project_id
            all_projects_page.append(project_row)
        return all_projects_page

    def get_select_row_pagination(self) -> WebElement:
        """Finds and returns the select pagination element of the page."""
        element = self.find_element.by_xpath(self.__select_row_pagination)
        return element

    def get_select_row_pagination_option(self, option: str) -> WebElement:
        """Finds and returns the option of the select pagination element of the page."""
        locator = self.generate_locator_by_project_id(self.__select_row_pagination, option)
        element = self.find_element.by_xpath(locator)
        return element

    def get_previous_page_button(self) -> WebElement:
        """Finds and returns the previous page button element of the page."""
        element = self.find_element.by_xpath(locators.PREVIOUS_PAGE_BUTTON)
        return element

    def get_next_page_button(self) -> WebElement:
        """Finds and returns the next page button element of the page."""
        element = self.find_element.by_xpath(locators.NEXT_PAGE_BUTTON)
        return element

    def get_page_number_button(self, page_number) -> WebElement:
        """Finds and returns the number page button element of the page."""
        locator = self.generate_locator_by_project_id(locators.NUMBER_PAGE_BUTTON, page_number)
        element = self.find_element.by_xpath(locator)
        return element
