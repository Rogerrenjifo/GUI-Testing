from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Flows import permissions_locators as locators
from Libraries.Drivers.base_page import BasePage


class ProcessPermissions(BasePage):
    """This class represents the process permission of a Blueprint application"""

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
