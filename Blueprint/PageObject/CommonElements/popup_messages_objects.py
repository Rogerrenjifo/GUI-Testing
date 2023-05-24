from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.CommonElements import popup_messages_locators as locators
from selenium.webdriver.remote.webelement import WebElement


class PopupMessagesObjects(BasePage):
    """This class represents the elements of popup messages in flow page"""

    def get_popup_message(self, index: str = "1") -> WebElement:
        """Returns the popup message element"""
        xpath = f"({locators.POPUP_MESSAGES_LOCATOR})[{str(index)}]"
        element = self.find_element.by_xpath(xpath)
        return element
    
    def get_close_popup_message(self, index: str = "1") -> WebElement:
        """Returns the close popup message element"""
        xpath = f"({locators.CLOSE_POPUP_MESSAGES_LOCATOR})[{str(index)}]"
        element = self.find_element.by_xpath(xpath)
        return element

    def get_popup_messages_list(self) -> list:
        """Returns a list with all the popup messages displayed"""
        element = self.find_elements.by_xpath(locators.CLOSE_POPUP_MESSAGES_LOCATOR)
        return element
