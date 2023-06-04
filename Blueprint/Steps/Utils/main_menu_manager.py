import time

from selenium.webdriver.common.by import By
from Blueprint.Steps.Actions.MainMenu.main_menu_actions import MainMenuActions
from Blueprint.Steps.Actions.Flows.flow_page_actions import NewFlowActions
from Blueprint.Steps.Actions.Flows.header_actions import HeaderActions
from Blueprint.Steps.Actions.Flows.flow_components_actions import FlowComponentsActions
from Blueprint.Steps.Actions.Flows.flow_main_panel_actions import FlowMainPanelActions
from Blueprint.Steps.Actions.Flows.flows_properties_actions import FlowPropertiesActions
from Blueprint.Steps.Actions.Flows.publish_tab_actions import PublishTabActions
from robot.api import logger


class MainMenuManager:
    def __init__(self):
        self.main_menu = MainMenuActions()
        self.new_flow = NewFlowActions()
        self.flow_header = HeaderActions()
        self.flow_components = FlowComponentsActions()
        self.flow_main_panel = FlowMainPanelActions()

    def flow_exists(self, flow_name: str) -> bool:
        """Verifies the flow name exists in the flows list"""
        self.main_menu.click_on_flows_button()
        self.main_menu.insert_flow_name_into_the_search_bar(flow_name)
        flow_results = len(self.main_menu.get_flow_results_container()
                           .find_elements(By.XPATH, ".//*"))
        self.main_menu.click_on_flows_button()
        return flow_results > 1

    def go_to_existent_project(self, flow_exists: bool, flow_name: str) -> str:
        """Goes to an existent project. If the project does not exist,
         creates a flow with its name, publish it, and redirects to its project page"""
        if flow_exists:
            self.main_menu.go_to_project_process_in_main_menu(flow_name)
        else:
            logger.console("flow no existe")
            # flow_name = "new_flow_name"
            flow_name = self.create_simple_flow()
            self.main_menu.driver.refresh()
            time.sleep(5)
            self.main_menu.go_to_project_process_in_main_menu(flow_name)
            time.sleep(5)
        return flow_name

    def create_simple_flow(self):
        flow_name = self.new_flow.create_a_new_flow_with_random_code()
        self.flow_header.click_tab_in_flow_header("Create Flow")
        self.flow_components.move_action_to_board_position(20, 60)
        self.flow_main_panel.click_component("first")
        self.flow_main_panel.connect_components_in_flow_main_panel(source_id="first",
                                                                   target_id="002Added1",
                                                                   source_point_number=12,
                                                                   target_point_number=4)
        self.flow_components.move_step_to_board_position(70, 60)
        self.flow_main_panel.click_component("002Added1")
        self.flow_main_panel.connect_components_in_flow_main_panel(source_id="002Added1",
                                                                   target_id="001Added1",
                                                                   source_point_number=8,
                                                                   target_point_number=16)
        self.flow_main_panel.click_component("001Added1")
        FlowPropertiesActions().click_end_step_checkbox_in_flow_properties("001Added1")
        self.flow_header.click_tab_in_flow_header("Publish")
        PublishTabActions().click_save_publish_button()
        time.sleep(8)
        return flow_name
