from Blueprint.Steps.Actions.Projects.ProjectTracing.flow_actions import ProjectFlowActions
from Libraries.Assertions.assertions import Verification


class FlowProjectTracingVerifications:
    """This class represents the verifications of system on the project tracing page"""
    def __init__(self):
        self.main_panel = ProjectFlowActions()
        self.verification = Verification()

    def flow_title_should_be_displayed(self, expected_title):
        """Verifies that the title Flow is displayed"""
        actual_title = self.main_panel.get_project_flow_title()
        self.verification.verify_equal_ignore(actual_title, expected_title)

    def start_text_component_should_be_displayed(self, expected_title):
        """Verifies that the text of the start component is displayed"""
        actual_title = self.main_panel.get_start_text_in_project_flow()
        self.verification.verify_equal_ignore(actual_title, expected_title)

    def last_text_component_should_be_displayed(self, expected_title):
        """Verifies that the text of the last component is displayed"""
        actual_title = self.main_panel.get_final_step_text_in_project_flow()
        self.verification.verify_equal_ignore(actual_title, expected_title)

    def start_component_should_be_displayed(self):
        """Verifies that start component is displayed"""
        actual_result = self.main_panel.get_start_component_in_flow()
        self.verification.element_should_be_displayed(actual_result)

    def last_component_should_be_displayed(self):
        """Verifies that the last component is displayed"""
        actual_result = self.main_panel.get_last_component_in_flow()
        self.verification.element_should_be_displayed(actual_result)

    def step_text_component_should_be_displayed(self, number: int, expected_result):
        """Verifies that the text of the step component by order is displayed"""
        actual_result = self.main_panel.get_flow_step_text_by_order_in_project_flow(number)
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def action_text_component_should_be_displayed(self, number: int, expected_result):
        """Verifies that the text of the action component by order is displayed"""
        actual_result = self.main_panel.get_flow_step(number)
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def border_element_should_be_highlighted(self, number: int, expected_color):
        """Verifies the RGB border color of an action is highlighted"""
        actual_color = self.main_panel.get_the_rgb_border_popup_in_project_flow(number)
        self.verification.verify_equal_ignore(actual_color, expected_color)
        
    def data_text_from_popup_action(self, number: int, expected_result = False):
        """Verifies that start component is displayed"""
        actual_result = self.main_panel.get_data_popup_in_project_flow(number)
        self.verification.verify_is_not_equal(actual_result, expected_result)

    def actions_components_are_displayed_by_order(self, number: int):
        """Verifies that the components are displayed by order"""
        actual_result = self.main_panel.get_flow_action(number)
        self.verification.element_should_be_displayed(actual_result)

    def steps_components_are_displayed_by_order(self, number: int):
        """Verifies that the components are displayed by order"""
        actual_result = self.main_panel.get_flow_step(number)
        self.verification.element_should_be_displayed(actual_result)
