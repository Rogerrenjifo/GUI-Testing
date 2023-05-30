from Blueprint.PageObject.Projects.ProjectPage.project_page_objects import ProjectPageObjects
from selenium.webdriver.support.ui import Select
from Blueprint.Steps.Actions.CommonElements.delete_dialog_actions import DeleteDialogActions


class ProjectPageActions(ProjectPageObjects):
    """This class represents the Project PAge actions of a Blueprint application"""
    def __init__(self):
        super().__init__()
        self.delete_dialog = DeleteDialogActions()

    def click_on_new_request_button(self):
        """Clicks the new request button."""
        button = self.get_project_new_request_button()
        button.click()

    def hover_new_request_button(self):
        """Position the mouse pointer over the element."""
        button = self.get_project_new_request_button()
        self.action_chains.move_to_an_element(button)

    def click_on_row_in_a_project_instance(self, project_id: str):
        """Clicks the table row according to the project id."""
        row = self.get_table_row(project_id)["project_row"]
        row.click()

    def click_on_id_in_project_instance(self, project_id: str):
        """Clicks on the project id."""
        project_id_element = self.get_table_row(project_id)["id"]
        project_id_element.click()

    def click_action_button_in_project_instance(self, project_id: str):
        """Clicks the action menu of a row."""
        button = self.get_table_row(project_id)["project_actions_button"]
        button.click()

    def click_action_delete_button_project_instance(self, project_id: str):
        """Clicks the delete option of a row's action menu."""
        button = self.get_table_row(project_id)["project_actions_delete"]
        button.click()

    def hover_action_delete_button_in_project_instance(self, project_id: str):
        """Position the mouse pointer over the element."""
        button = self.get_table_row(project_id)["project_actions_delete"]
        self.action_chains.move_to_an_element(button)

    def click_dialog_close_button_in_a_project_instance(self):
        """Clicks the close button of a delete dialog."""
        self.delete_dialog.click_close_dialog_button()

    def hover_dialog_close_button_in_project_instance(self):
        """Position the mouse pointer over the element."""
        button = self.delete_dialog.get_close_dialog_button()
        self.action_chains.move_to_an_element(button)

    def click_dialog_cancel_button_in_project_instance(self):
        """Clicks the cancel button of a delete dialog."""
        self.delete_dialog.click_cancel_dialog_button()

    def hover_dialog_cancel_button_in_project_instance(self):
        """Position the mouse pointer over the element."""
        button = self.delete_dialog.get_cancel_dialog_button()
        self.action_chains.move_to_an_element(button)

    def click_dialog_delete_button_in_project_instance(self):
        """Clicks the delete button of a delete dialog."""
        self.delete_dialog.click_delete_dialog_button()

    def hover_dialog_delete_button_in_project_instance(self):
        """Position the mouse pointer over the element."""
        button = self.delete_dialog.get_delete_dialog_button()
        self.action_chains.move_to_an_element(button)

    def click_select_row_pagination_in_project_page(self):
        """Clicks the select row pagination element."""
        select = self.get_select_row_pagination()
        select.click()

    def select_pagination_option_in_project_page(self, value: str):
        """Selects the row pagination option from the select element."""
        select = Select(self.get_select_row_pagination())
        select.select_by_value(value)

    def click_previous_page_button_in_project_page(self):
        """Clicks the previous page button."""
        button = self.get_previous_page_button()
        button.click()

    def click_next_page_button_in_project_page(self):
        """Clicks the next page button."""
        button = self.get_next_page_button()
        button.click()

    def click_page_number_button_in_project_page(self, page_number: str):
        """Clicks a specific page nuber button."""
        button = self.get_page_number_button(page_number)
        button.click()

    def hover_page_number_button_in_project_page(self, page_number: str):
        """Position the mouse pointer over the element."""
        button = self.get_page_number_button(page_number)
        self.action_chains.move_to_an_element(button)

    def get_project_details_in_project_page(self, project_id: str) -> dict:
        """Returns the text of each element of a project."""
        row = self.get_table_row(project_id)
        project = {
            "checkbox": row["project_checkbox"].is_selected(),
            "id": project_id,
            "title": row["project_title"].text,
            "current_step": row["project_current_step"].text,
            "owner": row["project_owner"].text,
            "creator": row["project_creator"].text,
            "date_created": row["project_date_created"].text,
            "closure_date": row["project_closure_date"].text
        }
        return project

    def get_project_name_text_in_project_page(self) -> str:
        """Returns the text of the project name"""
        text = self.get_project_name().text
        return text

    def delete_project_instance_process_in_project_page(self, project_id: str):
        """Deletes a project instance"""
        self.click_action_button_in_project_instance(project_id)
        self.click_action_delete_button_project_instance(project_id)
        self.click_dialog_delete_button_in_project_instance()

    def cancel_delete_project_instance_process_in_project_page(self, project_id: str):
        """Cancel delete a project instance process"""
        self.click_action_button_in_project_instance(project_id)
        self.click_action_delete_button_project_instance(project_id)
        self.click_dialog_cancel_button_in_project_instance()

    def close_delete_project_instance_process_in_project_page(self, project_id: str):
        """Closes delete a project instance process"""
        self.click_action_button_in_project_instance(project_id)
        self.click_action_delete_button_project_instance(project_id)
        self.click_dialog_close_button_in_a_project_instance()
