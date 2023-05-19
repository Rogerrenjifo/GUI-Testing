from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Flows import create_form_properties_panel_locators as locators
from Libraries.Drivers.base_page import BasePage

class PropertiesPanelObjects(BasePage):
    """This class represents the properties panel on the create form tab in the flow page of Blueprint app"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.__section_name_input_locator = locators.SECTION_NAME_INPUT_LOCATOR
        self.__name_input_locator = locators.NAME_INPUT_LOCATOR
        self.__placeholder_input_locator = locators.PLACEHOLDER_INPUT_LOCATOR
        self.__default_value_input_locator = locators.DEFAULT_VALUE_INPUT_LOCATOR
        self.__field_type_select_locator = locators.FIELD_TYPE_SELECT_LOCATOR
        self.__required_field_label_locator = locators.REQUIRED_FIELD_LABEL_LOCATOR
        self.__number_format_select_locator = locators.NUMBER_FORMAT_SELECT_LOCATOR
        self.__number_default_value_formatted_noedit_locator = locators.NUMBER_DEFAULT_VALUE_FORMATTED_NOEDIT_LOCATOR
        self.__checkbox_default_checked_label_locator = locators.CHECKBOX_DEFAULT_CHECKED_LABEL_LOCATOR
        self.__date_default_year_select = locators.DEFAULT_DATE_YEAR_SELECT_LOCATOR
        self.__date_default_month_select = locators.DEFAULT_DATE_MONTH_SELECT_LOCATOR
        self.__date_format_select_locator = locators.DATE_FORMAT_SELECT_LOCATOR
        self.__add_dropdown_value_input_locator = locators.ADD_DROPDOWN_VALUE_INPUT_LOCATOR
        self.__add_dropdown_value_button_locator = locators.ADD_DROPDOWN_VALUE_BUTTON_LOCATOR
        self.__dropdown_values_noedit_locator = locators.DROPDOWN_VALUES_NOEDIT_LOCATOR
        self.__default_value_select_locator = locators.DEFAULT_VALUE_SELECT_LOCATOR
        self.__userlist_values_select_locator = locators.USERLIST_VALUES_SELECT_LOCATOR
    
    def get_section_name_input(self) -> WebElement:
        """Finds and returns section name input."""
        element = self.find_element.by_xpath(self.__section_name_input_locator)
        return element
    
    def get_name_input(self) -> WebElement:
        """Finds and returns name input."""
        element = self.find_element.by_xpath(self.__name_input_locator)
        return element
    
    def get_placeholder_input(self) -> WebElement:
        """Finds and returns placeholder input."""
        element = self.find_element.by_xpath(self.__placeholder_input_locator)
        return element
    
    def get_default_value_input(self) -> WebElement:
        """Finds and returns default value input."""
        element = self.find_element.by_xpath(self.__default_value_input_locator)
        return element
    
    def get_field_type_select(self) -> WebElement:
        """Finds and returns field type select."""
        element = self.find_element.by_xpath(self.__field_type_select_locator)
        return element
    
    def get_field_type_select_option(self, value: str) -> WebElement:
        """Finds and returns field type option"""
        new_xpath = "//span[@class='ng-option-label' and text()='"+value+"']"
        try:
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Option "+value+" not found.")
    
    def get_required_field_label(self) -> WebElement:
        """Finds and returns required field label."""
        element = self.find_element.by_xpath(self.__required_field_label_locator)
        return element
    
    def get_number_format_select(self) -> WebElement:
        """Finds and returns section number format select."""
        element = self.find_element.by_xpath(self.__number_format_select_locator)
        return element
    
    def get_number_default_value_formatted_noedit(self) -> WebElement:
        """Finds and returns number default value formatted no edit."""
        element = self.find_element.by_xpath(self.__number_default_value_formatted_noedit_locator)
        return element
    
    def get_checkbox_default_checked_label(self) -> WebElement:
        """Finds and returns checkbox default checked label."""
        element = self.find_element.by_xpath(self.__checkbox_default_checked_label_locator)
        return element
    
    def get_date_default_year_select(self) -> WebElement:
        """Finds and returns date default value year select."""
        element = self.find_element.by_xpath(self.__date_default_year_select)
        return element
    
    def get_date_default_year_value(self, year: str) -> WebElement:
        """Finds and returns a year value from the dropdaown with the required value."""
        new_xpath = "//div[@class='item-container selected' or @class='item-container']//child::a[text()=' " + year + " ']"
        try:
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Year  " + year + " not found.")
    
    def get_date_default_month_select(self) -> WebElement:
        """Finds and returns date default value month select."""
        element = self.find_element.by_xpath(self.__date_default_month_select)
        return element
    
    def get_date_default_month_value(self, month: str) -> WebElement:
        """Finds and returns a month value from the dropdaown with the required value."""
        new_xpath = "//div[@class='item-container selected' or @class='item-container']//child::a[text()=' " + month + " ']"
        try:
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Month  " + month + " not found.")
    
    def get_date_default_day_value(self, day: str) -> WebElement:
        """Finds and returns a day value from the dropdaown with the required value."""
        new_xpath = "//div[@class='calendar-table-cell' and text()=' " + day + " ']"
        try:
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Day  " + day + " not found.")
    
    def get_date_format_select(self) -> WebElement:
        """Finds and returns date format select."""
        element = self.find_element.by_xpath(self.__date_format_select_locator)
        return element
    
    def get_add_dropdown_value_input(self) -> WebElement:
        """Finds and returns add dropdown value input."""
        element = self.find_element.by_xpath(self.__add_dropdown_value_input_locator)
        return element
    
    def get_add_dropdown_value_button(self) -> WebElement:
        """Finds and returns add dropdown value button."""
        element = self.find_element.by_xpath(self.__add_dropdown_value_button_locator)
        return element
    
    def get_dropdown_values_noedit(self) -> WebElement:
        """Finds and returns dropdown values noedit."""
        element = self.find_element.by_xpath(self.__dropdown_values_noedit_locator)
        return element
    
    def get_added_dropdown_value(self, value: str) -> WebElement:
        """Finds and returns added dropdown value with text of the value."""
        new_xpath = "//p[@title='"+value+"']"
        try:
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Added dropdown value with text "+value+" not found.")
    
    def get_added_dropdown_value_delete_button(self, value: str) -> WebElement:
        """Finds and returns delete button of an added dropdown value with text of the value."""
        new_xpath = "//p[@class='flex-1 default-overflow-full' and text()=' " + value + " ']//following::button[1]"
        try:
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Added dropdown value with text "+value+" not found.")
        
    def get_default_value_select(self) -> WebElement:
        """Finds and returns default value select."""
        element = self.find_element.by_xpath(self.__default_value_select_locator)
        return element
    
    def get_default_value_select_value(self, value: str) -> WebElement:
        """Finds and returns dropdown default value selectable element with text of the value."""
        new_xpath = "//div[@class='selectable-overflow-full' and text()=' " + value + " ']"
        try:
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Added dropdown value with text "+value+" not found.")
    
    def get_userlist_values_select(self) -> WebElement:
        """Finds and returns userlist values select."""
        element = self.find_element.by_xpath(self.__userlist_values_select_locator)
        return element

    def get_userlist_value(self, name: str) -> WebElement:
        """Finds and returns userlist option with value name given."""
        new_xpath = "//span[@title='"+ name + "']"
        try:
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("User or group with name "+name+" not found.")
    
    def get_userlist_default_value_option(self, name: str) -> WebElement:
        """Finds and returns userlist default value option with value name given."""
        new_xpath = "//span[@class='ng-option-label' and text()='" + name + "']"
        try:
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("User or group with name " + name + " not found.")