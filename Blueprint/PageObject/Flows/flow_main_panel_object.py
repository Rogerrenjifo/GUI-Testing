from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flow_main_panel_locators as locators
from Blueprint.PageObject.Flows.elements.components.first_component import FirstComponent
from Blueprint.PageObject.Flows.elements.components.start_component import StartComponent


class FlowMainPanelObject(BasePage):
    """This class represents main panel of create flow"""
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.canvas = self.get_canvas_element()
        self.start_component = StartComponent(locators.START_ID, self.canvas, self.driver)
        self.first_component = FirstComponent(locators.FIRST_ID, self.canvas, self.driver)
    
    def generate_elements(self) -> WebElement:
        """Generates all the components from canvas board."""
        elements = self.find_elements.by_xpath(locators.COMPONENT_LIST_XPATH)
        return elements

    def generate_components_ids(self) -> list:
        """Generates components ids."""
        list_id=[]
        elements = self.generate_elements()
        for element in elements:
            element_id = element.get_attribute('id')
            list_id.append(element_id)
        return list_id

    def get_canvas_element(self) -> WebElement:
        """Returns the canvas element."""
        element = self.find_element.by_id(locators.CANVAS)
        return element
