from Blueprint.PageObject.Flows.flow_main_panel_object import FlowMainPanelObject


class FlowMainPanelActions(FlowMainPanelObject):
    """Represents the actions of Create flow main panel"""

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def  move_component_to_specific_position(self, element, x, y):
        """Move components to specific position."""
        #TODO

    def connect_component_to(self, source, target):
        """Connect two components."""
        self.action_chains.drag_and_drop_element(source, target)

    def delete_component(self, element):
        """deletes a component."""
        #TODO

    def clone_component(self, element):
        """clones component."""
        #TODO

    def select_component(self, element):
        """select a components"""
        #TODO
