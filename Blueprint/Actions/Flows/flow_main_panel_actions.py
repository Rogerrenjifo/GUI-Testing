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
        self.target = self.get_canvas_element()

    def move_component_to_specific_position(self, component_id: str, x: int, y: int) -> None:
        """Moves components to specific position."""
        component = self.index.component_dictionary[component_id]
        component.move_component(x, y)

    def select_component(self, component_id: str) -> BaseComponent:
        """Selects 'actions' or 'steps' components"""
        component = self.index.component_dictionary[component_id]
        component.select_component()
        return component

    def connect_component_to(self, source_id: str, target_id: str, source_point_number: int,
                              target_point_number: int) -> None:
        """Connect two components."""
        source_component = self.index.component_dictionary[source_id]
        target_component = self.index.component_dictionary[target_id]
        target_endpoint = target_component.get_connector_element(target_point_number)
        source_component.connect_component(target_endpoint, source_point_number)

    def delete_component(self, id: str) -> None:
        """Deletes 'actions' or 'steps' component."""
        component = self.index.component_dictionary[id]
        component.delete()
        del self.index.component_dictionary[id]

    def clone_component(self, id) -> None:
        """Clones 'actions' or 'steps' components."""
        component = self.index.component_dictionary[id]
        component.clone()
        if component.type =="Action":
            new_id = f"002Added{self.index.counter_action}"
            self.index.add_component(new_id, ActionComponent(new_id, self.target))
            self.index.increment_counter_action()
        if component.type =="Step":
            new_id = f"001Added{self.index.counter_step}"
            self.index.add_component(new_id, StepComponent(new_id, self.target))
            self.index.increment_counter_step()

    def click_component(self, id):
        component:BaseComponent = self.index.component_dictionary[id]
        component.select_component()
        return component
