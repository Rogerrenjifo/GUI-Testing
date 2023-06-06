from Blueprint.Steps.Actions.Flows.create_form_main_panel_actions import FormMainPanelActions
from Blueprint.Steps.Actions.Flows.create_form_elements_actions import CreateFormElementsActions
from Libraries.Assertions.assertions import Verification
from Blueprint.PageObject.Flows.Elements.FormElements.form_elements_storage import FormElementsStorage


class CreateFormElementsVerifications:
    """This class represents the verifications of elements in form tab"""
    def __init__(self):
        self.main_panel = FormMainPanelActions()
        self.verification = Verification()
        self.elements_panel = CreateFormElementsActions()

    def input_text_should_be_displayed(self):
        """Verifies that text box input is displayed in create form tab"""
        self.verification.verify_element_is_displayed(self.elements_panel.get_input_text_element())

    def input_date_should_be_displayed(self):
        """Verifies that date input is displayed in create form tab"""
        self.verification.verify_element_is_displayed(self.elements_panel.get_input_date_element())

    def input_checkbox_should_be_displayed(self):
        """Verifies that checkbox input is displayed in create form tab"""
        self.verification.verify_element_is_displayed(self.elements_panel.get_input_checkbox_element())

    def input_multiline_should_be_displayed(self):
        """Verifies that multiline input is displayed in create form tab"""
        self.verification.verify_element_is_displayed(self.elements_panel.get_input_multiline_element())

    def input_numbers_should_be_displayed(self):
        """Verifies that numbers input is displayed in create form tab"""
        self.verification.verify_element_is_displayed(self.elements_panel.get_input_numbers_element())

    def input_user_list_should_be_displayed(self):
        """Verifies that user list input is displayed in create form tab"""
        self.verification.verify_element_is_displayed(self.elements_panel.get_input_user_list_element())

    def input_dropdown_should_be_displayed(self):
        """Verifies that dropdown input is displayed in create form tab"""
        self.verification.verify_element_is_displayed(self.elements_panel.get_input_dropdown_element())

    def input_section_should_be_displayed(self):
        """Verifies that section input is displayed in create form tab"""
        self.verification.verify_element_is_displayed(self.elements_panel.get_section_element())

    def components_title_should_be_displayed(self, expected_title: str):
        """Verifies that the components title is displayed in create form tab"""
        actual_title = self.elements_panel.get_components_title().text
        self.verification.verify_equal_ignore(expected_title, actual_title)

    def section_title_should_be_displayed(self, expected_title: str):
        """Verifies that the section title is displayed in create form tab"""
        actual_title = self.elements_panel.get_section_title().text
        self.verification.verify_equal_ignore(expected_title, actual_title)

    def default_section_should_be_displayed(self, expected_section_title: str):
        """Verifies that the default section is displayed in create form tab"""
        expected_section = self.main_panel.get_section(expected_section_title)
        self.verification.verify_element_is_displayed(expected_section)

    def default_component_should_be_displayed(self, expected_component_id: str):
        """Verifies that the default component is displayed in create form tab"""
        expected_component = self.main_panel.get_component(expected_component_id)
        self.verification.verify_element_is_displayed(expected_component)

    def default_component_title_should_be(self, expected_component_title: str, component_id: str):
        """Verifies that the component title is the expected"""
        actual_component_title = self.main_panel.obtain_component_title_in_form_main_panel(component_id)
        self.verification.verify_equal_ignore(actual_component_title, expected_component_title)

    def component_should_be_in_default_section(self, component_id: str):
        """Verifies that a component is displayed in default section"""
        actual_section_components = FormElementsStorage().components_in_sections["section-1"]
        self.verification.verify_a_dictionary_contains_key(actual_section_components, component_id)
