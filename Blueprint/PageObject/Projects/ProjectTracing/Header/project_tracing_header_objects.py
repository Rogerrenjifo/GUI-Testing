from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Projects.ProjectTracing.Header import project_tracing_header_locators as locators
from Libraries.Drivers.base_page import BasePage


class ProjectTracingHeader(BasePage):
    """This class represents the header of the Project Tracing page."""    

    def get_project_tag(self) -> WebElement:
        """Finds and returns the project tag element of the project tracing header."""
        element = self.find_element.by_xpath(locators.PROJECT_TAG)
        return element
    
    def get_project_title(self) -> WebElement:
        """Finds and returns the project title element of the project tracing header."""
        element = self.find_element.by_xpath(locators.PROJECT_TITLE)
        return element
    
    def get_delete_button(self) -> WebElement:
        """Finds and returns the delete button element of the project tracing header."""
        element = self.find_element.by_xpath(locators.DELETE_BUTTON)
        return element    
    
    def get_action_button(self, button_text: str) -> WebElement:
        """Finds and returns the action button element of the project tracing header."""
        element = self.find_element.by_xpath(locators.ACTION_BUTTON.replace('<<value>>', button_text))
        return element
    
    def get_no_actions_label(self) -> WebElement:
        """Finds and returns the 'No more available actions' text element of the project tracing header."""
        element = self.find_element.by_class(locators.NO_ACTIONS_TEXT)
        return element
