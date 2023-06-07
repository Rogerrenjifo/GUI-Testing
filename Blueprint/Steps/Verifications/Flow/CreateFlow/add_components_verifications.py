from Blueprint.Steps.Actions.Flows.flow_main_panel_actions import FlowMainPanelActions
from Blueprint.Steps.Actions.Flows.flow_components_actions import FlowComponentsActions
from Libraries.Assertions.assertions import Verification


class AddComponentsVerification:
    """This class contains the method to verify the actions of flow main panel."""

    def __init__(self) -> None:
        self.verification = Verification()
        self.main_panel = FlowMainPanelActions()
        self.component = FlowComponentsActions()

    def the_component_should_be_added_to_the_main_board(self, step_id: str) -> None:
        """Verifies the component were added to canvas board."""
        elements_ids = self.main_panel.generate_components_ids()
        self.verification.verify_a_list_contains(elements_ids, step_id)

    def the_component_should_not_be_added_to_the_main_board(self, step_id: str) -> None:
        """Verifies the component were added to canvas board."""
        elements_ids = self.main_panel.generate_components_ids()
        self.verification.verify_a_list_does_not_contain(elements_ids, step_id)

    def the_component_properties_should_be_displayed(self, title: str):
        """Verifies that the component properties is displayed."""
        element = self.component.get_properties_panel_title_element()
        self.verification.verify_equal_ignore(element.text, title)

    def component_should_have_different_title(self, id_1: str, id_2: str):
        """Verifies that the component has different titles"""
        title_1 = self.main_panel.obtain_component_title_in_flow_main_panel(id_1)
        title_2 = self.main_panel.obtain_component_title_in_flow_main_panel(id_2)
        self.verification.verify_is_not_equal(title_1, title_2)

    def component_title_should_be(self, component_id, expected_title):
        """Verifies the title is equal as expected"""
        actual_title = self.main_panel.obtain_component_title_in_flow_main_panel(component_id)
        self.verification.verify_equal_ignore(actual_title, expected_title)
