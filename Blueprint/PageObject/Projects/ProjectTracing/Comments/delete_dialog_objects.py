from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Projects.ProjectTracing.Comments import dialog_delete_comment_locators \
    as locators
from Libraries.Drivers.base_page import BasePage


class DeleteCommentDialog(BasePage):
    """This class represents the "Delete comment" dialog displayed in project tracing page"""

    def get_delete_button(self) -> WebElement:
        """Finds and returns the delete button in the dialog"""
        element = self.find_element.by_xpath(locators.DIALOG_DELETE_BUTTON)
        return element

    def get_cancel_button(self) -> WebElement:
        """Finds and returns the cancel button in the dialog"""
        element = self.find_element.by_xpath(locators.DIALOG_CANCEL_BUTTON)
        return element

    def get_x_button(self) -> WebElement:
        """Finds and returns the x button in the dialog"""
        element = self.find_element.by_class(locators.DIALOG_X_BUTTON)
        return element

    def get_title(self) -> WebElement:
        """Finds and returns dialog title"""
        element = self.find_element.by_class(locators.COMMENT_DIALOG_TITLE)
        return element

    def get_description(self) -> WebElement:
        """Finds and returns the dialog description"""
        element = self.find_element.by_class(locators.COMMENT_DIALOG_TEXT)
        return element
