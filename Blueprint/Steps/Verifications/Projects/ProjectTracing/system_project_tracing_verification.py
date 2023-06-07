from Blueprint.Steps.Actions.Projects.ProjectTracing.system_actions import ProjectSystemActions
from Libraries.Assertions.assertions import Verification


class SystemProjectTracingVerifications:
    """This class represents the verifications of system on the project tracing page"""

    def __init__(self):
        self.main_panel = ProjectSystemActions()
        self.verification = Verification()

    def system_title_should_be_displayed(self, actual_title, expected_title):
        """Verifies that the title System is displayed"""
        self.verification.verify_equal_ignore(actual_title, expected_title)

    def current_step_title_should_be_displayed(self, actual_title, expected_title):
        """Verifies the title Current step is displayed"""
        self.verification.verify_equal_ignore(actual_title, expected_title)

    def button_should_be_visible(self, actual_result, expected_result=False):
        """Verifies save button is displayed"""
        self.verification.verify_is_not_equal(actual_result, expected_result)

    def dropdown_list_should_not_be_empty(self, actual_list):
        """Verifies dropdown list is not empty"""
        self.verification.verify_a_list_is_not_empty(actual_list)

    def border_element_should_be_equal(self, actual_color, expected_color):
        """Verifies the border element is highlighted"""
        self.verification.verify_equal_ignore(actual_color, expected_color)

    def creation_date_title_should_be_displayed(self, actual_title, expected_title):
        """Verifies the title Create date is displayed"""
        self.verification.verify_equal_ignore(actual_title, expected_title)

    def last_update_title_should_be_displayed(self, actual_title, expected_title):
        """Verifies the title Last update is displayed"""
        self.verification.verify_equal_ignore(actual_title, expected_title)

    def closure_date_title_should_be_displayed(self, actual_title, expected_title):
        """Verifies the title Closure Date is displayed"""
        self.verification.verify_equal_ignore(actual_title, expected_title)

    def data_text_should_be_displayed(self, actual_data, expected_result=False ):
        """Verifies data text is displayed"""
        self.verification.verify_is_not_equal(actual_data, expected_result)

    def field_required_should_be_displayed(self, actual_result, expected_result=False ):
        """Verifies field required is displayed"""
        self.verification.verify_is_not_equal(actual_result, expected_result)

    def dropdown_list_should_not_be_displayed(self, actual_status, expected_status=False):
        """Verifies dropdown list in not displayed"""
        self.verification.verify_is_not_equal(actual_status, expected_status)
