from selenium.webdriver.remote.webelement import WebElement
from Blueprint.PageObject.Flows.flow_components_object import Components


class ComponentsActions(Components):
    """This class represents the components of a Blueprint application"""
    def __init__(self, driver):
        super().__init__(driver)

    def drag_and_drop_action(self) -> WebElement:
        """Drags and Drop action"""
        target = self.get_canvas_element()
        element = self.get_action_element()
        self.action_chains.drag_and_drop_element(element, target)

    def drag_and_drop_step(self) -> WebElement:
        """Drags and Drop step"""
        target = self.get_canvas_element()
        element = self.get_step_element()
        self.action_chains.drag_and_drop_element(element, target)
