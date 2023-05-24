from Libraries.Drivers.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class BaseComponent(BasePage):
    """This class represents the common attributs and methods of components"""
    
    def __init__(self, id: str, canvas: WebElement) -> None:
        super().__init__()
        self.id = id
        self.element = self.get_component()
        self.title = self.get_component_title()
        self.canvas = canvas
        self.properties = ""
        self.x_percentage, self.y_percentage = self.convert_pixel_to_percentage()
    
    def get_component(self) -> WebElement:
        """Returns the component"""
        element = self.find_element.by_id(self.id)
        return element

    def get_component_title(self) -> str:
        """Returns the component's title"""
        title = self.element.text
        return title

    def move_component(self, new_position_x: int, new_position_y: int) -> None:
        """Moves component by position"""
        x = new_position_x
        y = new_position_y
        self.action_chains.drag_and_drop_by_position(self.element, self.canvas, x, y)

    def select_component(self) -> None:
        """Selects component"""
        self.element.click()
    
    def convert_pixel_to_percentage(self) -> list:
        """Converts the position from pixels to percentage"""
        canvas_size = self.canvas.size
        width = canvas_size["width"] 
        height = canvas_size["height"] 
        x_canvas = self.canvas.location['x']
        y_canvas = self.canvas.location['y']
        element_x = self.element.location['x'] - (width - 1) / 2 - x_canvas
        element_y = self.element.location['y'] - (height - 1) / 2 - y_canvas
        x_percentage = ((element_x + (width / 2)) / (width - 166)) * 100
        y_percentage = ((element_y + (height / 2)) / (height - 23)) * 100
        return x_percentage, y_percentage
    
    def __repr__(self) -> str:
        return f"title: {self.title}, x_position: {self.x_percentage}, y_position: {self.y_percentage}"
