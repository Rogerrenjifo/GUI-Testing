from Blueprint.PageObject.Projects.ProjectTracing.project_tracing_forms_objects import FormObjects


class FormsActions(FormObjects):
    """This class represents the forms actions on the project tracing page."""
    
    def select_field_to_edit(self, field_title: str):
        """Selects a field with title given to be editable."""
        self.get_input_field(field_title).click()
        self.get_edit_button(field_title).click()
    
    def set_text_input(self, field_title: str, input_text: str):
        """Edits text field into given value."""
        self.select_field_to_edit(field_title)
        self.get_editable_text_input().clear()
        self.get_editable_text_input().send_keys(input_text)
    
    def click_save_changes(self):
        """Saves changes made on the editing field."""
        self.get_save_button().click()

    def click_cancel_changes(self):
        """Cancels changes made on the editing field."""
        self.get_cancel_button().click()
    
    def set_dropdown_value(self, field_title: str, value: str):
        """Edits and selects dropdown value from dropdown field with given name and value."""
        self.select_field_to_edit(field_title)
        self.get_dropdown_clear_all_button().click()
        self.get_editable_text_input().click()
        self.get_dropdown_option(value).click()
    
    def set_numeric_input(self, field_title: str, value: str):
        """Sets a given value on a numeric input with field title given."""
        self.select_field_to_edit(field_title)
        self.get_editable_number_input().clear()
        self.get_editable_number_input().send_keys(value)
    
    def click_checkbox_label(self, field_title: str):
        """Selects or des-selects a checkbox with field title given."""
        self.select_field_to_edit(field_title)
        self.get_checkbox_label(field_title).click()
    
    def edit_date(self, field_title: str, year: str, month: str, day: str):
        """Seleects a date on the field with the title given."""
        self.select_field_to_edit(field_title)
        self.get_editable_text_input().click()
    
    def set_multiline_text_input(self, field_title: str, input_text: str):
        """Edits multiline text field into given value."""
        self.get_multiline_input_field(field_title).click()
        self.get_edit_button(field_title).click()
        self.get_multiline_editable_input().clear()
        self.get_multiline_editable_input().send_keys(input_text)
        
    def select_user_from_userlist(self, field_title: str, user_name: str):
        """Selects a user from userlist with given title."""
        self.select_field_to_edit(field_title)
        self.get_dropdown_clear_all_button().click()
        self.get_editable_text_input().click()
        self.get_userlist_option(user_name).click()
