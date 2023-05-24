from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Flows import permissions_locators as locators
from Blueprint.PageObject.Flows.Elements.dropdowns import Dropdownbox
from Libraries.Drivers.base_page import BasePage


class ProcessPermissions(BasePage):
    """This class represents the process permission of a Blueprint application"""

    def __init__(self):
        """Builds the class constructor"""
        super().__init__()
        self.dropdown_process_admin = Dropdownbox(self.driver, 2)

    def get_title_process_permissions(self) -> WebElement:
        """Finds and returns the process permissions title object"""
        element = self.find_element.by_xpath(locators.TITLE_PROCESS_PERMISSIONS)
        return element

    def get_title_current_versions(self) -> WebElement:
        """Finds and returns the current versions title object"""
        element = self.find_element.by_xpath(locators.TITLE_CURRENT_VERSION)
        return element

    def get_title_section_visibility(self) -> WebElement:
        """Finds and returns the section visibility subtitle object"""
        element = self.find_element.by_xpath(locators.TITLE_SECTION_VISIBILITY)
        return element
