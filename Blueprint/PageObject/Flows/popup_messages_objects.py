from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import popup_messages_locators as locators


class PopupMessagesObjects(BasePage):
    """This class represents the Elements of popup messages in flow page"""

    def __init__(self):
        super().__init__()
        self.__popup_messages = locators.POPUP_MESSAGES_LOCATOR
        self.__close_popup_messages = locators.CLOSE_POPUP_MESSAGES_LOCATOR

    def get_popup_messages(self):
        """Returns the popup message element"""
        element = self.find_element.by_xpath(self.__popup_messages)
        return element
    
    def get_close_popup_message(self):
        """Returns the close popup message element"""
        element = self.find_element.by_xpath(self.__close_popup_messages)
        return element
    