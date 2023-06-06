from Blueprint.Steps.Actions.Flows.create_form_main_panel_actions import FormMainPanelActions
from Blueprint.Steps.Actions.Flows.create_form_properties_panel_actions import PropertiesPanelActions
from Blueprint.PageObject.Flows.Elements.FormElements.form_elements_storage import FormElementsStorage
from Libraries.Assertions.assertions import Verification


class CreateFormAddComponentVerifications:
    """This class represents the verifications of add a section in form tab"""
    def __init__(self):
        self.main_panel = FormMainPanelActions()
        self.properties_panel = PropertiesPanelActions()
        self.verification = Verification()
        self.elements_storage = FormElementsStorage()

    def components_order_should_be(self, expected_result: list, section: str = "section-1"):
        """Verifies that the component order in a section is the expected"""
        actual_result = self.main_panel.get_all_components_title_in_a_section_in_form_main_panel(
            section)
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def new_component_should_not_be_displayed_in_main_panel(self, component_title):
        """Verifies that a new component is not displayed in the main menu or the section"""
        section_actual_list = self.main_panel.get_all_sections_title_in_form_main_panel()
        self.verification.verify_a_list_does_not_contain(section_actual_list, component_title)

    def new_component_should_not_be_displayed_in_default_section(self, component_title):
        """Verifies that a new component is displayed in the default section"""
        component_actual_list = self.main_panel.get_all_components_title_in_a_section_in_form_main_panel()
        self.verification.verify_a_list_does_not_contain(component_actual_list, component_title)

    def new_component_should_be_displayed_in_default_section(self):
        """Verifies that a new component is displayed in the default section"""
        component_actual_list = self.main_panel.get_all_components_title_in_a_section_in_form_main_panel()
        component_expected_list = self.elements_storage.get_components_title()
        self.verification.verify_equal_ignore(component_actual_list, component_expected_list)

    def new_component_should_be_displayed_in_new_section(self, section: str, expected_component: str):
        """Verifies that a new component is displayed in the default section"""
        component_actual_list = self.main_panel.get_all_components_title_in_a_section_in_form_main_panel(section)
        self.verification.verify_a_list_contains(component_actual_list, expected_component)

    def the_components_order_should_be(self, component_expected_list: list, section: str):
        component_actual_list = self.main_panel.get_all_components_title_in_a_section_in_form_main_panel(section)
        self.verification.verify_equal_ignore(component_actual_list, component_expected_list)

    def component_properties_should_be_displayed(self, expected_result: str):
        """Verifies that the new section properties are displayed"""
        actual_result = self.properties_panel.get_panel_title_in_form_properties()
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def component_should_be_displayed_in_expected_color(self, expected_color: str, component_id: str):
        """Verifies that the new section is displayed in the expected color"""
        section = component_id.split('_')[0]
        actual_color = self.elements_storage.components_in_sections[section][component_id].obtain_component_rgb_color()
        self.verification.verify_equal_ignore(actual_color, expected_color)
