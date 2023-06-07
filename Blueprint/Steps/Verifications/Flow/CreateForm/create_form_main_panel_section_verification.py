from Blueprint.Steps.Actions.Flows.create_form_main_panel_actions import FormMainPanelActions
from Blueprint.Steps.Actions.Flows.create_form_properties_panel_actions import PropertiesPanelActions
from Libraries.Assertions.assertions import Verification
from Blueprint.PageObject.Flows.Elements.FormElements.form_elements_storage import FormElementsStorage


class CreateFormMainPanelSectionsVerifications:
    """This class represents the verifications of Main Panel in form tab"""
    def __init__(self):
        self.main_panel = FormMainPanelActions()
        self.verification = Verification()
        self.elements_storage = FormElementsStorage()

    def default_section_should_be_displayed(self, expected_section: str):
        """Verifies that the default section is displayed in create form tab"""
        actual_sections = self.main_panel.get_all_sections_title_in_form_main_panel()
        self.verification.verify_a_list_contains(actual_sections, expected_section)

    def section_order_should_be(self, expected_section_order: list):
        """Verifies that the sections order is the expected"""
        actual_section_order = self.main_panel.get_all_sections_title_in_form_main_panel()
        self.verification.verify_equal_ignore(actual_section_order, expected_section_order)

    def section_dots_button_should_be_displayed(self, section_name: str):
        """Verifies that the sections dots button is displayed"""
        self.verification.verify_element_is_displayed(self.main_panel.get_section_dropdown(section_name))

    def selected_section_properties_should_be_displayed(self, expected_result: str):
        """Verifies that the section properties are displayed"""
        actual_result = PropertiesPanelActions().get_panel_title_in_form_properties()
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def section_delete_option_should_be_displayed(self, expected_option: str):
        """Verifies that the sections delete button is displayed"""
        actual_option = self.main_panel.get_section_delete_button().text
        self.verification.verify_equal_ignore(actual_option, expected_option)

    def component_should_not_be_displayed(self, component_id: str):
        """Verifies that a component is not displayed"""
        actual_section_components = self.elements_storage.components_in_sections
        self.verification.verify_a_dictionary_does_not_contain(actual_section_components, component_id)
