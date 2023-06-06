from Blueprint.PageObject.Projects.ProjectTracing.system_objects import ProjectSystemObject
from Blueprint.PageObject.Flows.Elements.dropdowns import Dropdownbox


class ProjectSystemActions(ProjectSystemObject):
    """Represents the system section actions of the Project Tracing"""

    def __init__(self):
        super().__init__()
        self.dropdown = Dropdownbox('projects_tracing_system')

    def get_system_title_in_project_tracing_system(self) -> str:
        """Returns the system title text"""
        title = self.get_system_title().text
        return title

    def get_current_step_title_in_project_tracing_system(self) -> str:
        """Returns the current step title text"""
        current_step_title = self.get_current_step_title().text
        return current_step_title

    def get_current_step_in_project_system(self) -> str:
        """Returns the current step text"""
        current_step = self.get_current_step_element().text
        return current_step

    def get_action_owner_title_in_project_tracing_system(self) -> str:
        """Returns the action owner text"""
        action_owner = self.get_action_owner_element().text
        return action_owner

    def get_creation_date_title_in_project_tracing_system(self) -> str:
        """Returns the creation date text"""
        creation_date_title = self.get_creation_date_title().text
        return creation_date_title

    def get_creation_date_data_in_project_tracing_system(self) -> str:
        """Returns creation date text of the project tracing"""
        creation_date_data = self.get_creation_date_element().text
        return creation_date_data

    def get_last_update_title_in_project_tracing_system(self) -> str:
        """Returns the last update text"""
        last_update_title = self.get_last_update_title().text
        return last_update_title

    def get_last_update_data_in_project_tracing_system(self) -> str:
        """Returns last update text of the project tracing"""
        last_update_data = self.get_last_update_element().text
        return last_update_data

    def get_closure_date_title_in_project_tracing_system(self) -> str:
        """Returns the closure date text"""
        closure_date_title = self.get_closure_date_title().text
        return closure_date_title

    def get_closure_date_data_in_project_tracing_system(self) -> str:
        """Returns last update text of the project tracing"""
        closure_date_data = self.get_closure_date_element().text
        return closure_date_data

    def click_edit_current_step_button_in_project_system(self):
        """Clicks edit current step button"""
        self.get_current_step_element().click()
        self.get_edit_current_step_button_element().click()

    def click_edit_action_owner_button_in_project_system(self):
        """Clicks edit action owner button"""
        self.get_action_owner_element().click()
        self.get_edit_action_owner_button_element().click()

    def save_changes_in_project_system(self):
        """Clicks save button"""
        self.get_save_button_element().click()

    def cancel_changes_in_project_system(self):
        """Clicks cancel button"""
        self.get_cancel_button_element().click()

    def select_specific_option_in_project_system(self, option: str):
        """Scroll and select an option of the dropdown"""
        self.dropdown.scroll_down('OPTION', option)

    def delete_current_value_in_project_system(self):
        """Clicks clear all button"""
        self.dropdown.delete_all_options('CLEAR_ALL')

    def display_dropdown_in_project_system(self):
        """Displays the dropdown"""
        self.dropdown.click_drop_arrow('ARROW_LOCATOR')

    def get_options_in_dropdown(self) -> list:
        """Gets the options contents in the dropdown"""
        options_in_dropdown = self.dropdown.get_available_options('DROPDOWN_LIST')
        return options_in_dropdown

    def obtain_all_the_components_of_the_dropdown(self):
        """Gets the selected element contents in the dropdown"""
        dropdown_list = self.dropdown.get_element('DROPDOWN_LIST')
        return dropdown_list

    def get_current_step_button_color(self) -> str:
        """Gets the color of the  current step."""
        color = self.get_css_selector_from_current_step()
        return color

    def get_action_owner_button_color(self) -> str:
        """Gets the color of the current step."""
        color = self.get_css_selector_from_action_owner()
        return color

    def obtain_save_button_element(self):
        """Obtains the save button element"""
        save_element = self.get_save_button_element()
        return save_element

    def obtain_cancel_button_element(self):
        """Obtains the cancel button element"""
        cancel_element = self.get_cancel_button_element()
        return cancel_element

    def obtain_clear_button_element(self):
        """Obtains the clear button element"""
        clear_element = self.get_clear_button_element()
        return clear_element

    def get_the_field_requirement_message(self):
        """Gets the message that the field is required"""
        message_field_requirement = self.get_field_required_element()
        return message_field_requirement
