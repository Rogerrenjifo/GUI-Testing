from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Flows import header_locators as locators
from Libraries.Drivers.base_page import BasePage


class Header(BasePage):
    """This class represents the header of the Flow feature"""    
    
    def get_flow_status(self) -> WebElement:
        """Finds and returns the flow status element of the header."""
        element = self.find_element.by_xpath(locators.STATUS)
        return element
    
    def get_flow_version(self) -> WebElement:
        """Finds and returns the flow version element of the header."""
        element = self.find_element.by_xpath(locators.VERSION)
        return element
    
    def get_flow_name(self) -> WebElement:
        """Finds and returns the flow name element of the header."""
        element = self.find_element.by_xpath(locators.FLOW_NAME)
        return element
    
    def get_dropdown_button(self) -> WebElement:
        """Finds and returns the dropdown element of the header."""
        element = self.find_element.by_xpath(locators.FLOW_DROPDOWN)
        return element
    
    def get_delete_option(self) -> WebElement:
        """Finds and returns the delete option element in the dropdown of the header."""
        element = self.find_element.by_xpath(locators.DELETE)
        return element    
    
    def get_select_version_option(self) -> WebElement:
        """Finds and returns the select version element in the dropdown of the header."""
        element = self.find_element.by_xpath(locators.SELECT_VERSION)
        return element
    
    def get_version_list(self) -> WebElement:
        """Finds and returns the version list element in the dropdown of the header."""
        element = self.find_element.by_xpath(locators.VERSIONS_LIST)
        return element
    
    def get_specific_version(self, version: str) -> WebElement:
        """Finds and returns a version from the select version list."""
        element = self.find_element.by_xpath(locators.VERSIONS.replace('<<value>>', version))
        return element
    
    def get_last_updated(self) -> WebElement:
        """Finds and returns the updated text element of the header."""
        element = self.find_element.by_xpath(locators.LAST_UPDATED_TEXT)
        return element
    
    def get_save_button(self) -> WebElement:
        """Finds and returns the Save button element of the header."""
        element = self.find_element.by_class(locators.SAVE_BUTTON)
        return element
    
    def get_save_next_button(self) -> WebElement:
        """Finds and returns the Save & Next button element of the header."""
        element = self.find_element.by_class(locators.SAVE_NEXT_BUTTON)
        return element  
    
    def get_tab(self, tab_name: str) -> WebElement:
        """Finds and returns the bar element from the selected tab."""
        bar_element = self.find_element.by_xpath(locators.BAR_TAB.replace('TAB_NAME', tab_name))
        return bar_element
    
    def is_marked_tab_elements(self, tab_name: str) -> WebElement:
        """Finds the marked bar and icon element from the selected tab."""
        try:
            self.find_element.by_xpath(locators.BAR_TAB_MARKED.replace('TAB_NAME', tab_name))
            self.find_element.by_xpath(locators.ICON_TAB_MARKED.replace('TAB_NAME', tab_name))
            return True
        except Exception:
            return False
    
    def is_unmarked_tab_elements(self, tab_name: str) -> WebElement:
        """Finds the unmarked bar and icon element from the selected tab."""
        try:
            self.find_element.by_xpath(locators.BAR_TAB_UNMARKED.replace('TAB_NAME', tab_name))
            self.find_element.by_xpath(locators.ICON_TAB_UNMARKED.replace('TAB_NAME', tab_name))
            return True
        except Exception:
            return False
    
    def is_error_marked_tab_elements(self, tab_name: str) -> WebElement:
        """Finds the marked bar and error icon element from the selected tab."""
        try:
            self.find_element.by_xpath(locators.BAR_TAB_MARKED.replace('TAB_NAME', tab_name))
            self.find_element.by_xpath(locators.ICON_ERROR_MARKED.replace('TAB_NAME', tab_name))
            return True
        except Exception:
            return False
    
    def is_error_unmarked_tab_elements(self, tab_name: str) -> WebElement:
        """Finds the unmarked bar and error icon element from the selected tab."""
        try:
            self.find_element.by_xpath(locators.BAR_TAB_UNMARKED.replace('TAB_NAME', tab_name))
            self.find_element.by_xpath(locators.ICON_ERROR_UNMARKED .replace('TAB_NAME', tab_name))
            return True
        except Exception:
            return False
