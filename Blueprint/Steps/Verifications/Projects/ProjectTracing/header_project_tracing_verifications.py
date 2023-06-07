from Blueprint.Steps.Actions.Projects.ProjectTracing.Header.project_tracing_header_actions import \
    ProjectTracingHeaderActions
from Libraries.Assertions.assertions import Verification
from selenium.webdriver.remote.webelement import WebElement


class HeaderProjectTracingVerifications:
    """This class represents the verifications of header on the project tracing page"""

    def __init__(self):
        self.header = ProjectTracingHeaderActions()
        self.verification = Verification()

    def project_tag_text_should_be_displayed(self, expected_tag_text: str):
        """Verifies that the text of the Project tag is displayed"""
        actual_tag_text = self.header.get_project_tag_text_in_project_tracing()
        self.verification.verify_equal_ignore(actual_tag_text, expected_tag_text)

    def project_name_text_should_be_displayed(self, expected_project_name_text: str):
        """Verifies that the text of the Project name is displayed"""
        actual_project_name_text = self.header.get_project_title_text_in_project_tracing()
        self.verification.verify_equal_ignore(actual_project_name_text, expected_project_name_text)

    def delete_button_should_be_displayed(self):
        """Verifies that delete button is displayed"""
        delete_button = self.header.get_delete_button()
        self.verification.element_should_be_displayed(delete_button)

    def the_background_of_the_delete_button_should_be_turquoise(self, expected_color: str):
        """Verifies the RGB background color of the delete button is rgb(0, 217, 194, 1)"""
        actual_color = self.header.get_the_rgb_background_delete_button()
        self.verification.verify_equal_ignore(actual_color, expected_color)

    def the_background_of_the_action_button_should_be_highlighted(self, button_text: str, expected_color: str):
        """Verifies the RGB background color of the delete button is rgb(5, 176, 158, 1)"""
        actual_color = self.header.get_the_rgb_background_action_button(button_text)
        self.verification.verify_equal_ignore(actual_color, expected_color)

    def popup_window_should_be_displayed(self, expected_result=False):
        """Verifies that the popup window delete process instance is displayed"""
        actual_result = self.header.get_popup_window_delete_process_instance_in_project_tracing()
        self.verification.verify_is_not_equal(actual_result, expected_result)

    def cancel_button_of_delete_process_instance_should_be_displayed(self,  expected_result=False):
        """Verifies cancel button is displayed on the popup window delete process instance"""
        actual_result = self.header.get_cancel_button_form_popup_window_delete_process_instance_in_project_tracing()
        self.verification.verify_is_not_equal(actual_result, expected_result)

    def delete_button_of_delete_process_instance_should_be_displayed(self,  expected_result=False):
        """Verifies delete button is displayed on the popup window delete process instance"""
        actual_result = self.header.get_delete_button_form_popup_window_delete_process_instance_in_project_tracing()
        self.verification.verify_is_not_equal(actual_result, expected_result)
