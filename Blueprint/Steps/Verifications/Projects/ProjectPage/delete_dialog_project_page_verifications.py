import time
from Libraries.Assertions.assertions import Verification
from Blueprint.Steps.Actions.Projects.ProjectPage.project_page_actions import ProjectPageActions


class DeleteDialogProjectPageVerifications:
    def __init__(self):
        self.assertions = Verification()
        self.project_page = ProjectPageActions()

    def delete_dialog_title_should_be(self, expected_title: str):
        actual_title = self.project_page.obtain_title_in_delete_dialog_in_project_instance()
        self.assertions.verify_equal_ignore(actual_title, expected_title)

    def project_instance_should_still_exist(self, project_id: str):
        project_id_list = self.project_page.get_all_projects_ids_text_in_project_page()
        self.assertions.verify_a_list_contains(project_id_list, project_id)

    def project_instance_should_not_exist(self, project_id: str):
        time.sleep(2)
        project_id_list = self.project_page.get_all_projects_ids_text_in_project_page()
        self.assertions.verify_a_list_does_not_contain(project_id_list, project_id)

    def popup_message_should_be_displayed(self):
        popup = self.project_page.obtain_popup_message_in_project_page()
        self.assertions.element_should_be_displayed(popup)
