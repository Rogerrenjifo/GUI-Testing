import time
from typing import List
from assertpy import soft_assertions
from Libraries.Assertions.assertions import Verification
from Blueprint.Steps.Actions.Projects.ProjectPage.project_page_actions import ProjectPageActions
from Blueprint.Steps.Actions.Projects.ProjectTracing.Header.project_tracing_header_actions import ProjectTracingHeaderActions


class TableProjectPageVerifications:
    def __init__(self):
        self.assertions = Verification()
        self.project_page = ProjectPageActions()
        self.project_tracing = ProjectTracingHeaderActions()

    def checkbox_should_be_checked(self, project_id: str):
        """Verifies the checkbox value is checked"""
        with soft_assertions():
            project = self.project_page.get_project_details_in_project_page(project_id)
            checkbox = project["checkbox"]
            self.assertions.verify_equal_ignore(checkbox, True)

    def checkbox_should_not_be_checked(self, project_id: str):
        """Verifies the checkbox value is unchecked"""
        with soft_assertions():
            project = self.project_page.get_project_details_in_project_page(project_id)
            checkbox = project["checkbox"]
            self.assertions.verify_equal_ignore(checkbox, False)

    def actions_menu_should_be_displayed(self, project_id: str):
        """Verifies the actions menu is displayed"""
        with soft_assertions():
            project = self.project_page.get_table_row(project_id)
            actions_menu = project["project_actions_delete"]
            self.assertions.verify_element_is_displayed(actions_menu)

    def delete_dialog_should_be_displayed(self):
        """Verifies the delete dialog is displayed"""
        with soft_assertions():
            dialog = self.project_page.delete_dialog.get_dialog_title()
            self.assertions.verify_element_is_displayed(dialog)

    def all_ids_should_have_same_base_code(self, ids_list: List[str]):
        """Verifies all the elements have the same base code"""
        with soft_assertions():
            base_code = ids_list[0].split("-")[0]
            for project_id in ids_list:
                self.assertions.verify_equal_ignore(project_id.split("-")[0], base_code)

    def current_url_should_be_project_tracing_page(self, flow_name: str, project_id: str):
        """Verifies the current page is the tracing page of the project"""
        with soft_assertions():
            project_name = self.project_tracing.get_project_title_text_in_project_tracing()
            time.sleep(2)
            id_tag = self.project_tracing.get_project_tag_text_in_project_tracing()
            self.assertions.verify_equal_ignore(project_name, flow_name)
            self.assertions.verify_equal_ignore(id_tag, project_id)

    def project_should_have_value(self, value: str, project_id: str):
        """Verifies the project instance has the specified value"""
        with soft_assertions():
            value_content = self.project_page.get_project_details_in_project_page(project_id)[value]
            self.assertions.verify_is_not_equal(value_content, "")
            self.assertions.verify_is_not_equal(value_content, None)

    def all_projects_should_have_id(self, ids: str):
        """Verifies all the projects have an Id"""
        with soft_assertions():
            for project_id in ids:
                self.assertions.verify_is_not_equal(project_id, "")
                self.assertions.verify_is_not_equal(project_id, None)

    def all_projects_should_have_title(self, ids: list):
        """Verifies all the projects have a title"""
        with soft_assertions():
            for project_id in ids:
                self.project_should_have_value("title", project_id)

    def all_projects_should_have_current_step(self, ids: list):
        """Verifies all the projects have a current_step"""
        with soft_assertions():
            for project_id in ids:
                self.project_should_have_value("current_step", project_id)

    def all_projects_should_have_owner(self, ids: list):
        """Verifies all the projects have a owner"""
        with soft_assertions():
            for project_id in ids:
                self.project_should_have_value("owner", project_id)

    def all_projects_should_have_creator(self, ids: list):
        """Verifies all the projects have a creator"""
        with soft_assertions():
            for project_id in ids:
                self.project_should_have_value("creator", project_id)

    def all_projects_should_have_date_created(self, ids: list):
        """Verifies all the projects have a date_created"""
        with soft_assertions():
            for project_id in ids:
                self.project_should_have_value("date_created", project_id)
