from Blueprint.PageObject.Flows.flow_components_object import FlowComponentObjects
from Blueprint.PageObject.Flows.Elements.Components.action_component import ActionComponent
from Blueprint.PageObject.Flows.Elements.Components.step_component import StepComponent
from Blueprint.PageObject.Flows.Elements.Components.component_storage import ComponentStorage


class FlowComponentsActions(FlowComponentObjects):
    """This class represents the components of a Blueprint application"""
    def __init__(self) -> None:
        super().__init__()
        self.index = ComponentStorage()
        self.target = self.get_canvas_element()

    def move_action_to_board_position(self, x_percentage: int, y_percentage: int) -> None:
        """Drags and drops an action to the center of the board"""
        component = self.get_action_element()
        self.action_chains.drag_and_drop_by_position(component, self.target, x_percentage, y_percentage)
        component_id = f"002Added{self.index.counter_action}"
        self.index.add_component(component_id, ActionComponent(component_id, self.target))
        self.index.increment_counter_action()

    def move_step_to_board_position(self, x_percentage: int, y_percentage: int) -> None:
        """Drags and drops a step to the center of the board"""
        component = self.get_step_element()
        self.action_chains.drag_and_drop_by_position(component, self.target, x_percentage, y_percentage)
        component_id = f"001Added{self.index.counter_step}"
        self.index.add_component(component_id, StepComponent(component_id, self.target))
        self.index.increment_counter_step()
