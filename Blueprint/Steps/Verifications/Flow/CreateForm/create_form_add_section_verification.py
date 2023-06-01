from Blueprint.Steps.Actions.Flows.create_form_main_panel_actions import FormMainPanelActions
from Blueprint.Steps.Actions.Flows.create_form_properties_panel_actions import PropertiesPanelActions
from Libraries.Assertions.assertions import Verification
from robot.api import logger
from Blueprint.PageObject.Flows.Elements.FormElements.form_elements_storage import FormElementsStorage


class CreateFormAddSectionVerifications:
    """This class represents the verifications of add a section in form tab"""
    def __init__(self):
        super().__init__()
        self.main_panel = FormMainPanelActions()
        self.properties_panel = PropertiesPanelActions()
        self.verification = Verification()
        self.elements_storage = FormElementsStorage()

    def new_section_should_be_displayed(self):
        """Verifies that a new section is displayed"""
        section_actual_list = self.main_panel.get_all_sections_title_in_form_main_panel()
        section_expected_list = self.elements_storage.get_sections_title()
        self.verification.verify_equal_ignore(section_actual_list, section_expected_list)

    def new_section_should_be_displayed_above_selected(self, selected_section: str):
        """Verifies that a new section is displayed above another"""
        logger.info(f"New section should be before section {selected_section}")
        self.new_section_should_be_displayed()

    def new_section_should_be_displayed_below_selected(self, selected_section):
        """Verifies that a new section is displayed bellow another"""
        logger.info(f"New section should be after section {selected_section}")
        self.new_section_should_be_displayed()

    def new_section_should_be_empty(self, section_title: str):
        """Verifies that the new section added is empty"""
        section_actual_list = self.main_panel.get_all_components_title_in_a_section_in_form_main_panel(section_title)
        self.verification.verify_a_list_is_empty(section_actual_list)

    def new_section_properties_should_be_displayed(self, expected_result: str):
        """Verifies that the new section properties are displayed"""
        actual_result = self.properties_panel.get_panel_title_in_form_properties()
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def new_section_should_not_be_displayed(self, new_section_title: str):
        """Verifies that the new section is not added in main panel"""
        section_actual_list = self.main_panel.get_all_sections_title_in_form_main_panel()
        self.verification.verify_a_list_does_not_contain(section_actual_list, new_section_title)

    def pop_up_error_message_should_be_displayed(self, expected_message: str):
        """Verifies that a pop up message is displayed in the main panel"""
        actual_message = self.main_panel.obtain_text_of_form_main_panel_pop_up_message()
        self.verification.verify_equal_ignore(actual_message, expected_message)

    def error_message_should_be_displayed(self, section_title: str, expected_message: str):
        """Verifies that an error message is displayed in the new section"""
        actual_message = self.main_panel.obtain_section_error_message_in_form_main_panel(section_title)
        self.verification.verify_equal_ignore(actual_message, expected_message)

    def section_should_be_displayed_in_expected_color(self, expected_color: str, section_index: str):
        """Verifies that the new section is displayed in the expected color"""
        actual_color = self.main_panel.obtain_section_rgb_color_in_form_main_panel(section_index)
        self.verification.verify_equal_ignore(actual_color, expected_color)

    def pop_up_message_should_be_displayed_in_expected_color(self, expected_color: str):
        """Verifies that the pop up message is displayed in the expected color"""
        actual_color = self.main_panel.obtain_rgb_color_of_form_main_panel_pop_up_message()
        self.verification.verify_equal_ignore(actual_color, expected_color)

    def error_message_should_be_displayed_in_expected_color(self, expected_color: str, section_title: str):
        """Verifies that the error message is displayed in the expected color"""
        actual_color = self.main_panel.obtain_section_error_message_rgb_color_in_form_main_panel(section_title)
        self.verification.verify_equal_ignore(actual_color, expected_color)
