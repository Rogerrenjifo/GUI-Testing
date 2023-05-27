from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flows_properties_locators as locators


class UpdateFieldsCheck(BasePage):
    """Checkbox object for update files."""

    def __init__(self):
        super().__init__()
        self.__label: WebElement 
        self.__checkbox: WebElement

    @property
    def label(self):
        """Label for update fields checkbox"""
        self.__label = self.find_element.by_xpath(locators.UPDATE_FIELDS_LBL)
        return self.__label

    @property
    def checkbox(self):
        """Checkbox ticker."""
        self.__checkbox = self.find_element.by_xpath(locators.UPDATE_FIELDS_CHK)
        return self.__checkbox
