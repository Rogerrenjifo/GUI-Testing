from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Flows import overwrite_draft_locators as locators
from Libraries.Drivers.base_page import BasePage


class OverwriteDraftDialogObjects(BasePage):
    """This class represents the Overwrite draft dialog in flows page."""
    
    def get_overwrite_dialog_cancel_button(self) -> WebElement:
        """Finds and returns the Cancel button element of the Overwrite draft dialog."""
        element = self.find_element.by_xpath(locators.CANCEL_OVERWRITE_DIALOG_BUTTON)
        return element
    
    def get_overwrite_dialog_confirm_button(self) -> WebElement:
        """Finds and returns the Confirm button element of the Overwrite draft dialog."""
        element = self.find_element.by_xpath(locators.CONFIRM_OVERWRITE_DIALOG_BUTTON)
        return element
    
    def get_overwrite_dialog_close_button(self) -> WebElement:
        """Finds and returns the close button element of the Overwrite draft dialog."""
        element = self.find_element.by_class(locators.CLOSE_OVERWRITE_DIALOG_BUTTON)
        return element
    
    def get_overwrite_dialog_title(self) -> WebElement:
        """Finds and returns the title element of the Overwrite draft dialog."""
        element = self.find_element.by_xpath(locators.OVERWRITE_DIALOG_TITLE)
        return element
    
    def get_overwrite_dialog_question(self) -> WebElement:
        """Finds and returns the question text element of the Overwrite draft dialog."""
        element = self.find_element.by_xpath(locators.OVERWRITE_DIALOG_QUESTION)
        return element
