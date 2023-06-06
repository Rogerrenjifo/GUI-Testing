from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Projects.ProjectTracing import project_tracing_forms_locators as locators
from Libraries.Drivers.base_page import BasePage


class FormObjects(BasePage):
    """This class represents the forms page on the Projects feature."""

    def get_section_h3(self, section_title: str) -> WebElement:
        """Finds and returns the h3 of the section with the given title."""
        try:
            new_xpath = locators.SECTION_TITLE_H3_LOCATOR.replace("<<value>>", section_title)
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Section with title " + section_title + " not found.")
    
    def get_section_h3_locator(self, section_title: str) -> str:
        """Returns locator of a section."""
        new_xpath = locators.SECTION_TITLE_H3_LOCATOR.replace("<<value>>", section_title)
        return new_xpath
    
    def get_required_field_div(self) -> WebElement:
        """Finds and returns the required field div on project tracing forms."""
        element = self.find_element.by_xpath(locators.FIELD_REQUIRED_DIV_LOCATOR)
        return element
    
    def get_input_field(self, title: str, section_title: str) -> WebElement:
        """Finds and returns a input field with given title in the given section."""
        try:
            new_xpath = locators.FIELD_LOCATOR.replace("<<value>>", title)
            new_xpath = new_xpath.replace("<<section_title>>", section_title)
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Field with title " + title + " in section " + section_title + " not found.")
    
    def get_multiline_input_field(self, title: str, section_title: str) -> WebElement:
        """Finds and returns multiline input text field with given title in the given section."""
        try:
            new_xpath = locators.MULTILINE_FIELD_LOCATOR.replace("<<value>>", title)
            new_xpath = new_xpath.replace("<<section_title>>", section_title)
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
    
    def get_save_button_locator(self) -> str:
        """Returns save button locator."""
        return locators.SAVE_BUTTON_LOCATOR
    
    def get_cancel_button(self) -> WebElement:
        """Finds and returns cancel button."""
        element = self.find_element.by_xpath(locators.CANCEL_BUTTON_LOCATOR)
        return element
    
    def get_cancel_button_locator(self) -> str:
        """Returns cancel button locator."""
        return locators.CANCEL_BUTTON_LOCATOR
    
    def get_edit_button(self, title: str, section_title: str) -> WebElement:
        """Finds and returns Edit button from field with given title in the given section."""
        try:
            new_xpath = locators.EDIT_BUTTON_LOCATOR.replace("<<value>>", title)
            new_xpath = new_xpath.replace("<<section_title>>", section_title)
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Field with title  " + title + " not found.")
    
    def get_edit_button_locator(self, title: str, section_title: str) -> str:
        """Returns edit button locator"""
        new_xpath = locators.EDIT_BUTTON_LOCATOR.replace("<<value>>", title)
        new_xpath = new_xpath.replace("<<section_title>>", section_title)
        return new_xpath
    
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
    
    def get_no_items_found_dropdown_option(self) -> WebElement:
        """Finds and returns the 'No items found' option on the dropdown."""
        element = self.find_element.by_xpath(locators.DROPDOWN_NO_ITEMS_FOUND_LOCATOR)
        return element
        
    def get_checkbox_label(self, title: str, section_title: str) -> WebElement:
        """Finds and returns the clickable checkbox label with the title field given in the section given."""
        new_xpath = locators.CHECKBOX_LABEL_LOCATOR.replace("<<value>>", title).replace("<<section_title>>", section_title)
        element = self.find_element.by_xpath(new_xpath)
        return element
    
    def get_checkbox_value(self, title: str, section_title: str) -> str:
        """Returns the value of a checkbox with the title field given in the section given."""
        new_xpath = locators.CHECKBOX_LABEL_VALUE_LOCATOR.replace("<<value>>", title).replace("<<section_title>>", section_title)
        value = self.find_element.by_xpath(new_xpath).get_attribute('checked')
        return value
    
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
    
    def get_multiline_value(self, title: str, section_title: str) -> str:
        """Returns the value assigned to a multiline text with given title and section names."""
        value = self.get_multiline_input_field(title, section_title).get_attribute('value')
        return value
    
    def get_please_select_user_div(self) -> WebElement:
        """Finds and returns div containing the 'Please select a user form user list' message."""
        element = self.find_element.by_xpath(locators.PLEASE_SELECT_USER_LOCATOR)
        return element
    
    def get_user_list_email_button(self, title: str, section_title: str) -> WebElement:
        """Finds and returns the 'Mail to' button from user list with field title given in the section given."""
        new_xpath = locators.USER_LIST_EMAIL_BUTTON_LOCATOR.replace("<<value>>", title)
        new_xpath = new_xpath.replace("<<section_title>>", section_title)
        element = self.find_element.by_xpath(new_xpath)
        return element
    
    def get_userlist_option(self, name: str) -> WebElement:
        """Finds and returns userlist dropdown option with given name."""
        try:
            new_xpath = locators.USERLIST_DROPDOWN_OPTION_LOCATOR.replace("<<value>>", name)
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Option with name  " + name + " not found.")
