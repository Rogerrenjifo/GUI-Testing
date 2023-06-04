from Blueprint.PageObject.Flows.create_form_main_panel_objects import FormMainPanelPage


class Component(FormMainPanelPage):
    """This class represents an 'action' component"""
    def __init__(self, component_id) -> None:
        super().__init__()
        self.component_id = component_id

    def select_component(self):
        """Clicks a component from main panel for display its properties"""
        self.get_component(self.component_id).click()

    def display_component_delete_menu(self):
        """Displays component drop-down menu from its 3 dots button"""
        self.action_chains.move_to_an_element(self.get_component_dropdown(self.component_id))
        self.get_component_dropdown(self.component_id).click()

    def obtain_component_title(self) -> str:
        """Returns component title displayed in main panel"""
        component_title = self.get_component_title(self.component_id).text
        return component_title

    def select_component_delete_button(self):
        """Clicks delete button from component drop-down menu"""
        self.get_component_delete_button(self.component_id).click()

    def obtain_component_rgb_color(self) -> str:
        """Gets the rgb color of a component title"""
        rgb_color = self.get_component_title(self.component_id).value_of_css_property('color')
        return rgb_color

    def obtain_component_type(self) -> str:
        """Gets the type of a component"""
        component_type = self.get_component(self.component_id).get_attribute("type")
        return component_type
