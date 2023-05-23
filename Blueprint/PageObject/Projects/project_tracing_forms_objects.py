from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Projects import project_tracing_forms_locators as locators
from Libraries.Drivers.base_page import BasePage


class FormObjects(BasePage):
    """This class represents the forms page on the Projects feature."""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_input_field(self, title: str) -> WebElement:
        """Finds and returns a input field with title given."""
        try:
            new_xpath = locators.FIELD_LOCATOR.replace("<<value>>", title)
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Field with title  " + title + " not found.")
    
    def get_multiline_input_field(self, title: str) -> WebElement:
        """Finds and returns multiline input text field with given title."""
        try:
            new_xpath = locators.MULTILINE_FIELD_LOCATOR.replace("<<value>>", title)
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Field with title  " + title + " not found.")
    
    def get_editable_text_input(self) -> WebElement:
        """Finds and returns editable text input."""
        element = self.find_element.by_xpath(locators.EDITABLE_TEXT_INPUT_LOCATOR)
        return element
    
    def get_editable_number_input(self) -> WebElement:
        """Finds and returns editable number input."""
        element = self.find_element.by_xpath(locators.EDITABLE_NUMBER_INPUT_LOCATOR)
        return element    
    
    def get_save_button(self) -> WebElement:
        """Finds and returns save button."""
        element = self.find_element.by_xpath(locators.SAVE_BUTTON_LOCATOR)
        return element
    
    def get_cancel_button(self) -> WebElement:
        """Finds and returns cancel button."""
        element = self.find_element.by_xpath(locators.CANCEL_BUTTON_LOCATOR)
        return element
    
    def get_edit_button(self, title: str) -> WebElement:
        """Finds and returns Edit button from field with given title."""
        try:
            new_xpath = locators.EDIT_BUTTON_LOCATOR.replace("<<value>>", title)
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Field with title  " + title + " not found.")
    
    def get_dropdown_clear_all_button(self) -> WebElement:
        """Finds and returns the 'Clear all' dropdown button."""
        element = self.find_element.by_xpath(locators.CLEAR_ALL_DROPDOWN_BUTTON)
        return element
    
    def get_dropdown_option(self, value: str) -> WebElement:
        """Finds and returns selectablle option from dropdown with given value."""
        try:
            new_xpath = locators.DROPDOWN_OPTION_LOCATOR.replace("<<value>>", value)
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Option with value  " + value + " not found.")
        
    def get_checkbox_label(self, title: str) -> WebElement:
        """Finds and returns the clickable checkbox label with the title field given."""
        element = self.find_element.by_xpath(locators.CHECKBOX_LABEL_LOCATOR.replace("<<value>>", title))
        return element
    
    def get_select_date_input(self) -> WebElement:
        """Finds and returns select date input."""
        element = self.find_element.by_xpath(locators.SELECT_DATE_INPUT_LOCATOR)
        return element
    
    def get_date_clear_all_button(self) -> WebElement:
        """Finds and returns the 'Clear all' button for dates."""
        element = self.find_element.by_xpath(locators.DELETE_DATE_BUTTON_LOCATOR)
        return element
    
    def get_date_calendar_button(self) -> WebElement:
        """Finds and returns the calendar button for dates."""
        element = self.find_element.by_xpath(locators.CALENDAR_DATE_BUTTON_LOCATOR)
        return element
    
    def get_multiline_editable_input(self) -> WebElement:
        """Finds and returns editable multiline text input."""
        element = self.find_element.by_xpath(locators.EDITABLE_MULTILINE_INPUT_LOCATOR)
        return element
    
    def get_user_list_email_button(self, title: str) -> WebElement:
        """Finds and returns the 'Mail to' button from user list with field title given."""
        element = self.find_element.by_xpath(locators.USER_LIST_EMAIL_BUTTON_LOCATOR.replace("<<value>>", title))
        return element
    
    def get_userlist_option(self, name: str) -> WebElement:
        """Finds and returns userlist dropdown option with given name."""
        try:
            new_xpath = locators.USERLIST_DROPDOWN_OPTION_LOCATOR.replace("<<value>>", name)
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Option with name  " + name + " not found.")
