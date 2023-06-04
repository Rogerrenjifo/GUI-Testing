from Blueprint.Steps.Actions.Flows.flow_page_actions import NewFlowActions
from Libraries.Assertions.assertions import Verification


class CreateFlowVerifications:
    """This class represents the verifications of the Main Menu"""
    def __init__(self):
        self.create_flow = NewFlowActions()
        self.verification = Verification()

    def name_label_should_be_displayed(self, expected_result: str):
        """Verifies that the name label is displayed correctly."""
        actual_result = self.create_flow.get_label_name()
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def code_label_should_be_displayed(self, expected_result: str):
        """Verifies that the code label is displayed correctly."""
        actual_result = self.create_flow.get_label_code()
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def name_field_required_message_should_be_displayed(self):
        """Verifies that the required message for the name field is displayed."""
        self.verification.verify_element_is_displayed(self.create_flow.get_name_field_required_message())

    def code_field_required_message_should_be_displayed(self):
        """Verifies that the required message for the code field is displayed."""
        self.verification.verify_element_is_displayed(self.create_flow.get_code_field_required_message())

    def create_flow_dialog_should_not_be_display(self):
        """Verifies that the create flow dialog is not displayed."""
        self.verification.verify_element_is_not_displayed(self.create_flow.get_header_create_new_flow())

    def process_created_pop_up_message_should_be_displayed(self):
        """Verifies that the pop-up message for a successfully created process is displayed."""
        self.verification.verify_element_is_displayed(self.create_flow.pop_up_messages.get_popup_message())

    def pop_up_message_a_flow_with_code_already_exists_should_be_displayed(self):
        """Verifies that the pop-up message for a flow with an existing code is displayed."""
        self.verification.verify_element_is_displayed(self.create_flow.pop_up_messages.get_popup_message())
