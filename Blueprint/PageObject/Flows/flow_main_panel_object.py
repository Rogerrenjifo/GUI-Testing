from selenium.webdriver.remote.webelement import WebElement
from typing import List
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flow_main_panel_locators as locators
from Blueprint.PageObject.Flows.Elements.Components.first_component import FirstComponent
from Blueprint.PageObject.Flows.Elements.Components.start_component import StartComponent


class FlowMainPanelObject(BasePage):
    """This class represents main panel of create flow"""
    def __init__(self) -> None:
        super().__init__()
        self.start_component = StartComponent(locators.START_ID)
        self.first_component = FirstComponent(locators.FIRST_ID)
    
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
