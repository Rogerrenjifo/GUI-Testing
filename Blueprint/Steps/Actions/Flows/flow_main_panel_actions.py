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
    
    def obtain_dictionary_status_in_flow_main_panel(self) -> list:
        """Returns the dictionary with the current components"""
        dictionary = self.index.component_dictionary
        return dictionary
    
    def obtain_component_dot_status_in_flow_main_panel(self, component_id :str, component_number: int) -> bool:
        """Returns status of a dot component"""
        target_component = self.index.component_dictionary[component_id]
        target_endpoint = target_component.get_connector_element(component_number)
        dot_status = target_component.get_dot_status(target_endpoint)
        return dot_status
    
    def obtain_dots_list_of_start_component_in_flow_main_panel(self) -> list:
        """Returns a list of dots associated with the start component"""
        dots_list = self.get_dots_list_of_start_component()
        return dots_list
    
    def is_dropdown_not_found_in_flow_main_panel(self, component_id :str) -> bool:
        """Checks if a dropdown component is not found"""
        component = self.index.component_dictionary[component_id]
        is_found = component.is_element_not_found()
        return is_found
    
    def obtains_dropdown_options_in_flow_main_panel(self, component_id :str) -> list:
        """Returns a list of options available in a dropdown"""
        component = self.index.component_dictionary[component_id]
        options = component.get_dropdown_menu_options()
        return options
    
    def obtain_dropdown_color_in_flow_main_panel(self, component_id :str) -> str:
        """Returns the color of dropdown"""
        component = self.index.component_dictionary[component_id]
        color = component.get_color_dropdown()
        return color
    
    def obtain_x_and_y_position_component_in_flow_main_panel(self, component_id :str) -> list:
        """Returns a list of component positions"""
        component = self.index.component_dictionary[component_id]
        x_position, y_position = component.convert_pixel_to_percentage()
        return x_position, y_position
