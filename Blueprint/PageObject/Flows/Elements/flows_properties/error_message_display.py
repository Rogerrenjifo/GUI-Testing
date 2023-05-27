from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flows_properties_locators as locators


class ErrorMessage(BasePage):
    """Error message object for update fields."""

    def __init__(self):
        super().__init__()
        self.__message: WebElement 

    @property
    def message(self):
        """Error message locator."""
        self.__message = self.find_element.by_xpath(locators.MSG_REQUIRED_ERROR)
        return self.__message
