from Blueprint.PageObject.Projects.ProjectTracing.flow_objects import ProjectFlowObject


class ProjectFlowActions(ProjectFlowObject):
    """This class represents the Flow section of the Project Tracing"""

    def get_project_flow_title(self) -> str:
        """Finds and returns the title of the flow"""
        title_project_flow = self.get_title_project_flow().text
        return title_project_flow

    def get_start_text_in_project_flow(self) -> str:
        """Finds and return the text of the start of the flow"""
        start_text = self.get_start_element().text
        return start_text

    def get_final_step_text_in_project_flow(self) -> str:
        """Finds and returns the text of the final step of the flow"""
        final_step_text = self.get_final_step().text
        return final_step_text

    def get_flow_step_text_by_order_in_project_flow(self, number: int) -> str:
        """Finds and returns the text of the steps of the flow"""
        step_text = self.get_flow_step(number).text
        return step_text

    def get_action_text_by_order_in_project_flow(self, number: int) -> str:
        """Finds and returns the text of actions of the flow"""
        action_text = self.get_flow_action(number).text
        return action_text

    def get_data_popup_in_project_flow(self, number: int) -> str:
        """Finds and returns the data of the popup of the actions"""
        action = self.get_flow_action(number)
        self.action_chains.move_to_an_element(action)
        data = self.get_popup_action().text
        return data

    def get_the_rgb_border_popup_in_project_flow(self, number: int) -> str:
        """Finds and returns the rgb border of the popup of the actions"""
        action = self.get_flow_action(number)
        self.action_chains.move_to_an_element(action)
        rgb_border = self.get_popup_action().value_of_css_property('border-color')
        return rgb_border

    def get_start_component_in_project_flow(self):
        """Obtains the start component of the flow"""
        start_component = self.get_start_component_in_flow()
        return start_component

    def get_last_component_in_project_flow(self):
        """Obtains the last component of the flow"""
        last_component = self.get_last_component_in_flow()
        return last_component
