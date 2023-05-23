from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Projects.ProjectsTracing import system_locators as locators
from Libraries.Drivers.base_page import BasePage
from robot.api import logger


class ProjectSystemObject(BasePage):
    """This class represents the system section of the Project Tracing"""

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def get_system_title(self) -> WebElement:
        """Finds and returns the title element of the system section"""
        element = self.find_element.by_xpath(locators.SYSTEM_TITLE)
        return element
    
    def get_label_current_step(self) -> WebElement:
        """Finds and returns the label element of the current step"""
        element = self.find_element.by_xpath(locators.LABEL_CURRENT_STEP)
        return element
    
    def get_label_action_owner(self) -> WebElement:
        """Finds and returns the label element of the action owner"""
        element = self.find_element.by_xpath(locators.LABEL_ACTION_OWNER)
        return element
    
    def get_label_creation_date(self) -> WebElement:
        """Finds and returns the label element of the creation date"""
        element = self.find_element.by_xpath(locators.LABEL_CREATION_DATE)
        return element
    
    def get_label_last_update(self) -> WebElement:
        """Finds and returns the label element of the last update"""
        element = self.find_element.by_xpath(locators.LABEL_LAST_UPDATE)
        return element
    
    def get_label_closure_date(self) -> WebElement:
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
    
    def get_arrow_element(self) -> WebElement:
        """Finds and returns the arrow element"""
        element = self.find_element.by_xpath(locators.ARROW_LOCATOR)
        return element
    
    def get_option_selected_element(self, option: str) -> WebElement:
        """Finds and returns the option element of the dropdown"""
        try:
            xpath = locators.OPTION.replace("<<option>>", option)
            element = self.find_element.by_xpath(xpath)
            return element
        except Exception:
            logger.info(f"'{option}' is not an available option")
    
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
        element = self.find_element.by_xpath(locators.SAVE_LOCATOR)
        return element
    
    def get_cancel_button_element(self) -> WebElement:
        """Finds and returns the cancel button element"""
        element = self.find_element.by_xpath(locators.CANCEL_LOCATOR)
        return element
    
    def get_clear_all_button_element(self) -> WebElement:
        """Finds and returns the clear all button element"""
        element = self.find_element.by_xpath(locators.CLEAR_LOCATOR)
        return element
    
    def get_field_required_element(self) -> WebElement:
        """Finds and returns the message element"""
        element = self.find_element.by_xpath(locators.FIELD_REQUIRED)
        return element
    
    def get_dropdown_elements(self) -> WebElement:
        """Finds and returns the dropdown element"""
        elements = self.find_elements.by_xpath(locators.DROPDOWN_LOCATOR)
        return elements
    
    def get_available_options(self) ->list:
        """Return a list of available options of the dropdown"""
        options = self.get_dropdown_elements()
        available_options = [option.text for option in options]
        option_list = available_options[0].split("\n")
        return option_list
