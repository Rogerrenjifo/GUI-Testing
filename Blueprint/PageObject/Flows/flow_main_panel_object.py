from selenium.webdriver.remote.webelement import WebElement
from typing import List
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flow_main_panel_locators as locators
from Blueprint.PageObject.Flows.Elements.Components.component_storage import ComponentStorage
from Blueprint.PageObject.Flows.Elements.Components.first_component import FirstComponent
from Blueprint.PageObject.Flows.Elements.Components.start_component import StartComponent


class FlowMainPanelObject(BasePage):
    """This class represents main panel of create flow"""
    def __init__(self) -> None:
        super().__init__()
        self.index = ComponentStorage()
        self.add_start = self.add_start_component_to_dictionary()
        self.add_first = self.add_initial_step_to_dictionary()
    
    def generate_elements(self) -> List[WebElement]:
        """Generates all the components from canvas board."""
        elements = self.find_elements.by_xpath(locators.COMPONENT_LIST_XPATH)
        return elements

    def generate_components_ids(self) -> list:
        """Generates components ids."""
        list_id = []
        elements = self.generate_elements()
        for element in elements:
            element_id = element.get_attribute('id')
            list_id.append(element_id)
        return list_id
    
    def add_start_component_to_dictionary(self) -> None:
        """Adds the start component to the dictionary"""
        id = 'start'
        self.index.add_component(id, StartComponent(locators.START_ID))
    
    def add_initial_step_to_dictionary(self) -> None:
        """Adds the initial step to the dictionary"""
        id = 'first'
        self.index.add_component(id, FirstComponent(locators.FIRST_ID))

    def get_dots_list_of_start_component(self) -> WebElement:
        """Return a dots list of the start component"""
        elements = self.find_elements.by_xpath(locators.DOT_START)
        return elements
