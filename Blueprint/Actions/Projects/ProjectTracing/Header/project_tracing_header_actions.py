from Blueprint.PageObject.Projects.ProjectTracing.Header.project_tracing_header_objects import ProjectTracingHeader
from Blueprint.Actions.CommonElements.delete_dialog_actions import DeleteDialogActions


class ProjectTracingHeaderActions(ProjectTracingHeader):
    """This class represents the actions in the header of the Project Tracing page"""
    
    def __init__(self) -> None:
        super().__init__()
        self.delete_dialog = DeleteDialogActions()
    
    def get_project_tag_text(self) -> str:
        """Gets the text of the project tag"""
        project_tag_text = self.get_project_tag().text
        return project_tag_text
    
    def get_project_title_text(self) -> str:
        """Gets the text of the project title"""
        project_title_text = self.get_project_title().text
        return project_title_text
    
    def click_delete_button(self):
        """Clicks on the Delete button"""
        delete = self.get_delete_button()
        delete.click()

    def click_cancel_button_from_delete_dialog(self):
        """Clicks on the Cancel button of the Delete Process dialog. The "click_delete_button" method needs to be executed before."""
        self.delete_dialog.click_cancel_dialog_button()

    def click_delete_button_from_delete_dialog(self):
        """Clicks on the Delete button of the Delete Process dialog. The "click_delete_button" method needs to be executed before."""
        self.delete_dialog.click_delete_dialog_button()

    def click_close_button_from_delete_dialog(self):
        """Clicks on the close button of the Delete Process dialog. The "click_delete_button" method needs to be executed before."""
        self.delete_dialog.click_close_dialog_button()

    def delete_process_instance(self):
        """Deletes a Process Instance from the project tracing page."""
        self.click_delete_button()
        self.click_delete_button_from_delete_dialog()

    def click_action_button(self, button_text: str):
        """Clicks on the action button."""
        action_button = self.get_action_button(button_text)
        action_button.click()            

    def is_disabled_action_button(self, button_text: str) -> bool:
        """Returns True when the action button is disabled and False when is enabled."""
        action_button = self.get_action_button(button_text)
        return not action_button.is_enabled()

    def get_no_actions_text(self) -> str:
        """Gets the text of the 'No more available actions' label."""
        no_actions_text = self.get_no_actions_label().text
        return no_actions_text

    def cancel_delete_process_instance(self):
        """Cancel delete a Process Instance from the project tracing page."""
        self.click_delete_button()
        self.click_cancel_button_from_delete_dialog()

    def close_delete_process_instance(self):
        """Closes delete a Process Instance from the project tracing page."""
        self.click_delete_button()
        self.click_close_button_from_delete_dialog()
