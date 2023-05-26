from Blueprint.PageObject.Projects.ProjectTracing.project_tracing_forms_objects import FormObjects
from Blueprint.Actions.CommonElements.date_actions import DateActions


class FormsActions(FormObjects):
    """This class represents the forms actions on the project tracing page."""

    def select_field_to_edit_in_project_forms(self, field_title: str):
        """Selects a field with title given to be editable."""
        self.get_input_field(field_title).click()
        self.get_edit_button(field_title).click()

    def set_text_input_in_project_forms(self, field_title: str, input_text: str):
        """Edits text field into given value."""
        self.select_field_to_edit_in_project_forms(field_title)
        self.get_editable_text_input().clear()
        self.get_editable_text_input().send_keys(input_text)

    def click_save_changes_in_project_forms(self):
        """Saves changes made on the editing field."""
        self.get_save_button().click()

    def click_cancel_changes_in_project_forms(self):
        """Cancels changes made on the editing field."""
        self.get_cancel_button().click()

    def set_dropdown_value_in_project_forms(self, field_title: str, value: str):
        """Edits and selects dropdown value from dropdown field with given name and value."""
        self.select_field_to_edit_in_project_forms(field_title)
        self.get_dropdown_clear_all_button().click()
        self.get_editable_text_input().click()
        self.get_dropdown_option(value).click()

    def set_numeric_input_in_project_forms(self, field_title: str, value: str):
        """Sets a given value on a numeric input with field title given."""
        self.select_field_to_edit_in_project_forms(field_title)
        self.get_editable_number_input().clear()
        self.get_editable_number_input().send_keys(value)

    def click_checkbox_label_in_project_forms(self, field_title: str):
        """Selects or des-selects a checkbox with field title given."""
        self.select_field_to_edit_in_project_forms(field_title)
        self.get_checkbox_label(field_title).click()

    def edit_date_in_project_forms(self, field_title: str, year: str, month: str, day: str):
        """Selects a date on the field with the title given."""
        self.select_field_to_edit_in_project_forms(field_title)
        self.get_editable_text_input().click()
        DateActions().set_date(year, month, day)

    def set_multiline_text_input_in_project_forms(self, field_title: str, input_text: str):
        """Edits multiline text field into given value."""
        self.get_multiline_input_field(field_title).click()
        self.get_edit_button(field_title).click()
        self.get_multiline_editable_input().clear()
        self.get_multiline_editable_input().send_keys(input_text)

    def select_user_from_userlist_in_project_forms(self, field_title: str, user_name: str):
        """Selects a user from userlist with given title."""
        self.select_field_to_edit_in_project_forms(field_title)
        self.get_dropdown_clear_all_button().click()
        self.get_editable_text_input().click()
        self.get_userlist_option(user_name).click()
