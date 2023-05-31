from Blueprint.Locators.Projects.ProjectPage import project_table_locators as locators
from Libraries.Drivers.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class ProjectTableObjects(BasePage):
    """This class represents the Project Page of a Blueprint application"""

    def __init__(self):
        super().__init__()
        self.__projects_ids = locators.PROJECTS_IDS

    @staticmethod
    def generate_locator_by_index(locator_template: str, index: str) -> str:
        """Generates the locators according to the index of the element"""
        locator = f"({locator_template})[{index}]"
        return locator

    @staticmethod
    def generate_locator_by_project_id(locator_template: str, project_id: str) -> str:
        """Generates the locators according to the project id"""
        locator = locator_template.replace("<<value>>", project_id)
        return locator

    def get_table_row_by_project_id(self, project_id: str) -> WebElement:
        """Finds and returns the table row element of the page according to the project id."""
        locator = self.generate_locator_by_project_id(locators.PROJECT_ROW, project_id)
        element = self.find_element.by_xpath(locator)
        return element

    def get_project_checkbox_by_project_id(self, project_id: str) -> WebElement:
        """Finds and returns the checkbox element of the page according to the project id."""
        locator = self.generate_locator_by_project_id(locators.PROJECT_CHECKBOX, project_id)
        element = self.find_element.by_xpath(locator)
        return element

    def get_project_checkbox_label_by_project_id(self, project_id: str) -> WebElement:
        """Finds and returns the checkbox element of the page according to the project id."""
        locator = self.generate_locator_by_project_id(locators.PROJECT_CHECKBOX_LABEL, project_id)
        element = self.find_element.by_xpath(locator)
        return element

    def get_all_project_ids(self) -> List[WebElement]:
        """Finds and returns all the project ids elements of the page."""
        element_list = self.find_elements.by_xpath(self.__projects_ids)
        return element_list

    def get_project_id_by_index(self, index: str) -> WebElement:
        """Finds and returns the project id element of the page according to the element index."""
        locator = self.generate_locator_by_index(self.__projects_ids, index)
        element = self.find_element.by_xpath(locator)
        return element

    def get_project_title_by_project_id(self, project_id: str) -> WebElement:
        """Finds and returns the project title element of the page according to the project id."""
        locator = self.generate_locator_by_project_id(locators.PROJECT_TITLE, project_id)
        element = self.find_element.by_xpath(locator)
        return element

    def get_project_current_step_by_project_id(self, project_id: str) -> WebElement:
        """Finds and returns the current step element of the page according to the project id."""
        locator = self.generate_locator_by_project_id(locators.PROJECT_CURRENT_STEP, project_id)
        element = self.find_element.by_xpath(locator)
        return element

    def get_project_owner_by_project_id(self, project_id: str) -> WebElement:
        """Finds and returns the project owner element of the page according to the project id."""
        locator = self.generate_locator_by_project_id(locators.PROJECT_OWNER, project_id)
        element = self.find_elements.by_xpath(locator)[0]
        return element

    def get_project_creator_by_project_id(self, project_id: str) -> WebElement:
        """Finds and returns the project creator element of the page according to the project id."""
        locator = self.generate_locator_by_project_id(locators.PROJECT_CREATOR, project_id)
        element = self.find_elements.by_xpath(locator)[1]
        return element

    def get_project_date_created_by_project_id(self, project_id: str) -> WebElement:
        """Finds and returns the date created element of the page according to the project id."""
        locator = self.generate_locator_by_project_id(locators.PROJECT_DATE_CREATED, project_id)
        element = self.find_elements.by_xpath(locator)[0]
        return element

    def get_project_closure_date_by_project_id(self, project_id: str) -> WebElement:
        """Finds and returns the closure date element of the page according to the project id."""
        locator = self.generate_locator_by_project_id(locators.PROJECT_CLOSURE_DATE, project_id)
        element = self.find_elements.by_xpath(locator)[1]
        return element

    def get_project_action_by_project_id(self, project_id: str) -> WebElement:
        """Finds and returns the action button element of the page according to the project id."""
        locator = self.generate_locator_by_project_id(locators.PROJECT_ACTION, project_id)
        element = self.find_element.by_xpath(locator)
        return element

    def get_project_action_delete_by_project_id(self, project_id: str) -> WebElement:
        """Finds and returns the delete option element of the page according to the project id."""
        locator = self.generate_locator_by_project_id(locators.PROJECT_ACTION_DELETE, project_id)
        element = self.find_element.by_xpath(locator)
        return element
