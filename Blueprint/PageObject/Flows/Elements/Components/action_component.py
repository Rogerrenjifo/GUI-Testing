from selenium.webdriver.remote.webelement import WebElement
from Blueprint.PageObject.Flows.Elements.Components.base_component import BaseComponent
from Blueprint.Locators.Flows import flow_main_panel_locators as elements


class ActionComponent(BaseComponent):
    """This class represents an 'action' component"""
    def __init__(self, id) -> None:
        super().__init__(id)
        self.type = "Action"

    def connect_component(self, target, number) -> None:
        """Connect the 'action' with an 'step' component"""
        source = self.get_connector_element(number)
        self.action_chains.drag_and_drop_element(source, target)
    
    def delete(self) -> None:
        """Deletes the component"""
        self.__click_dots_button()
        delete_xpath = elements.DELETE_BUTTON_XPATH.replace("<<data>>", self.id)
        delete_option = self.find_element.by_xpath(delete_xpath)
        delete_option.click()

    def clone(self) -> None:
        """Clones the component"""
        self.__click_dots_button()
        clone_xpath = elements.CLONE_BUTTON_XPATH.replace("<<data>>", self.id)
        clone_option = self.find_element.by_xpath(clone_xpath)
        clone_option.click()

    def get_connector_element(self, number: int) -> WebElement: 
        """Returns the enpoint of the component to connect""" 
        xpath = elements.CONECTOR_XPATH.replace("<<data>>", self.id).replace("<<number>>", str(number))
        return self.find_element.by_xpath(xpath)

    def __click_dots_button(self) -> None:
        """Clicks dots menu button"""
        xpath = elements.DOTS_BUTTON_XPATH.replace("<<data>>", self.id)
        menu_step = self.find_element.by_xpath(xpath)
        self.action_chains.custom_click_element(menu_step)
