from Blueprint.PageObject.Flows.Elements.Components.base_component import BaseComponent
from Blueprint.Locators.Flows import flow_main_panel_locators as elements
from selenium.webdriver.remote.webelement import WebElement


class EndComponent(BaseComponent):
    """This class represents an end component"""
    def __init__(self, id) -> None:
        super().__init__(id)
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

    def get_dot_status(self, dot: WebElement) -> bool:
        """Returns status of dot component"""
        class_name = dot.get_attribute('class')
        is_connected = 'jtk-endpoint-connected' in class_name
        return is_connected
    
    def get_dropdown_menu_options(self) -> list:
        """Returns the list of options in the dropdown menu"""
        self.__click_dots_button()
        options = self.find_elements.by_xpath(elements.MENU_DROPDOWN)
        available_options = [option.text for option in options]
        dropdown_list = available_options[0].split("\n")
        return dropdown_list
    
    def get_color_dropdown(self) -> str:
        """Returns the RGB color code of the dropdown element"""
        xpath = elements.DOTS_BUTTON_XPATH.replace("<<data>>", self.id)
        dropdown = self.find_element.by_xpath(xpath)
        self.action_chains.move_to_an_element(dropdown)
        color = dropdown.value_of_css_property('background-color')
        return color
    
    def connect_component(self, target: WebElement, number: int) -> None:
        """Connect the end step with an action"""
        source = self.get_connector_element(number)
        self.action_chains.drag_and_drop_element(source, target)
