from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Flows import header_locators as locators
from Libraries.Drivers.base_page import BasePage
import os

class Header(BasePage):
    """This class represents the header of the Flow feature"""

    def __init__(self, driver):
        super().__init__(driver)
        self.__status_locator = locators.STATUS
        self.__version_locator = locators.VERSION
        self.__flow_name_locator = locators.FLOW_NAME
        self.__flow_dropdown = locators.FLOW_DROPDOWN
        self.__delete_locator = locators.DELETE
        self.__select_version_locator = locators.SELECT_VERSION
        self.__versions_locator = locators.VERSIONS
        self.__update_text_locator = locators.UPDATE_TEXT
        self.__save_button_locator = locators.SAVE_BUTTON
        self.__save_next_button_locator = locators.SAVE_NEXT_BUTTON
        self.__bar_tab_marked_locator = locators.BAR_TAB_MARKED
        self.__icon_tab_marked_locator = locators.ICON_TAB_MARKED
        self.__icon_error_marked_locator = locators.ICON_ERROR_MARKED
        self.__bar_tab_unmarked_locator = locators.BAR_TAB_UNMARKED
        self.__icon_tab_unmarked_locator = locators.ICON_TAB_UNMARKED
        self.__icon_error_unmarked_locator = locators.ICON_ERROR_UNMARKED 
    
    def get_status(self) -> WebElement:
        """Finds and returns the status element of the page."""
        element = self.find_element.by_class(self.__status_locator)
        return element
    
    def get_version(self) -> WebElement:
        """Finds and returns the version element of the page."""
        element = self.find_element.by_class(self.__version_locator)
        return element
    
    def get_flow_name(self) -> WebElement:
        """Finds and returns the flow name element of the page."""
        element = self.find_element.by_class(self.__flow_name_locator)
        return element
    
    def get_dropdown_button(self) -> WebElement:
        """Finds and returns the dropdown element of the page."""
        element = self.find_element.by_class(self.__flow_dropdown)
        return element
    
    def get_delete_option(self) -> WebElement:
        """Finds and returns the delete option element of the page."""
        element = self.find_element.by_class(self.__delete_locator)
        return element
    
    def get_select_version_option(self) -> WebElement:
        """Finds and returns the select version element of the page."""
        element = self.find_element.by_class(self.__select_version_locator)
        return element
    
    def get_specific_version(self, version: str) -> WebElement:
        """Finds and returns a version from the select version list."""
        element = self.find_element.by_xpath(self.__versions_locator.replace('v1', version))
        return element
    
    def get_update_text(self) -> WebElement:
        """Finds and returns the updated text element of the page."""
        element = self.find_element.by_class(self.__update_text_locator)
        return element
    
    def get_save_button(self) -> WebElement:
        """Finds and returns the save button element of the page."""
        element = self.find_element.by_class(self.__save_button_locator)
        return element
    
    def get_save_next_button(self) -> WebElement:
        """Finds and returns the save and next button element of the page."""
        element = self.find_element.by_class(self.__save_next_button_locator)
        return element  
    
    def get_create_form_marked(self) -> WebElement:
        """Finds and returns the marked bar and icon element from the Create Form tab."""
        bar_element = self.find_element.by_xpath(self.__bar_tab_marked_locator.replace('TAB_NAME','Create Form'))
        icon_element = self.find_element.by_xpath(self.__icon_tab_marked_locator.replace('TAB_NAME','Create Form'))
        return (bar_element & icon_element)
    
    def get_create_form_error_icon_marked(self) -> WebElement:
        """Finds and returns the marked error icon element from the Create Form tab."""
        element = self.find_element.by_xpath(self.__icon_error_marked_locator.replace('TAB_NAME','Create Form'))
        return element
    
    def get_create_form_unmarked(self) -> WebElement:
        """Finds and returns the unmarked bar and icon element from the Create Form tab."""
        bar_element = self.find_element.by_xpath(self.__bar_tab_unmarked_locator.replace('TAB_NAME','Create Form'))
        icon_element = self.find_element.by_xpath(self.__icon_tab_unmarked_locator.replace('TAB_NAME','Create Form'))
        return (bar_element & icon_element)
    
    def get_create_form_error_icon_unmarked(self) -> WebElement:
        """Finds and returns the unmarked error icon element from the Create Form tab."""
        element = self.find_element.by_xpath(self.__icon_error_unmarked_locator.replace('TAB_NAME','Create Form'))
        return element
    
    def get_create_flow_marked(self) -> WebElement:
        """Finds and returns the marked bar and icon element from the Create Flow tab."""
        bar_element = self.find_element.by_xpath(self.__bar_tab_marked_locator.replace('TAB_NAME','Create Flow'))
        icon_element = self.find_element.by_xpath(self.__icon_tab_marked_locator.replace('TAB_NAME','Create Flow'))
        return (bar_element & icon_element)
    
    def get_create_flow_error_icon_marked(self) -> WebElement:
        """Finds and returns the marked error icon element from the Create Flow tab."""
        element = self.find_element.by_xpath(self.__icon_error_marked_locator.replace('TAB_NAME','Create Flow'))
        return element
    
    def get_create_flow_unmarked(self) -> WebElement:
        """Finds and returns the unmarked bar and icon element from the Create Flow tab."""
        bar_element = self.find_element.by_xpath(self.__bar_tab_unmarked_locator.replace('TAB_NAME','Create Flow'))
        icon_element = self.find_element.by_xpath(self.__icon_tab_unmarked_locator.replace('TAB_NAME','Create Flow'))
        return (bar_element & icon_element)
    
    def get_create_flow_error_icon_unmarked(self) -> WebElement:
        """Finds and returns the unmarked error icon element from the Create Flow tab."""
        element = self.find_element.by_xpath(self.__icon_error_unmarked_locator.replace('TAB_NAME','Create Flow'))
        return element
    
    def get_permissions_marked(self) -> WebElement:
        """Finds and returns the marked bar and icon element from the Permissions tab."""
        bar_element = self.find_element.by_xpath(self.__bar_tab_marked_locator.replace('TAB_NAME','Permissions'))
        icon_element = self.find_element.by_xpath(self.__icon_tab_marked_locator.replace('TAB_NAME','Permissions'))
        return (bar_element & icon_element)
    
    def get_permissions_error_icon_marked(self) -> WebElement:
        """Finds and returns the marked error icon element from the Permissions tab."""
        element = self.find_element.by_xpath(self.__icon_error_marked_locator.replace('TAB_NAME','Permissions'))
        return element
    
    def get_permissions_unmarked(self) -> WebElement:
        """Finds and returns the unmarked bar and icon element from the Permissions tab."""
        bar_element = self.find_element.by_xpath(self.__bar_tab_unmarked_locator.replace('TAB_NAME','Permissions'))
        icon_element = self.find_element.by_xpath(self.__icon_tab_unmarked_locator.replace('TAB_NAME','Permissions'))
        return (bar_element & icon_element)
    
    def get_permissions_error_icon_unmarked(self) -> WebElement:
        """Finds and returns the unmarked error icon element from the Permissions tab."""
        element = self.find_element.by_xpath(self.__icon_error_unmarked_locator.replace('TAB_NAME','Permissions'))
        return element
    
    def get_publish_marked(self) -> WebElement:
        """Finds and returns the marked bar and icon element from the Publish tab."""
        bar_element = self.find_element.by_xpath(self.__bar_tab_marked_locator.replace('TAB_NAME','Publish'))
        icon_element = self.find_element.by_xpath(self.__icon_tab_marked_locator.replace('TAB_NAME','Publish'))
        return (bar_element & icon_element)
    
    def get_publish_unmarked(self) -> WebElement:
        """Finds and returns the unmarked bar and icon element from the Publish tab."""
        bar_element = self.find_element.by_xpath(self.__bar_tab_unmarked_locator.replace('TAB_NAME','Publish'))
        icon_element = self.find_element.by_xpath(self.__icon_tab_unmarked_locator.replace('TAB_NAME','Publish'))
        return (bar_element & icon_element)
    