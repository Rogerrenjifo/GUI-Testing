from Blueprint.Steps.Actions.Flows.create_form_main_panel_actions import FormMainPanelActions
from Blueprint.Steps.Actions.Flows.flow_main_panel_actions import FlowMainPanelActions
from Blueprint.Steps.Actions.Flows.header_actions import HeaderActions
from Blueprint.Steps.Actions.Flows.flow_permissions_actions import FlowPermissionsActions
from Blueprint.Steps.Actions.Flows.process_permissions_actions import ProcessPermissionsActions
from Blueprint.Steps.Actions.Flows.section_visibility_permissions_actions import SectionsVisibilityActions
from Libraries.Assertions.assertions import Verification
from assertpy import soft_assertions
from robot.api import logger


class ScholarshipApplicationVerifications:
    """This class represents the verifications of scholarship application scenario"""
    def __init__(self):
        self.main_panel = FormMainPanelActions()
        self.assertions = Verification()
        self.flow_board = FlowMainPanelActions()

    def components_type_in_section_should_be(self, component_types: list, section_title: str = "section-1"):
        """Verifies that the components types in a section are the expected"""
        actual_types = self.main_panel.get_all_components_type_in_a_section_in_form_main_panel(section_title)
        self.assertions.verify_equal_ignore(actual_types, component_types)

    def flow_header_title_should_be_the_same_as_the_title_set_in_create_flow(self, expected_title: str):
        actual_title = HeaderActions().get_flow_name_text_in_flow_header()
        self.assertions.verify_equal_ignore(actual_title, expected_title)

    def popup_message_should_be_displayed(self):
        popup_message = self.main_panel.pop_up_messages.get_popup_message()
        self.assertions.verify_element_is_displayed(popup_message)

    def popup_message_text_should_be(self, expected_message_text: str):
        actual_message_text = self.main_panel.obtain_text_of_form_main_panel_pop_up_message()
        self.assertions.verify_equal_ignore(actual_message_text, expected_message_text)

    def component_title_should_be(self, expected_result, component_id):
        actual_result = self.flow_board.obtain_component_title_in_flow_main_panel(component_id)
        self.assertions.verify_equal_ignore(actual_result, expected_result)

    def components_titles_should_be(self, component_dict: dict):
        with soft_assertions():
            for key, value in component_dict.items():
                self.component_title_should_be(value, key)

    def components_titles_should_not_have_errors(self, component_dict: dict, expected_rgb_color: str):
        with soft_assertions():
            for key, value in component_dict.items():
                color = self.flow_board.obtain_component_color_in_flow_main_panel(key)
                self.assertions.verify_is_not_equal(color, expected_rgb_color)

    def user_selected_in_flow_permissions_should_be(self, user: str):
        actual_user = FlowPermissionsActions().obtain_user_list_selected_in_text_box_in_flow_permissions()[0]
        self.assertions.verify_equal_ignore(actual_user, user)

    def user_in_section_visibility_should_be(self, expected_result: str, dropdown_index: str = "3"):
        actual_result = \
        self.section_visibility.obtain_user_list_selected_in_text_box_in_section_visibility(
            dropdown_index)[0]
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def user_in_process_permission_should_be(self, expected_result: str):
        actual_result = \
        self.process_permission.obtain_user_list_selected_in_text_box_in_process_permissions()[0]
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def user_in_flow_permission_should_be(self, expected_result: str):
        actual_result = \
        self.flow_permission.obtain_user_list_selected_in_text_box_in_flow_permissions()[0]
        self.verification.verify_equal_ignore(actual_result, expected_result)
