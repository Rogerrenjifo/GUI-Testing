from Blueprint.PageObject.Projects.ProjectTracing.system_objects import ProjectSystemObject
from selenium.webdriver.remote.webelement import WebElement


class ProjectSystemActions(ProjectSystemObject):
    """Represents the system section actions of the Project Tracing"""

    def get_current_step_in_project_system(self) -> str:
        """Returns the current step text"""
        current_step = self.get_current_step_element().text
        return current_step
    
    def get_action_owner_in_project_system(self) -> str:
        """Returns the action owner text"""
        action_owner = self.get_action_owner_element().text
        return action_owner
    
    def get_creation_date_in_project_system(self) -> str:
        """Returns the creation date text"""
        creation_date = self.get_creation_date_element().text
        return creation_date
    
    def get_last_update_in_project_system(self) -> str:
        """Returns the last update text"""
        last_update = self.get_last_update_element().text
        return last_update
    
    def get_closure_date_in_project_system(self) -> str:
        """Returns the closure date text"""
        closure_date = self.get_closure_date_element().text
        return closure_date
    
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

    def select_specific_option_in_project_system(self, option: WebElement):
        """Scroll and select an option of the dropdown"""
        self.action_chains.custom_scroll(option)

    def delete_current_value_in_project_system(self):
        """Clicks clear all button"""
        self.get_clear_all_button_element().click()

    def display_dropdown_in_project_system(self):
        """Displays the dropdown"""
        self.get_arrow_element().click()
