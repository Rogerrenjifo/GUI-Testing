from Blueprint.Steps.Actions.Flows.flow_main_panel_actions import FlowMainPanelActions
from Libraries.Assertions.assertions import Verification


class CreateFlowMainPanelVerifications:
    """This class represents the verifications of main panel in flow tab"""
    def __init__(self):
        self.main_panel = FlowMainPanelActions()
        self.verification = Verification()
    
    def component_rgb_color_should_be_equal(self, actual_color: str, expected_color: str):
        """Verifies that the component is displayed in the expected rgb color code"""
        self.verification.verify_equal_ignore(actual_color, expected_color)

    def component_should_not_have_a_button_dropdown(self, actual_found_result: bool, expected_found_result: bool = True):
        """Verifies that a component does not have a dropdown button"""
        self.verification.verify_equal_ignore(actual_found_result, expected_found_result)

    def component_should_have_a_single_dot(self, actual_list: list, expected_lenght_list: int = 1):
        """Verifies that a component have a single dot"""
        actual_lenght_list = len(actual_list)
        self.verification.verify_equal_ignore(actual_lenght_list, expected_lenght_list)

    def component_dot_should_be_connected(self, component_id: str, dot_number: str, expected_status: bool = True):
        """Verifies that a component dot is connected"""
        dot_status = self.main_panel.obtain_component_dot_status_in_flow_main_panel(component_id, dot_number)
        self.verification.verify_equal_ignore(dot_status, expected_status)

    def component_should_have_a_button_dropdown(self, actual_found_result: bool, expected_found_result: bool = False):
        """Verifies that a component have a dropdown button"""
        self.verification.verify_equal_ignore(actual_found_result, expected_found_result)
    
    def message_pop_up_should_be_equal(self, actual_message: str, expected_message: str):
        """Verifies that message pop up is displayed as expected"""
        self.verification.verify_equal_ignore(actual_message, expected_message)

    def dropdown_options_should_be_displayed(self, actual_options: list, expected_options: list = ['Clone', 'Delete']):
        """Verifies that the dropdown button displays clone and delete options"""
        self.verification.verify_equal_ignore(actual_options, expected_options)

    def dictionary_should_not_contain_component(self, dictionary: dict, component_id: str):
        """Verifies that the dictionary does not contain a component"""
        self.verification.verify_a_dictionary_does_not_contain(dictionary, component_id)

    def dictionary_should_contain_component(self, dictionary: dict, component_id: str):
        """Verifies that the dictionary contains a component"""
        self.verification.verify_a_dictionary_contains_key(dictionary, component_id)

    def component_should_have_different_positions(self, actual_position: str, expected_position: str):
        """Verifies that a component has a different position after moving it"""
        self.verification.verify_is_not_equal(actual_position, expected_position)
