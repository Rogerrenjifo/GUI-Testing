from Blueprint.PageObject.Flows.Elements.Components.base_component import BaseComponent
from Blueprint.Locators.Flows import flow_main_panel_locators as elements
from selenium.webdriver.remote.webelement import WebElement


class EndComponent(BaseComponent):
    """This class represents an end component"""
    def __init__(self, id, canvas) -> None:
        super().__init__(id, canvas)
        self.type = "End"
    
    def delete(self) -> None:
        """Deletes the step"""
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
        """clicks dots menu button"""
        xpath = elements.DOTS_BUTTON_XPATH.replace("<<data>>", self.id)
        menu_step = self.find_element.by_xpath(xpath)
        self.action_chains.custom_click_element(menu_step)
