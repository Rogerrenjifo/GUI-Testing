from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flow_main_panel_locators as locators


class FlowMainPanelObject(BasePage):
    """This class represents main panel of create flow"""
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.__start_component = locators.start_id
        self.__first_step = locators.first_id

    def get_title(self, id):
        """Returns title from the component."""
        xpath = f"//div[@id = '{id}']/descendant::span"
        element = self.find_element.by_xpath(xpath).text
        return element
    
    def __get_endpoint_xpath(self, id, number):
        """Returns the endpoint xpath from a component."""
        endpoint = f"endpoint{id}"
        xpath = f"//div[contains(@class,'{endpoint}')][{number}]"
        return xpath

    def get_endpoint_element(self, id, number):
        """Get the conection point from the component."""
        xpath = self.__get_endpoint_xpath(id, number)
        element = self.find_element.by_xpath(xpath)
        return element

    def generate_elements(self):
        """Generates all the components from canvas board."""
        elements = self.find_elements.by_xpath(locators.components_list_xpath)
        return elements

    def generate_components_ids(self):
        """Generates components ids."""
        list_id=[]
        elements = self.generate_elements()
        for element in elements:
            element_id = element.get_attribute('id')
            list_id.append(element_id)
        return list_id
