from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Flows import flow_components_locators as locators
from Libraries.Drivers.base_page import BasePage


class FlowComponentObjects(BasePage):
    """This class represents components menu of create flow"""

    def __init__(self) -> None:
        super().__init__()
        self.__components_title = locators.COMPONENTS_TITLE
        self.__step_locator = locators.STEP_LOCATOR
        self.__action_locator = locators.ACTION_LOCATOR
        self.__canvas = locators.CANVAS_LOCATOR

    def get_components_title(self) -> WebElement:
        """Finds and returns the title element of the components menu"""
        element = self.find_element.by_xpath(self.__components_title)
        return element

    def get_step_element(self) -> WebElement:
        """Finds and returns step element"""
        element = self.find_element.by_xpath(self.__step_locator)
        return element

    def get_action_element(self) -> WebElement:
        """Finds and returns action element"""
        element = self.find_element.by_xpath(self.__action_locator)
        return element

    def get_canvas_element(self) -> WebElement:
        """Finds and returns canvas element"""
        element = self.find_element.by_xpath(self.__canvas)
        return element

    def get_main_container_element(self) -> WebElement:
        """Finds and return the element of all the flow windows"""
        element = self.find_element.by_xpath(locators.MAIN_CONTAINER_LOCATOR)
        return element

    def get_main_menu_element(self) -> WebElement:
        """Finds and return the element of all the flow windows"""
        element = self.find_element.by_xpath(locators.MAIN_MENU_LOCATOR)
        return element

    def get_panel_right_element(self) -> WebElement:
        """Finds and returns the right panel element"""
        element = self.find_element.by_xpath(locators.PANEL_RIGHT_LOCATOR)
        return element

    def get_header_element(self) -> WebElement:
        """Finds and returns the header element"""
        element = self.find_element.by_xpath(locators.HEADER_LOCATOR)
        return element

    def get_properties_element(self) -> WebElement:
        """Finds and returns the properties element"""
        element = self.find_element.by_xpath(locators.PROPERTIES_LOCATOR)
        return element

    def get_properties_panel_title_element(self) -> WebElement:
        """Finds and returns the properties title element"""
        element = self.find_element.by_xpath(locators.PROPERTIES_TITLE_LOCATOR)
        return element
