from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flows_properties_locators as locators


class UpdateFieldsCommons(BasePage):
    """'Required to Update Fields' common elements"""

    def __init__(self):
        super().__init__()
        self.__label: WebElement 
        self.__button: WebElement
        self.__button_text: WebElement
        self.__form_button_trash: WebElement

    @property
    def label(self):
        """Returns properties subtitle label for fields options."""
        self.__label = self.find_element.by_xpath(locators.REQ_FIELDS_LBL)
        return self.__label

    @property
    def button(self):
        """Required update fields button."""
        self.__button = self.find_element.by_xpath(locators.REQ_FIELDS_BTN)
        return self.__button
    
    @property
    def button_text(self):
        """Returns button's text."""
        self.__button_text = self.find_element.by_xpath(locators.REQ_FIELDS_BTN + "/text()")
        return self.__button_text

    @property
    def form_button_trash(self):
        """Returns trash button element."""
        self.__form_button_trash = self.find_element.by_xpath(locators.REQ_FIELDS_TRASH)
        return self.__form_button_trash
