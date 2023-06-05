from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Projects.ProjectTracing import system_locators as locators
from Libraries.Drivers.base_page import BasePage
from robot.api import logger


class ProjectSystemObject(BasePage):
    """This class represents the system section of the Project Tracing"""

    def get_system_title(self) -> WebElement:
        """Finds and returns the title element of the system section"""
        element = self.find_element.by_xpath(locators.SYSTEM_TITLE)
        return element
    
    def get_current_step_title(self) -> WebElement:
        """Finds and returns the label element of the current step"""
        element = self.find_element.by_xpath(locators.LABEL_CURRENT_STEP)
        return element
    
    def get_label_action_owner(self) -> WebElement:
        """Finds and returns the label element of the action owner"""
        element = self.find_element.by_xpath(locators.LABEL_ACTION_OWNER)
        return element
    
    def get_creation_date_title(self) -> WebElement:
        """Finds and returns the label element of the creation date"""
        element = self.find_element.by_xpath(locators.LABEL_CREATION_DATE)
        return element
    
    def get_last_update_title(self) -> WebElement:
        """Finds and returns the label element of the last update"""
        element = self.find_element.by_xpath(locators.LABEL_LAST_UPDATE)
        return element
    
    def get_closure_date_title(self) -> WebElement:
        """Finds and returns the label element of the closure date"""
        element = self.find_element.by_xpath(locators.LABEL_CLOSURE_DATE)
        return element
    
    def get_current_step_element(self) -> WebElement:
        """Finds and returns the current step value element"""
        element = self.find_element.by_xpath(locators.CURRENT_STEP_VALUE)
        return element
    
    def get_action_owner_element(self) -> WebElement:
        """Finds and returns the action owner value element"""
        xpaths = [
            locators.ACTION_OWNER_VALUE,
            locators.NONE_ACTION_OWNER,
            locators.FIELD_REQUIRED_OWNER
        ]
        for xpath in xpaths:
            try:
                element = self.find_element.by_xpath(xpath)
                return element
            except Exception:
                logger.info("Action owner element not found")
    
    def get_creation_date_element(self) -> WebElement:
        """Finds and returns the creation date value element"""
        element = self.find_element.by_xpath(locators.CREATION_DATE_VALUE)
        return element
    
    def get_last_update_element(self) -> WebElement:
        """Finds and returns the last update value element"""
        element = self.find_element.by_xpath(locators.LAST_UPDATE_VALUE)
        return element
    
    def get_closure_date_element(self) -> WebElement:
        """Finds and returns the closure date value element"""
        element = self.find_element.by_xpath(locators.CLOSURE_DATE_VALUE)
        return element
    
    def get_edit_current_step_button_element(self) -> WebElement:
        """Finds and returns the edit element of the current step"""
        element = self.find_element.by_xpath(locators.EDIT_CURRENT_STEP)
        return element
    
    def get_edit_action_owner_button_element(self) -> WebElement:
        """Finds and returns the edit element of the action owner"""
        element = self.find_element.by_xpath(locators.EDIT_ACTION_OWNER)
        return element
    
    def get_save_button_element(self) -> WebElement:
        """Finds and returns the save button element"""
        try:
            element = self.find_element.by_xpath(locators.SAVE_LOCATOR)
            return element
        except Exception:
            logger.info("Element not found")
            return False

    def get_cancel_button_element(self) -> WebElement:
        """Finds and returns the cancel button element"""
        try:
            element = self.find_element.by_xpath(locators.CANCEL_LOCATOR)
            return element
        except Exception:
            logger.info("Element not found")
            return False

    def get_clear_button_element(self) -> WebElement:
        """Finds and returns the clear button element"""
        try:
            element = self.find_element.by_xpath(locators.CLEAR_LOCATOR)
            return element
        except Exception:
            logger.info("Element not found")
            return False
    
    def get_field_required_element(self) -> WebElement:
        """Finds and returns the message element"""
        element = self.find_element.by_xpath(locators.FIELD_REQUIRED)
        return element

    def get_css_selector_from_current_step(self) -> str:
        """Returns the css selector from current step input field"""
        element = self.find_element.by_xpath(locators.CURRENT_STEP_DROPDOWN)
        self.action_chains.move_to_an_element(element)
        rgb_color = element.value_of_css_property('border-color')
        return rgb_color

    def get_css_selector_from_action_owner(self) -> str:
        """Returns the css selector from action owner input field"""
        element = self.find_element.by_xpath(locators.ACTION_OWNER_DROPDOWN)
        self.action_chains.move_to_an_element(element)
        rgb_color = element.value_of_css_property('border-color')
        return rgb_color
