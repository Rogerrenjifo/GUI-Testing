from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Flows import permissions_locators as locators
from Blueprint.PageObject.Flows.Elements.dropdowns import Dropdownbox
from Libraries.Drivers.base_page import BasePage


class FlowPermissions(BasePage):
    """This class represents the flow permission of a Blueprint application"""
    def __init__(self, driver):
        """Builds the class constructor"""
        super().__init__(driver)
        self.dropdown_flow_admin = Dropdownbox(self.driver, 1)

    def get_title_flow_permissions(self) -> WebElement:
        """Finds and returns the flow permissions title object"""
        element = self.find_element.by_xpath(locators.TITLE_FLOW_PERMISSIONS)
        return element

    def get_title_all_versions(self) -> WebElement:
        """Finds and returns the all versions title object"""
        element = self.find_element.by_xpath(locators.TITLE_ALL_VERSIONS)
        return element
