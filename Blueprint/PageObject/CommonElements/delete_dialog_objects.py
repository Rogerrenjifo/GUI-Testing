from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.CommonElements import delete_dialog_locators as locators
from Libraries.Drivers.base_page import BasePage
from robot.api import logger


class DeleteDialogObjects(BasePage):
    """This class represents the delete dialog in Blueprint."""
    
    def get_cancel_dialog_button(self) -> WebElement:
        """Finds and returns the Cancel button element of the Delete Process dialog."""
        element = self.find_element.by_xpath(locators.CANCEL_DIALOG_BUTTON)
        return element
    
    def get_delete_dialog_button(self) -> WebElement:
        """Finds and returns the Delete button element of the Delete Process dialog."""
        element = self.find_element.by_xpath(locators.DELETE_DIALOG_BUTTON)
        return element
    
    def get_close_dialog_button(self) -> WebElement:
        """Finds and returns the close button element of the Delete Process dialog."""
        element = self.find_element.by_class(locators.CLOSE_DIALOG_BUTTON)
        return element
    
    def get_dialog_title(self) -> WebElement:
        """Finds and returns the title element of the delete dialog."""
        element = self.find_element.by_xpath(locators.DIALOG_TITLE)
        return element
    
    def get_dialog_question(self) -> WebElement:
        """Finds and returns the question text element of the delete dialog."""
        element = self.find_element.by_xpath(locators.DIALOG_QUESTION)
        return element

    def get_father_dialog_container(self) -> WebElement:
        """Finds and returns the father container element of the delete dialog."""
        element = self.find_element.by_xpath(locators.FATHER_DIALOG_CONTAINER)
        return element
    
    def get_delete_dialog(self) -> WebElement:
        """Finds and returns the delete dialog element."""
        try:
            self.driver.implicitly_wait(2)
            element = self.find_element.by_class(locators.DELETE_DIALOG)            
            return element
        except:
            logger.info("It returns False if the element is not found.")
            return False
