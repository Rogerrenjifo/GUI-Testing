from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flows_properties_locators as locators


class NameField(BasePage):
    """Name field object"""

    def __init__(self):
        super().__init__()
        self.__label: WebElement 
        self.__text_field: WebElement

    @property
    def label(self):
        """Label text for name object."""
        self.__label = self.find_element.by_xpath(locators.NAME_LBL)
        return self.__label

    @property
    def text_field(self):
        """Text field locator."""
        self.__text_field = self.find_element.by_xpath(locators.NAME_TXT)
        return self.__text_field
