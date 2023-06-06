from Blueprint.PageObject.Projects.ProjectTracing.Header.project_tracing_header_objects import ProjectTracingHeader
from Blueprint.Steps.Actions.CommonElements.delete_dialog_actions import DeleteDialogActions


class ProjectTracingHeaderActions(ProjectTracingHeader):
    """This class represents the actions in the header of the Project Tracing page"""
    
    def __init__(self) -> None:
        super().__init__()
        self.delete_dialog = DeleteDialogActions()
    
    def get_project_tag_text_in_project_tracing(self) -> str:
        """Gets the text of the project tag"""
        project_tag_text = self.get_project_tag().text
        return project_tag_text
    
    def get_project_title_text_in_project_tracing(self) -> str:
        """Gets the text of the project title"""
        project_title_text = self.get_project_title().text
        return project_title_text
    
    def click_delete_button_in_project_tracing(self):
        """Clicks on the Delete button"""
        delete = self.get_delete_button()
        delete.click()

    def click_cancel_button_from_delete_dialog_in_project_tracing(self):
        """Clicks on the Cancel button of the Delete Process dialog. The "click_delete_button" method needs to be
        executed before."""
        self.delete_dialog.click_cancel_dialog_button()

    def click_delete_button_from_delete_dialog_in_project_tracing(self):
        """Clicks on the Delete button of the Delete Process dialog. The "click_delete_button" method needs to be
        executed before."""
        self.delete_dialog.click_delete_dialog_button()

    def click_close_button_from_delete_dialog_in_project_tracing(self):
        """Clicks on the close button of the Delete Process dialog. The "click_delete_button" method needs to be
        executed before."""
        self.delete_dialog.click_close_dialog_button()

    def delete_process_instance_in_project_tracing(self):
        """Deletes a Process Instance from the project tracing page."""
        self.click_delete_button_in_project_tracing()
        self.click_delete_button_from_delete_dialog_in_project_tracing()

    def click_action_button_in_project_tracing(self, button_text: str):
        """Clicks on the action button."""
        action_button = self.get_action_button(button_text)
        action_button.click()            

    def is_disabled_action_button_in_project_tracing(self, button_text: str) -> bool:
        """Returns True when the action button is disabled and False when is enabled."""
        action_button = self.get_action_button(button_text)
        return not action_button.is_enabled()

    def get_no_actions_text_in_project_tracing(self) -> str:
        """Gets the text of the 'No more available actions' label."""
        no_actions_text = self.get_no_actions_label().text
        return no_actions_text

    def cancel_delete_process_instance(self):
        """Cancel delete a Process Instance from the project tracing page."""
        self.click_delete_button_in_project_tracing()
        self.click_cancel_button_from_delete_dialog_in_project_tracing()

    def close_delete_process_instance(self):
        """Closes delete a Process Instance from the project tracing page."""
        self.click_delete_button_in_project_tracing()
        self.click_close_button_from_delete_dialog_in_project_tracing()

    def get_delete_button_in_project_tracing(self):
        """Gets the Delete button"""
        delete_button = self.get_delete_button()
        return delete_button

    def get_the_rgb_background_delete_button(self) -> str:
        """Finds and returns the rgb background of the delete button"""
        action = self.get_delete_button()
        self.action_chains.move_to_an_element(action)
        rgb_background = self.get_delete_button().value_of_css_property('background-color')
        return rgb_background

    def get_the_rgb_background_action_button(self, button_text: str) -> str:
        """Finds and returns the rgb background of the action button"""
        action = self.get_action_button(button_text)
        self.action_chains.move_to_an_element(action)
        rgb_background = self.get_action_button(button_text).value_of_css_property('background-color')
        return rgb_background

    def get_popup_window_delete_process_instance_in_project_tracing(self):
        """Gets popup window deletes process instance"""
        popup_window = self.get_popup_delete_process_instance()
        return popup_window

    def get_cancel_button_form_popup_window_delete_process_instance_in_project_tracing(self):
        """Gets cancel button from popup window deletes process instance"""
        popup_window = self.get_cancel_button_from_delete_process_instance()
        return popup_window

    def get_delete_button_form_popup_window_delete_process_instance_in_project_tracing(self):
        """Gets delete button from popup window deletes process instance"""
        popup_window = self.get_delete_button_from_delete_process_instance()
        return popup_window
