from Blueprint.PageObject.Projects.ProjectTracing.project_tracing_forms_objects import FormObjects
from Blueprint.Steps.Actions.CommonElements.date_actions import DateActions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys


class FormsActions(FormObjects):
    """This class represents the forms actions on the project tracing page."""

    def wait_for_project_forms_page_to_load_in_project_forms(self, section_title: str):
        """Waits for project tracing page to load."""
        xpath = self.get_section_h3_locator(section_title)
        self.wait_for_element.wait_for_element_with_xpath(xpath)
    
    def wait_for_edit_button_to_load_in_project_forms(self, field_title: str, section_title: str):
        """Waits for edit button to appear on screen."""
        xpath = self.get_edit_button_locator(field_title, section_title)
        self.wait_for_element.wait_for_element_with_xpath(xpath)        
    
    def wait_for_save_button_to_load_in_project_forms(self):
        """Waits for edit button to appear on screen."""
        xpath = self.get_save_button_locator()
        self.wait_for_element.wait_for_element_with_xpath(xpath)
    
    def click_section_title_in_project_forms(self, section_title: str):
        """Clicks the section title with the given name."""
        self.get_section_h3(section_title).click()

    def move_mouse_hover_field_in_project_forms(self, field_title: str, section_title: str):
        """Puts the mouse hover a field with the given title in the given section."""
        self.action_chains.move_to_an_element(self.get_input_field(field_title, section_title))
    
    def click_input_field_in_project_forms(self, field_title: str, section_title: str):
        """Click input field of section with given title."""
        self.get_input_field(field_title, section_title).click()
    
    def select_field_to_edit_in_project_forms(self, field_title: str, section_title: str):
        """Selects a field with title given to be editable in the given section."""
        self.get_input_field(field_title, section_title).click()
        self.get_edit_button(field_title, section_title).click()

    def clear_text_input_in_project_forms(self, field_title: str, section_title: str):
        """Clears text field in the given section."""
        self.select_field_to_edit_in_project_forms(field_title, section_title)
        self.get_editable_text_input().clear()
    
    def get_editable_input_text_in_project_forms(self) -> str:
        """Gets editable text input text."""
        return self.get_editable_text_input().get_attribute('value')
    
    def get_editable_input_number_in_project_forms(self) -> str:
        """Gets value on editable numeric input."""
        return self.get_editable_number_input().get_attribute('value')
        
    def set_text_input_in_project_forms(self, field_title: str, section_title: str, input_text: str):
        """Edits text field into given value in the given section."""
        self.select_field_to_edit_in_project_forms(field_title, section_title)
        self.get_editable_text_input().clear()
        self.get_editable_text_input().send_keys(input_text)

    def set_empty_input_in_project_forms(self, field_title: str, section_title: str):
        """Clears text input with given title in the given section."""
        self.select_field_to_edit_in_project_forms(field_title, section_title)
        self.get_editable_text_input().send_keys(Keys.CONTROL + "a")
        self.get_editable_text_input().send_keys(Keys.DELETE)
    
    def click_save_changes_in_project_forms(self):
        """Saves changes made on the editing field."""
        self.get_save_button().click()
        
    def click_cancel_changes_in_project_forms(self):
        """Cancels changes made on the editing field."""
        self.get_cancel_button().click()

    def click_clear_all_dropdown_button_in_project_forms(self):
        """Clicks clear all button on dropdown field."""
        self.get_dropdown_clear_all_button().click()
    
    def set_dropdown_value_in_project_forms(self, field_title: str, section_title: str, value: str):
        """Edits and selects dropdown value from dropdown field with given name and value in the given section."""
        self.select_field_to_edit_in_project_forms(field_title, section_title)
        self.get_dropdown_clear_all_button().click()
        self.get_editable_text_input().click()
        self.get_dropdown_option(value).click()

    def set_numeric_input_in_project_forms(self, field_title: str, section_title: str, value: str):
        """Sets a given value on a numeric input with field title given in the given section."""
        self.select_field_to_edit_in_project_forms(field_title, section_title)
        self.get_editable_number_input().clear()
        self.get_editable_number_input().send_keys(value)

    def press_up_arrow_on_numeric_field_in_project_forms(self):
        """Presses the up arrow on a numeric field input."""
        self.get_editable_number_input().send_keys(Keys.ARROW_UP)
    
    def press_down_arrow_on_numeric_field_in_project_forms(self):
        """Presses the down arrow on a numeric field input."""
        self.get_editable_number_input().send_keys(Keys.ARROW_DOWN)
        
    def click_checkbox_label_in_project_forms(self, field_title: str, section_title: str):
        """Selects or des-selects a checkbox with field title given in the given section."""
        self.select_field_to_edit_in_project_forms(field_title, section_title)
        self.get_checkbox_label(field_title, section_title).click()

    def edit_date_in_project_forms(self, field_title: str, section_title: str, year: str, month: str, day: str):
        """Selects a date on the field with the title given in the given section."""
        self.select_field_to_edit_in_project_forms(field_title, section_title)
        self.get_editable_text_input().click()
        DateActions().set_date(year, month, day)

    def set_multiline_text_input_in_project_forms(self, field_title: str, section_title: str, input_text: str):
        """Edits multiline text field into given value in the given section."""
        self.get_multiline_input_field(field_title, section_title).click()
        self.get_edit_button(field_title, section_title).click()
        self.get_multiline_editable_input().clear()
        self.get_multiline_editable_input().send_keys(input_text)

    def select_user_from_userlist_in_project_forms(self, field_title: str, section_title: str, user_name: str):
        """Selects a user from userlist with given title."""
        self.select_field_to_edit_in_project_forms(field_title, section_title)
        self.get_dropdown_clear_all_button().click()
        self.get_editable_text_input().click()
        self.get_userlist_option(user_name).click()
