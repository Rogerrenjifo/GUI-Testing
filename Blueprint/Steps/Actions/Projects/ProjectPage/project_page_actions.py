from typing import List
from selenium.webdriver.remote.webelement import WebElement
from Blueprint.PageObject.Projects.ProjectPage.project_page_objects import ProjectPageObjects
from selenium.webdriver.support.ui import Select
from Blueprint.Steps.Actions.CommonElements.delete_dialog_actions import DeleteDialogActions
from Blueprint.Steps.Actions.CommonElements.popup_messages_actions import PopUpMessagesActions
from Blueprint.Steps.Actions.Projects.ProjectPage.export_dialog_actions import ExportDialogActions


class ProjectPageActions(ProjectPageObjects):
    """This class represents the Project PAge actions of a Blueprint application"""
    def __init__(self):
        super().__init__()
        self.delete_dialog = DeleteDialogActions()
        self.popup = PopUpMessagesActions()

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
    
    def click_on_checkbox_in_a_project_instance(self, project_id: str):
        print('project: ', project_id)
        checkbox = self.projects_table.get_project_checkbox_label_by_project_id(project_id)
        checkbox.click()

    def click_on_id_in_project_instance(self, project_index: str):
        """Clicks on the project id."""
        project_id_element = self.projects_table.get_all_project_ids()[int(project_index)]
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

    def get_all_projects_details_in_project_page(self) -> List[dict]:
        """Gets the details of all the instances"""
        all_projects = self.get_all_table_rows_page()
        all_projects_details = []
        for project in all_projects:
            project_details = {
                "checkbox": project["project_checkbox"].is_selected(),
                "id": project["id"].text,
                "title": project["project_title"].text,
                "current_step": project["project_current_step"].text,
                "owner": project["project_owner"].text,
                "creator": project["project_creator"].text,
                "date_created": project["project_date_created"].text,
                "closure_date": project["project_closure_date"].text
            }
            all_projects_details.append(project_details)
        return all_projects_details
    
    def get_all_projects_ids_text_in_project_page(self) -> List[str]:
        """Gets all the Ids from the projects in text format"""
        project_ids_elements = self.projects_table.get_all_project_ids()
        project_ids = []
        for project_id in project_ids_elements:
            project_ids.append(project_id.text)
        return project_ids

    def get_project_name_text_in_project_page(self) -> str:
        """Returns the text of the project name"""
        text = self.get_project_name().text
        return text

    def delete_project_instance_process_in_project_page(self, project_id: str):
        """Deletes a project instance"""
        self.open_delete_dialog_in_project_instance(project_id)
        self.click_dialog_delete_button_in_project_instance()

    def cancel_delete_project_instance_process_in_project_page(self, project_id: str):
        """Cancel delete a project instance process"""
        self.open_delete_dialog_in_project_instance(project_id)
        self.click_dialog_cancel_button_in_project_instance()

    def close_delete_project_instance_process_in_project_page(self, project_id: str):
        """Closes delete a project instance process"""
        self.open_delete_dialog_in_project_instance(project_id)
        self.click_dialog_close_button_in_a_project_instance()

    def open_delete_dialog_in_project_instance(self, project_id: str):
        """Opens the delete dialog in a delete a project instance process"""
        self.click_action_button_in_project_instance(project_id)
        self.click_action_delete_button_project_instance(project_id)

    def obtain_title_in_delete_in_project_instance(self) -> str:
        """Obtains the title of the delete instance dialog"""
        title = self.delete_dialog.get_dialog_title_text()
        return title

    def obtain_question_in_delete_in_project_instance(self) -> str:
        """Obtains the question of the delete instance dialog"""
        question = self.delete_dialog.get_dialog_question_text()
        return question

    def obtain_dialog_cancel_button_text_in_project_instance(self) -> str:
        """obtains the text from the cancel button of the delete instance dialog"""
        text = self.delete_dialog.get_cancel_dialog_button().text
        return text

    def obtain_dialog_delete_button_text_in_project_instance(self) -> str:
        """Obtains the text from the delete button of the delete instance dialog"""
        text = self.delete_dialog.get_delete_dialog_button().text
        return text

    def obtain_popup_message_in_project_page(self) -> WebElement:
        """Obtains the popup message in project page"""
        popup_message = self.popup.get_popup_message()
        return popup_message

    def obtain_popup_message_text_in_project_page(self) -> str:
        """Obtains the text in the popup message in the project page"""
        message = self.popup.get_popup_message_text()
        return message

    def obtain_popup_message_color_in_project_page(self) -> str:
        """Obtains the color of the popup message in project page"""
        color = self.popup.get_popup_message_color()
        return color
