from Blueprint.PageObject.Flows.Elements.Components.base_component import BaseComponent
from Blueprint.Locators.Flows import flow_main_panel_locators as elements
from selenium.webdriver.remote.webelement import WebElement


class FirstComponent(BaseComponent):
    """This class represents a step component"""
    def __init__(self, id) -> None:
        super().__init__(id)
        self.type = "First"

    def connect_component(self, target: WebElement, number: int) -> None:
        """Connect the step with an action"""
        source = self.get_connector_element(number)
        self.action_chains.drag_and_drop_element(source, target)
    
    def get_connector_element(self, number: str) -> WebElement: 
        """Returns the enpoint of the component to connect"""
        xpath = elements.CONECTOR_XPATH.replace("<<data>>", self.id).replace("<<number>>", str(number))
        return self.find_element.by_xpath(xpath)
    
    def get_dot_status(self, dot: WebElement) -> bool:
        """Returns status of dot component"""
        class_name = dot.get_attribute('class')
        is_connected = 'jtk-endpoint-connected' in class_name
        return is_connected
