from Blueprint.Steps.Actions.Flows.create_form_properties_panel_actions import PropertiesPanelActions
from Libraries.Assertions.assertions import Verification
from Blueprint.PageObject.Flows.Elements.FormElements.form_elements_storage import FormElementsStorage


class CreateFormPropertiesPanelVerifications:
    """This class represents the verifications of Main Panel in form tab"""
    def __init__(self):
        self.properties_panel = PropertiesPanelActions()
        self.verification = Verification()
        self.elements_storage = FormElementsStorage()

    def textbox_should_has_its_appropriate_fields(self, name: str, placeholder: str, default_value: str):
        """Sets the name, placeholder, and default value for a textbox in the form properties panel."""
        self.properties_panel.set_name_in_form_properties_panel(name)
        self.properties_panel.set_placeholder_in_form_properties_panel(placeholder)
        self.properties_panel.set_default_value_in_form_properties_panel(default_value)

    def numeric_box_should_has_its_appropriate_fields(self, name: str, placeholder: str, number_format: str,
                                                      default_value: str):
        """Sets the name, placeholder, number format, and default value for numeric box in the form properties panel."""
        self.properties_panel.set_name_in_form_properties_panel(name)
        self.properties_panel.set_placeholder_in_form_properties_panel(placeholder)
        self.properties_panel.select_number_format_in_form_properties_panel(number_format.lower())
        self.properties_panel.set_default_value_in_form_properties_panel(default_value)
        self.properties_panel.click_required_field_label_in_form_properties_panel()

    def default_value_formatted_should_be_the_according_to_format_in_numeric_box(self, number_format: str,
                                                                                 default_value: str,
                                                                                 expected_result: str):
        """Verifies that the default value in a numeric box is formatted correctly according to the specified format."""
        self.properties_panel.select_number_format_in_form_properties_panel(number_format.lower())
        self.properties_panel.set_default_value_in_form_properties_panel(default_value)
        default_value_formatted = self.properties_panel.get_number_default_value_formatted_in_form_properties_panel()
        self.verification.verify_equal_ignore(default_value_formatted, expected_result)

    def multiline_box_should_has_its_appropriate_fields(self, name: str, placeholder: str):
        """ Sets the name, placeholder, and required field label for a multiline box in the form properties panel."""
        self.properties_panel.set_name_in_form_properties_panel(name)
        self.properties_panel.set_placeholder_in_form_properties_panel(placeholder)
        self.properties_panel.click_required_field_label_in_form_properties_panel()

    def dropdown_box_should_has_its_appropriate_fields(self, name: str, placeholder: str, default_value: str,
                                                       component_id: str, values: list):
        """Sets the name, placeholder, default value, dropdown component ID, and dropdown values for a dropdown box
        in the form properties panel."""
        self.properties_panel.set_name_in_form_properties_panel(name)
        self.properties_panel.set_placeholder_in_form_properties_panel(placeholder)
        self.properties_panel.add_dropdown_values_process_in_form_properties(component_id, values)
        self.properties_panel.select_default_dropdown_value_in_form_properties_panel(default_value)
        self.properties_panel.click_required_field_label_in_form_properties_panel()
