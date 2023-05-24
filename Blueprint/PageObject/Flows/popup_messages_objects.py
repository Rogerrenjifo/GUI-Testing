from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import popup_messages_locators as locators


class PopupMessagesObjects(BasePage):
    """This class represents the elements of popup messages in flow page."""

    def get_popup_messages(self) -> WebElement:
        """Returns the popup message element."""
        element = self.find_element.by_xpath(locators.POPUP_MESSAGES_LOCATOR)
        return element
    
    def get_close_popup_message(self) -> WebElement:
        """Returns the close popup message element."""
        element = self.find_element.by_xpath(locators.CLOSE_POPUP_MESSAGES_LOCATOR)
        return element
