from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Flows import create_flow_components_locators as locators
from Libraries.Drivers.base_page import BasePage
# from Libraries.DataProcessors.find_elements import *

class Components(BasePage):
    """This class represents components menu of create form"""

    def __init__(self):
        self.__components_title = locators.COMPONENTS_TITLE
        self.__step_locator = locators.STEP_LOCATOR
        self.__action_locator = locators.ACTION_LOCATOR

    def get_components_title(self) -> WebElement:
        """Finds and returns the title element of the components menu"""
        element = self.find_element.by_xpath(self.driver, self.__components_title)
        return element
    
    def get_step_element(self) -> WebElement:
        """Finds and returns step element"""
        element = self.find_element.by_id(self.__step_locator)
        return element

    def get_action_element(self) -> WebElement:
        """Finds and returns action element"""
        element = self.find_element.by_id(self.__action_locator)
        return element
