from Blueprint.PageObject.Flows.flow_main_panel_object import FlowMainPanelObject
from Blueprint.PageObject.Flows.Elements.Components.component_storage import ComponentStorage
from Blueprint.PageObject.Flows.Elements.Components.action_component import ActionComponent
from Blueprint.PageObject.Flows.Elements.Components.step_component import StepComponent
from Blueprint.PageObject.Flows.Elements.Components.base_component import BaseComponent


class FlowMainPanelActions(FlowMainPanelObject):
    """Represents the actions of Create flow main panel"""

    def __init__(self) -> None:
        super().__init__()
        self.index = ComponentStorage()

    def move_component_to_specific_position_in_flow_main_panel(self, component_id: str, x: int, y: int) -> None:
        """Moves components to specific position."""
        component = self.index.component_dictionary[component_id]
        component.move_component(x, y)

    def connect_components_in_flow_main_panel(self, source_id: str, target_id: str, source_point_number: int,
                                                target_point_number: int) -> None:
        """Connect two components."""
        source_component = self.index.component_dictionary[source_id]
        target_component = self.index.component_dictionary[target_id]
        target_endpoint = target_component.get_connector_element(target_point_number)
        source_component.connect_component(target_endpoint, source_point_number)

    def delete_component_in_flow_main_panel(self, component_id: str) -> None:
        """Deletes 'actions' or 'steps' component."""
        component = self.index.component_dictionary[component_id]
        component.delete()
        del self.index.component_dictionary[component_id]

    def clone_component_in_flow_main_panel(self, component_id) -> None:
        """Clones 'actions' or 'steps' components."""
        component = self.index.component_dictionary[component_id]
        component.clone()
        if component.type == "Action":
            new_id = f"002Added{self.index.counter_action}"
            self.index.add_component(new_id, ActionComponent(new_id))
            self.index.increment_counter_action()
        if component.type == "Step":
            new_id = f"001Added{self.index.counter_step}"
            self.index.add_component(new_id, StepComponent(new_id))
            self.index.increment_counter_step()

    def click_component(self, component_id: str) -> None:
        """Clicks a component"""
        component: BaseComponent = self.index.component_dictionary[component_id]
        component.select_component()
    
    def obtain_component_color_in_flow_main_panel(self, component_id :str) -> str:
        """Returns the component color"""
        component = self.index.component_dictionary[component_id]
        color = component.get_component_color()
        return color
    
    def obtain_component_title_in_flow_main_panel(self, component_id :str) -> str:
        """Returns the component title"""
        component = self.index.component_dictionary[component_id]
        title = component.get_component_title()
        return title
