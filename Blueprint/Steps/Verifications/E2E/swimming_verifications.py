from Blueprint.Steps.Actions.Flows.header_actions import HeaderActions
from Libraries.Assertions.assertions import Verification
from Blueprint.Steps.Actions.Flows.create_form_main_panel_actions import FormMainPanelActions
from Blueprint.Steps.Actions.Flows.flow_main_panel_actions import FlowMainPanelActions
from Blueprint.Steps.Actions.Flows.section_visibility_permissions_actions import SectionsVisibilityActions
from Blueprint.Steps.Actions.Flows.process_permissions_actions import ProcessPermissionsActions
from Blueprint.Steps.Actions.Flows.flow_permissions_actions import FlowPermissionsActions
from Blueprint.Steps.Actions.Flows.section_visibility_permissions_actions import SectionsVisibilityActions
from Blueprint.Steps.Actions.Flows.process_permissions_actions import ProcessPermissionsActions
from Blueprint.Steps.Actions.Flows.flow_permissions_actions import FlowPermissionsActions
from Blueprint.Steps.Actions.Projects.ProjectPage.project_page_actions import ProjectPageActions


class SwimmingCompetitionVerifications:
    """This class represents the verifications for swimming competition E2E Scenario"""
    def __init__(self):
        self.verification = Verification()
        self.board_panel = FlowMainPanelActions()
        self.header = HeaderActions()
        
    def component_type_should_be(self, expected_result: list, section_title: str):
        """Verifies that component type are the expected"""
        actual_result = FormMainPanelActions().get_all_components_type_in_a_section_in_form_main_panel(section_title)
        self.verification.verify_equal_ignore(actual_result, expected_result)
    
    def component_title_should_be(self, expected_title: str, component_id: str):
        """Verifies that title of component is the expected"""
        actual_title = self.board_panel.obtain_component_title_in_flow_main_panel(component_id)
        self.verification.verify_equal_ignore(actual_title, expected_title)

    def component_color_should_be(self, component_id: str):
        """Verifies color component"""
        actual_color = self.board_panel.obtain_component_color_in_flow_main_panel(component_id)
        expected_color = self.color_to_look_for(component_id)
        self.verification.verify_equal_ignore(actual_color, expected_color)
    
    def color_to_look_for(self, component: str) -> str:
        """Returns a color depending of the component"""
        if component[2] == "1":
            return "rgb(0, 217, 194)"
        if component[2] == "2":
            return "rgb(229, 231, 235)"

    def user_in_flow_permission_should_be(self, expected_result: str):
        """Verifies user displayed flow permission"""
        actual_result = FlowPermissionsActions().obtain_user_list_selected_in_text_box_in_flow_permissions()[0]
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def user_in_process_permission_should_be(self, expected_result: str):
        """Verifies user displayed in process permission"""
        actual_result = ProcessPermissionsActions().obtain_user_list_selected_in_text_box_in_process_permissions()[0]
        self.verification.verify_equal_ignore(actual_result, expected_result)
    
    def user_in_section_visibility_should_be(self, expected_result: str, dropdown_index: str = "3"):
        """Verifies user displayed in section visibility"""
        actual_result = SectionsVisibilityActions().obtain_user_list_selected_in_text_box_in_section_visibility(dropdown_index)[0]
        self.verification.verify_equal_ignore(actual_result, expected_result)
    
    def flow_page_title_should_be_displayed(self, expected_result: str):
        """Verifies that flow page has the expected title"""
        actual_result = self.header.get_flow_name_text_in_flow_header()
        self.verification.verify_equal_ignore(actual_result, expected_result)

    def project_title_should_be(self, expected_result: str):
        """Verifies that project title is the expected"""
        actual_result = ProjectPageActions().get_project_name_text_in_project_page()
        self.verification.verify_equal_ignore(actual_result, expected_result)
