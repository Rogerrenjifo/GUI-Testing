from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flows_properties_locators as locators


class AddCommentCheck(BasePage):
    """Checkbox object for 'action' component."""

    def __init__(self):
        super().__init__()
        self.__label: WebElement 
        self.__checkbox: WebElement

    @property
    def label(self):
        """Add comment checkbox label text."""
        self.__label = self.find_element.by_xpath(locators.ADD_COMMENT_LBL)
        return self.__label

    @property
    def checkbox(self):
        """Add comment checkbox ticker"""
        self.__checkbox = self.find_element.by_xpath(locators.ADD_COMMENT_CHK)
        return self.__checkbox
