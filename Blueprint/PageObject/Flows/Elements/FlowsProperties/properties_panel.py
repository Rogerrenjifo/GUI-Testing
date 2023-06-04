from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flows_properties_locators as locators


class PropertiesPanel(BasePage):
    """Properties panel object"""

    def __init__(self):
        super().__init__()
        self.__properties_panel_title: WebElement
        self.__properties_panel_top_section: WebElement
        self.__properties_panel_bottom_section: WebElement

    @property
    def properties_panel_title(self):
        """Title text for properties panel."""
        self.__properties_panel_title = self.find_element.by_xpath(locators.HEADER_TITLE)
        return self.__properties_panel_title

    @property
    def properties_panel_top_section(self):
        """Top section container of the properties panel."""
        self.__properties_panel_top_section = self.find_element.by_xpath(locators.BODY_UPPPER)
        return self.__properties_panel_top_section

    @property
    def properties_panel_bottom_section(self):
        """Bottom section container of the properties panel."""
        self.__properties_panel_bottom_section = self.find_element.by_xpath(locators.BODY_LOWER)
        return self.__properties_panel_bottom_section
