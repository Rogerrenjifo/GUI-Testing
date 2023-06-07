from Blueprint.Steps.Actions.Flows.header_actions import HeaderActions
from Libraries.Assertions.assertions import Verification
from Blueprint.Steps.Actions.Flows.create_form_main_panel_actions import FormMainPanelActions
from Blueprint.Steps.Actions.Flows.flow_main_panel_actions import FlowMainPanelActions
from Blueprint.Steps.Actions.Flows.section_visibility_permissions_actions import SectionsVisibilityActions
from Blueprint.Steps.Actions.Flows.process_permissions_actions import ProcessPermissionsActions
from Blueprint.Steps.Actions.Flows.flow_permissions_actions import FlowPermissionsActions
from Blueprint.Steps.Actions.CommonElements.popup_messages_actions import PopUpMessagesActions
from Blueprint.Steps.Actions.Projects.ProjectPage.project_page_actions import ProjectPageActions


class ElectricitySupplyVerifications:
    """This class represents the verifications for e2e Scenario"""
    def __init__(self):
        self.header = HeaderActions()
        self.verification = Verification()
        self.board_panel = FlowMainPanelActions()

    def flow_page_should_be_displayed(self, expected_result: str):
        """Verifies that flow page has the expected title"""
        actual_result = self.header.get_flow_name_text_in_flow_header()
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def component_type_should_be(self, expected_result: list, section_title: str = "section-1"):
        """Verifies that component type are the expected"""
        actual_result = FormMainPanelActions().get_all_components_type_in_a_section_in_form_main_panel(section_title)
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def component_title_and_rgb_color_should_be(self, expected_title: str, expected_color: str, component_id: str):
        """Verifies that component title and rgb color are the expected"""
        actual_title = self.board_panel.obtain_component_title_in_flow_main_panel(component_id)
        actual_color = self.board_panel.obtain_component_color_in_flow_main_panel(component_id)
        self.verification.verify_equal_ignore(actual_title, expected_title)
        self.verification.verify_equal_ignore(actual_color, expected_color)

    def verify_that_tab_not_present_errors(self, tab_name: str):
        """Verifies that tab does not have errors"""
        marked_tab = self.header.get_error_marked_tab_in_flow_header(tab_name)
        self.verification.verify_equal_ignore(marked_tab, False)

    def user_in_section_visibility_should_be(self, expected_result: str, dropdown_index: str = "3"):
        """Verifies user displayed in section visibility"""
        actual_result = SectionsVisibilityActions().obtain_user_list_selected_in_text_box_in_section_visibility(dropdown_index)[0]
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def user_in_process_permission_should_be(self, expected_result: str):
        """Verifies user displayed in process permission"""
        actual_result = ProcessPermissionsActions().obtain_user_list_selected_in_text_box_in_process_permissions()[0]
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def user_in_flow_permission_should_be(self, expected_result: str):
        """Verifies user displayed flow permission"""
        actual_result = FlowPermissionsActions().obtain_user_list_selected_in_text_box_in_flow_permissions()[0]
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def pop_up_messages_should_be_displayed(self, expected_messages: list):
        """Verifies tab pop up messages"""
        actual_messages = PopUpMessagesActions().get_popup_message_text()
        self.verification.verify_equal_ignore(actual_messages, expected_messages)

    def project_title_should_be(self, expected_result: str):
        """Verifies that project title is the expected"""
        actual_result = ProjectPageActions().get_project_name_text_in_project_page()
        self.verification.verify_equal_ignore(actual_result, expected_result)
