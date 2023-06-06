from Blueprint.Steps.Actions.Flows.flow_page_actions import NewFlowActions
from Blueprint.Steps.Actions.MainMenu.main_menu_actions import MainMenuActions
from Libraries.Assertions.assertions import Verification


class MainMenuVerifications:
    """This class represents the verifications of the Main Menu"""
    def __init__(self):
        self.main_menu = MainMenuActions()
        self.create_flow = NewFlowActions()
        self.verification = Verification()

    def flows_label_should_be(self, expected_result: str):
        """Verifies that the label of the flows button in the main menu matches the expected result."""
        actual_result = self.main_menu.get_flows_button_label()
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def result_should_be_displayed(self):
        """Verifies that the flow result is displayed."""
        self.verification.verify_element_is_displayed(self.main_menu.get_flow_result("1"))

    def message_not_data_match_found_should_be_displayed(self, expected_result: str):
        """Verifies that the message for no data match found matches the expected result."""
        actual_result = self.main_menu.get_no_data_match_found_message_text()
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def create_flow_dialog_should_be_displayed(self):
        """Verifies that the create flow dialog is displayed."""
        self.verification.verify_element_is_displayed(self.main_menu.get_create_flow_dialog())

    def new_flow_button_should_be_displayed(self):
        """Verifies that the create flow dialog is displayed."""
        self.verification.verify_element_is_displayed(self.main_menu.get_new_flow_button())
