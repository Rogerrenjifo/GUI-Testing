import time

from selenium.webdriver.remote.webelement import WebElement
from Libraries.Assertions.assertions import Verification
from Blueprint.Steps.Actions.Projects.ProjectPage.export_dialog_actions import ExportDialogActions
from Blueprint.Steps.Actions.Projects.ProjectPage.project_page_actions import ProjectPageActions
from datetime import datetime


class HeaderProjectPageVerifications:
    def __init__(self):
        self.assertions = Verification()
        self.export_dialog = ExportDialogActions()
        self.project_page = ProjectPageActions()

    @staticmethod
    def actual_date() -> str:
        """Generates the actual date in the following format: d_m_YYYY"""
        today = datetime.today().strftime('%d_%m_%Y')
        today_list = today.split("_")
        if today_list[1][0] == "0":
            today_list[1] = today_list[1][1:2]
        today = "_".join(today_list)
        return today

    def generate_file_name(self, project_name: str) -> str:
        """Generates the filename in the following format: export_project_name_d_m_YYYY"""
        date = self.actual_date()
        project_name = project_name.replace(" ", "_")
        file_name = f"export_{project_name}_{date}"
        return file_name

    def export_file_name_should_follow_the_format(self, actual_result: str, project_name: str):
        expected_result = self.generate_file_name(project_name)
        self.assertions.verify_equal_ignore(actual_result, expected_result)

    def project_name_should_be_displayed(self):
        project_name = self.project_page.get_project_name()
        self.assertions.element_should_be_displayed(project_name)

    def export_dialog_should_be_displayed(self):
        dialog = self.export_dialog.get_export_dialog()
        self.assertions.element_should_be_displayed(dialog)

    def popup_message_should_be_displayed(self):
        popup = self.project_page.obtain_popup_message_in_project_page()
        self.assertions.element_should_be_displayed(popup)

    def current_url_should_be(self, expected_url: str):
        time.sleep(3)
        actual_url = self.project_page.driver.current_url
        self.assertions.verify_equal_ignore(actual_url, expected_url)
