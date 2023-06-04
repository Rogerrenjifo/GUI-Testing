from Blueprint.Steps.Actions.Flows.create_form_main_panel_actions import FormMainPanelActions
from Blueprint.Steps.Actions.Flows.create_form_properties_panel_actions import PropertiesPanelActions
from Libraries.Assertions.assertions import Verification


class CreateFormMainPanelComponentsVerifications:
    """This class represents the verifications of Main Panel in form tab"""
    def __init__(self):
        self.main_panel = FormMainPanelActions()
        self.verification = Verification()

    def components_order_should_be(self, expected_result: list, section: str = "section-1"):
        """Verifies that the component order in a section is the expected"""
        actual_result = self.main_panel.get_all_components_title_in_a_section_in_form_main_panel(section)
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def component_dots_button_should_be_displayed(self, component_id: str):
        """Verifies that the component dots button is displayed"""
        self.verification.verify_element_is_displayed(self.main_panel.get_component_dropdown(component_id))

    def selected_component_properties_should_be_displayed(self, expected_result: str):
        """Verifies that the component properties are displayed"""
        actual_result = PropertiesPanelActions().get_panel_title_in_form_properties()
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def component_delete_option_should_be_displayed(self, expected_option: str, component_id):
        """Verifies that the component delete button is displayed"""
        actual_option = self.main_panel.get_component_delete_button(component_id).text
        self.verification.verify_equal_ignore(actual_option, expected_option)

    def component_should_not_be_displayed(self, component_title: str, section: str):
        """Verifies that a component is not displayed in a section"""
        actual_section_components = self.main_panel.get_all_components_title_in_a_section_in_form_main_panel(section)
        self.verification.verify_a_list_does_not_contain(actual_section_components, component_title)

    def component_should_be_displayed(self, component_title: str, section: str):
        """Verifies that a component is displayed in a section"""
        actual_section_components = self.main_panel.get_all_components_title_in_a_section_in_form_main_panel(section)
        self.verification.verify_a_list_contains(actual_section_components, component_title)
