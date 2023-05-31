from Libraries.Drivers.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
from Blueprint.PageObject.Flows.flow_components_object import FlowComponentObjects
from Blueprint.Locators.Flows import flow_main_panel_locators as elements


class BaseComponent(BasePage):
    """This class represents the common attributs and methods of components"""
    
    def __init__(self, id: str) -> None:
        super().__init__()
        self.id = id
        self.components = FlowComponentObjects()
        self.properties = ""
    
    def get_component(self) -> WebElement:
        """Returns the component"""
        element = self.find_element.by_id(self.id)
        return element

    def get_component_title(self) -> str:
        """Returns the component's title"""
        title = self.get_component().text
        return title
    
    def get_component_color(self) -> str:
        """Returns the RGB color code of a component"""
        color = self.get_component().value_of_css_property('border-color')
        return color

    def move_component(self, new_position_x: int, new_position_y: int) -> None:
        """Moves component by position"""
        x = new_position_x
        y = new_position_y
        self.action_chains.drag_and_drop_by_position(self.get_component(), self.components.get_canvas_element(), x, y)

    def select_component(self) -> None:
        """Selects component"""
        self.get_component().click()
    
    def convert_pixel_to_percentage(self) -> list:
        """Converts the position from pixels to percentage"""
        canvas_size = self.components.get_canvas_element().size
        width = canvas_size["width"] 
        height = canvas_size["height"] 
        x_canvas = self.components.get_canvas_element().location['x']
        y_canvas = self.components.get_canvas_element().location['y']
        element_x = self.get_component().location['x'] - (width - 1) / 2 - x_canvas
        element_y = self.get_component().location['y'] - (height - 1) / 2 - y_canvas
        x_percentage = ((element_x + (width / 2)) / (width - 166)) * 100
        y_percentage = ((element_y + (height / 2)) / (height - 23)) * 100
        return x_percentage, y_percentage
    
    def is_element_not_found(self) -> bool:
        """Checks if the element is not found"""
        try:
            xpath = elements.DOTS_BUTTON_XPATH.replace("<<data>>", self.id)
            self.find_element.by_xpath(xpath)
            return False
        except Exception:
            return True

    def __repr__(self) -> str:
        return f"title: {self.get_component_title()}, x_position: {self.convert_pixel_to_percentage()[0]}, y_position: {self.convert_pixel_to_percentage()[1]}"
