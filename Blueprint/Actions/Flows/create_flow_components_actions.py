from selenium.webdriver.remote.webelement import WebElement
from Blueprint.PageObject.Flows.create_flow_components_locators import Components
from Libraries.Drivers.action_chains import ActionsChains


class ComponentsActions(Components):
    """This class represents the components of a Blueprint application"""

    def drag_and_drop_action(self, target) -> WebElement:
        """Drags and Drop action"""
        element = self.get_action_element()
        self.action_chains.drag_and_drop_element(element, target)

    def drag_and_drop_step(self, target) -> WebElement:
        """Drags and Drop step"""
        element = self.get_step_element()
        self.action_chains.drag_and_drop_element(element, target)
