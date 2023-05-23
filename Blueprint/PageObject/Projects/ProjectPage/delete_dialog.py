from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Projects.ProjectPage import delete_dialog_locators as locators
from Libraries.Drivers.base_page import BasePage


class DeleteDialogObjects(BasePage):
    """This class represents the Delete Dialog of a Blueprint application"""

    def __init__(self, driver):
        super().__init__(driver)

    def get_delete_dialog(self) -> WebElement:
        """Finds and returns the delete dialog element of the page."""
        element = self.find_element.by_xpath(locators.DELETE_DIALOG)
        return element

    def get_delete_dialog_close_button(self) -> WebElement:
        """Finds and returns the close button element of the delete dialog."""
        element = self.find_element.by_xpath(locators.DELETE_DIALOG_CLOSE_BUTTON)
        return element

    def get_delete_dialog_title(self) -> WebElement:
        """Finds and returns the title element of the delete dialog."""
        element = self.find_element.by_xpath(locators.DELETE_DIALOG_TITLE)
        return element

    def get_delete_dialog_paragraph(self) -> WebElement:
        """Finds and returns the paragraph element of the delete dialog."""
        element = self.find_element.by_xpath(locators.DELETE_DIALOG_PARAGRAPH)
        return element

    def get_delete_dialog_cancel_button(self) -> WebElement:
        """Finds and returns the cancel button element of the delete dialog."""
        element = self.find_element.by_xpath(locators.DELETE_DIALOG_CANCEL_BUTTON)
        return element

    def get_delete_dialog_delete_button(self) -> WebElement:
        """Finds and returns the delete button element of the delete dialog."""
        element = self.find_element.by_xpath(locators.DELETE_DIALOG_DELETE_BUTTON)
        return element
