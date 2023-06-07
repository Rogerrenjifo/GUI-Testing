from selenium.webdriver.common.by import By
from Libraries.Assertions.assertions import Verification
from Blueprint.Steps.Actions.Projects.ProjectPage.export_dialog_actions import ExportDialogActions
from Blueprint.Steps.Actions.Projects.ProjectPage.project_page_actions import ProjectPageActions
from Blueprint.Steps.Actions.Projects.new_project_actions import NewProjectActions
from Blueprint.Steps.Utils.generate_file_name import FileNameGenerator


class HeaderProjectPageVerifications:
    def __init__(self):
        self.assertions = Verification()
        self.export_dialog = ExportDialogActions()
        self.project_page = ProjectPageActions()
        self.verification = Verification()

    def export_file_name_should_follow_the_format(self, actual_result: str, project_name: str):
        """Verifies the default file name has the expected format"""
        expected_result = FileNameGenerator().generate_file_name(project_name)
        self.assertions.verify_equal_ignore(actual_result, expected_result)

    def project_name_should_be_displayed(self):
        """Verifies the project name is displayed"""
        project_name = self.project_page.get_project_name()
        self.assertions.verify_element_is_displayed(project_name)

    def export_dialog_should_be_displayed(self):
        """Verifies the export dialog is displayed"""
        dialog = self.export_dialog.get_export_dialog()
        self.assertions.verify_element_is_displayed(dialog)

    def export_dialog_should_not_be_displayed(self):
        """Verifies the export dialog is not displayed"""
        dialog_container = self.export_dialog.get_export_dialog_father_container()
        dialog = dialog_container.find_elements(By.XPATH, ".//*")
        self.assertions.verify_a_list_is_empty(dialog)

    def popup_message_should_be_displayed(self):
        """Verifies the popup message is displayed"""
        popup = self.project_page.obtain_popup_message_in_project_page()
        self.assertions.verify_element_is_displayed(popup)

    def current_page_should_be_new_project(self):
        """Verifies the actual page is new project"""
        tag_new = NewProjectActions().get_tag_new()
        self.assertions.verify_element_is_displayed(tag_new)

    def project_title_should_be(self, expected_result: str):
        """Verifies that project title is the expected"""
        actual_result = self.project_page.get_project_name_text_in_project_page()
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def project_name_should_be_as_expected(self, expected_name):
        """Verifies the project name is displayed as expected"""
        project_name = self.project_page.get_project_name().text
        self.assertions.verify_equal_ignore(project_name, expected_name)
