from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Flows import header_locators as locators
from Libraries.Drivers.base_page import BasePage

class Header(BasePage):
    """This class represents the header of the Flow feature"""

    def __init__(self, driver):
        super().__init__(driver)
        self.__status_locator = locators.STATUS
        self.__version_locator = locators.VERSION
        self.__flow_name_locator = locators.FLOW_NAME
        self.__flow_dropdown = locators.FLOW_DROPDOWN
        self.__delete_locator = locators.DELETE
        self.__cancel_button_locator = locators.CANCEL_BUTTON
        self.__delete_button_locator = locators.DELETE_BUTTON
        self.__close_button_locator = locators.CLOSE_BUTTON
        self.__select_version_locator = locators.SELECT_VERSION
        self.__versions_locator = locators.VERSIONS
        self.__update_text_locator = locators.UPDATE_TEXT
        self.__save_button_locator = locators.SAVE_BUTTON
        self.__save_next_button_locator = locators.SAVE_NEXT_BUTTON
        self.__tab_locator = locators.BAR_TAB
        self.__bar_tab_marked_locator = locators.BAR_TAB_MARKED
        self.__icon_tab_marked_locator = locators.ICON_TAB_MARKED
        self.__icon_error_marked_locator = locators.ICON_ERROR_MARKED
        self.__bar_tab_unmarked_locator = locators.BAR_TAB_UNMARKED
        self.__icon_tab_unmarked_locator = locators.ICON_TAB_UNMARKED
        self.__icon_error_unmarked_locator = locators.ICON_ERROR_UNMARKED 
    
    def get_status(self) -> WebElement:
        """Finds and returns the flow status element of the header."""
        element = self.find_element.by_xpath(self.__status_locator)
        return element
    
    def get_version(self) -> WebElement:
        """Finds and returns the flow version element of the header."""
        element = self.find_element.by_xpath(self.__version_locator)
        return element
    
    def get_flow_name(self) -> WebElement:
        """Finds and returns the flow name element of the header."""
        element = self.find_element.by_xpath(self.__flow_name_locator)
        return element
    
    def get_dropdown_button(self) -> WebElement:
        """Finds and returns the dropdown element of the header."""
        element = self.find_element.by_xpath(self.__flow_dropdown)
        return element
    
    def get_delete_option(self) -> WebElement:
        """Finds and returns the delete option element in the dropdown of the header."""
        element = self.find_element.by_xpath(self.__delete_locator)
        return element
    
    def get_cancel_button(self) -> WebElement:
        """Finds and returns the Cancel button element of the Delete Process dialog."""
        element = self.find_element.by_xpath(self.__cancel_button_locator)
        return element
    
    def get_delete_button(self) -> WebElement:
        """Finds and returns the Delete button element of the Delete Process dialog."""
        element = self.find_element.by_xpath(self.__delete_button_locator)
        return element
    
    def get_close_button(self) -> WebElement:
        """Finds and returns the close button element of the Delete Process dialog."""
        element = self.find_element.by_xpath(self.__close_button_locator)
        return element
    
    def get_select_version_option(self) -> WebElement:
        """Finds and returns the select version element in the dropdown of the header."""
        element = self.find_element.by_xpath(self.__select_version_locator)
        return element
    
    def get_specific_version(self, version: str) -> WebElement:
        """Finds and returns a version from the select version list."""
        element = self.find_element.by_xpath(self.__versions_locator.replace('v1', version))
        return element
    
    def get_last_updated(self) -> WebElement:
        """Finds and returns the updated text element of the header."""
        element = self.find_element.by_xpath(self.__update_text_locator)
        return element
    
    def get_save_button(self) -> WebElement:
        """Finds and returns the Save button element of the header."""
        element = self.find_element.by_class(self.__save_button_locator)
        return element
    
    def get_save_next_button(self) -> WebElement:
        """Finds and returns the Save & Next button element of the header."""
        element = self.find_element.by_class(self.__save_next_button_locator)
        return element  
    
    def get_tab(self, tab_name: str) -> WebElement:
        """Finds and returns the bar element from the selected tab."""
        bar_element = self.find_element.by_xpath(self.__tab_locator.replace('TAB_NAME', tab_name))
        return bar_element
    
    def is_marked_tab_elements(self, tab_name: str) -> WebElement:
        """Finds the marked bar and icon element from the selected tab."""
        try:
            self.find_element.by_xpath(self.__bar_tab_marked_locator.replace('TAB_NAME', tab_name))
            self.find_element.by_xpath(self.__icon_tab_marked_locator.replace('TAB_NAME', tab_name))
            return True
        except Exception:
            return False
    
    def is_unmarked_tab_elements(self, tab_name: str) -> WebElement:
        """Finds the unmarked bar and icon element from the selected tab."""
        try:
            self.find_element.by_xpath(self.__bar_tab_unmarked_locator.replace('TAB_NAME', tab_name))
            self.find_element.by_xpath(self.__icon_tab_unmarked_locator.replace('TAB_NAME', tab_name))
            return True
        except Exception:
            return False
    
    def is_error_marked_tab_elements(self, tab_name: str) -> WebElement:
        """Finds the marked bar and error icon element from the selected tab."""
        try:
            self.find_element.by_xpath(self.__bar_tab_marked_locator.replace('TAB_NAME', tab_name))
            self.find_element.by_xpath(self.__icon_error_marked_locator.replace('TAB_NAME', tab_name))
            return True
        except Exception:
            return False
    
    def is_error_unmarked_tab_elements(self, tab_name: str) -> WebElement:
        """Finds the unmarked bar and error icon element from the selected tab."""
        try:
            self.find_element.by_xpath(self.__bar_tab_unmarked_locator.replace('TAB_NAME', tab_name))
            self.find_element.by_xpath(self.__icon_error_unmarked_locator.replace('TAB_NAME', tab_name))
            return True
        except Exception:
            return False
