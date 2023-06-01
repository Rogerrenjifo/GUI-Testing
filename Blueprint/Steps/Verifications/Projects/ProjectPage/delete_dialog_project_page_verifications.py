import time
from selenium.webdriver.common.by import By
from Libraries.Assertions.assertions import Verification
from Blueprint.Steps.Actions.Projects.ProjectPage.project_page_actions import ProjectPageActions


class DeleteDialogProjectPageVerifications:
    def __init__(self):
        self.assertions = Verification()
        self.project_page = ProjectPageActions()

    def delete_dialog_title_should_be(self, expected_title: str):
        """Verifies the content of the title of the delete dialog"""
        actual_title = self.project_page.obtain_title_in_delete_dialog_in_project_instance()
        self.assertions.verify_equal_ignore(actual_title, expected_title)

    def project_instance_should_still_exist(self, project_id: str):
        """Verifies the project instance exists in the list"""
        project_id_list = self.project_page.get_all_projects_ids_text_in_project_page()
        self.assertions.verify_a_list_contains(project_id_list, project_id)

    def project_instance_should_not_exist(self, project_id: str):
        """Verifies the project instance does not exist"""
        time.sleep(2)
        project_id_list = self.project_page.get_all_projects_ids_text_in_project_page()
        self.assertions.verify_a_list_does_not_contain(project_id_list, project_id)

    def popup_message_should_be_displayed(self):
        """Verifies the popup message is displayed"""
        popup = self.project_page.obtain_popup_message_in_project_page()
        self.assertions.element_should_be_displayed(popup)

    def delete_dialog_should_not_be_displayed(self):
        """Verifies the delete dialog is not displayed"""
        dialog_container = self.project_page.delete_dialog.get_father_dialog_container()
        dialog = dialog_container.find_elements(By.XPATH, ".//*")
        self.assertions.verify_a_list_is_empty(dialog)
