from Blueprint.PageObject.Flows.flow_components_object import FlowComponentObjects
from Blueprint.PageObject.Flows.Elements.Components.action_component import ActionComponent
from Blueprint.PageObject.Flows.Elements.Components.step_component import StepComponent
from Blueprint.PageObject.Flows.Elements.Components.component_storage import ComponentStorage


class FlowComponentsActions(FlowComponentObjects):
    """This class represents the components of a Blueprint application"""
    def __init__(self) -> None:
        super().__init__()
        self.index = ComponentStorage()

    def move_action_to_board_position(self, x_percentage: int, y_percentage: int) -> None:
        """Drags and drops an action to the center of the board"""
        component = self.get_action_element()
        self.action_chains.drag_and_drop_by_position(
            component, self.get_canvas_element(), x_percentage, y_percentage)
        id = f"002Added{self.index.counter_action}"
        self.index.add_component(id, ActionComponent(id))
        self.index.increment_counter_action()

    def move_step_to_board_position(self, x_percentage: int, y_percentage: int) -> None:
        """Drags and drops a step to the center of the board"""
        component = self.get_step_element()
        self.action_chains.drag_and_drop_by_position(
            component, self.get_canvas_element(), x_percentage, y_percentage)
        component_id = f"001Added{self.index.counter_step}"
        self.index.add_component(component_id, StepComponent(component_id))
        self.index.increment_counter_step()

    def move_action_to_main_menu_position(self, x_percentage: int, y_percentage: int) -> None:
        """Drags and drops an action to specific position of the main menu"""
        component = self.get_action_element()
        self.action_chains.drag_and_drop_by_position(
            component, self.get_main_menu_element(), x_percentage, y_percentage)

    def move_step_to_main_menu_position(self, x_percentage: int, y_percentage: int) -> None:
        """Drags and drops an step to specific position of the main menu"""
        component = self.get_step_element()
        self.action_chains.drag_and_drop_by_position(
            component, self.get_main_menu_element(), x_percentage, y_percentage)

    def move_action_to_component_panel_position(self, x_percentage: int, y_percentage: int) -> None:
        """Drags and drops an action to specific position of component panel"""
        component = self.get_action_element()
        self.action_chains.drag_and_drop_by_position(
            component, self.get_panel_right_element(), x_percentage, y_percentage)

    def move_step_to_component_panel_position(self, x_percentage: int, y_percentage: int) -> None:
        """Drags and drops an step to specific position of the component panel"""
        component = self.get_step_element()
        self.action_chains.drag_and_drop_by_position(
            component, self.get_panel_right_element(), x_percentage, y_percentage)

    def move_action_to_header_position(self, x_percentage: int, y_percentage: int) -> None:
        """Drags and drops an action to specific position of the header"""
        component = self.get_action_element()
        self.action_chains.drag_and_drop_by_position(
            component, self.get_header_element(), x_percentage, y_percentage)

    def move_step_to_header_position(self, x_percentage: int, y_percentage: int) -> None:
        """Drags and drops an step to specific position of the header"""
        component = self.get_step_element()
        self.action_chains.drag_and_drop_by_position(
            component, self.get_header_element(), x_percentage, y_percentage)

    def move_action_to_properties_position(self, x_percentage: int, y_percentage: int) -> None:
        """Drags and drops an action to specific position of the properties panel"""
        component = self.get_action_element()
        self.action_chains.drag_and_drop_by_position(
            component, self.get_properties_element(), x_percentage, y_percentage)

    def move_step_to_properties_position(self, x_percentage: int, y_percentage: int) -> None:
        """Drags and drops an step to specific position of the properties panel"""
        component = self.get_step_element()
        self.action_chains.drag_and_drop_by_position(
            component, self.get_properties_element(), x_percentage, y_percentage)

    def click_and_hold_step_component(self) -> None:
        """Clicks and hold an 'step' component"""
        component = self.get_step_element()
        self.action_chains.click_and_hold_element(component)

    def click_and_hold_action_component(self) -> None:
        """Clicks and hold an 'action' component"""
        component = self.get_action_element()
        self.action_chains.click_and_hold_element(component)

    def move_component_to_target_position(self, target, x_percentage: int, y_percentage: int) -> None:
        """Moves clicked element to an target position"""
        elements = {"header": self.get_header_element(),
                    "canvas": self. get_canvas_element(),
                    "properties": self.get_properties_element(),
                    "component" : self.get_panel_right_element()}
        self.action_chains.move_element_to(elements.get(target),x_percentage, y_percentage)

    def drop_component(self) -> None:
        """Drop clicked component."""
        self.action_chains.drop_element()
