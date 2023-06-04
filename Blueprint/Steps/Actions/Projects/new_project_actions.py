from Blueprint.PageObject.Projects.new_project_objects import NewProjectObjects
from selenium.webdriver.common.keys import Keys
from Blueprint.PageObject.Flows.Elements.dropdowns import Dropdownbox


class NewProjectActions(NewProjectObjects):
    """This class represents the actions in new project page."""
    def __init__(self):
        super().__init__()
        self.dropdown = Dropdownbox('projects_new_project')

    def click_create_button_in_new_project_page(self) -> None:
        """Clicks create button."""
        self.get_create_button().click()

    def insert_text_or_number_in_a_component_in_new_project_page(self, section_name: str, label_name: str, value: str) -> None:
        """Inserts text or number in the textbox or numbericbox selected inside a section."""
        self.get_element_locator_from_each_section(section_name, label_name).send_keys(value)

    def click_a_component_inside_a_section_in_new_project_page(self, section_name: str, label_name: str) -> None:
        """Clicks on a specific textbox, numberbox, datebox or userlist inside a section."""
        self.get_element_locator_from_each_section(section_name, label_name).click()

    def click_a_checkbox_label_inside_a_section_in_new_project_page(self, section_name: str, label_name: str) -> None:
        """Clicks on any checkbox inside a section."""
        self.get_checkbox_label_locator(section_name, label_name).click()
    
    def click_a_checkbox_inside_a_section_in_new_project_page(self, section_name: str, label_name: str) -> None:
        """Clicks on any checkbox inside a section."""
        self.get_checkbox_locator(section_name, label_name).click()
        
    def select_user_from_the_dropdown_in_new_project_page(self, section_name: str, label_name: str, user: str) -> None:
        """Selects a user from the userlist dropdown."""
        self.dropdown.click_dropdown('TEXT_USER_NUMBER_DATE_BOX', section_name, label_name)
        self.dropdown.scroll_down('SELECT_USER', user)
        
    def delete_option_of_the_dropdown_in_new_project_page(self, section_name: str, label_name: str) -> None:
        """Deletes the users or group selected by clicking on the 'x' icon."""
        self.dropdown.delete_all_options('REMOVE_USER_LOCATOR', section_name, label_name)

    def increase_numbericbox_value_in_new_project_page(self, section_name: str, label_name: str, number: int = 1) -> None:
        """Increases the number value in a numbericbox inside a section."""
        element = self.get_element_locator_from_each_section(section_name, label_name)
        element.click()
        for _ in range(number): 
            element.send_keys(Keys.ARROW_UP)

    def decrease_numbericbox_value_in_new_project_page(self, section_name: str, label_name: str, number: int = 1) -> None:
        """Decreases the number value in a numbericbox inside a section."""
        element = self.get_element_locator_from_each_section(section_name, label_name)
        element.click() 
        for _ in range(number):
            element.send_keys(Keys.ARROW_DOWN)

    def mouse_over_create_button_in_new_project_page(self) -> None:
        """Position the mouse pointer over create button."""
        button = self.get_create_button()
        self.action_chains.move_to_an_element(button)
    
    def clear_the_content_of_a_component_in_new_project_page(self, section_name: str, label_name: str) -> None:
        """removes the text or number in a textbox or numbericbox in new request page."""
        self.get_element_locator_from_each_section(section_name, label_name).clear()

    def remove_the_content_of_a_component_in_new_project_page(self, section_name: str, label_name: str) -> None:
        """removes the text or number in a textbox or numbericbox in new request page."""
        element = self.get_element_locator_from_each_section(section_name, label_name)
        second_element = self.get_the_locator_of_flow_template_title()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        second_element.click()

    def get_text_of_create_button(self) -> str:
        """Returns the name of create button in new project page."""
        create_button = self.get_create_button().text
        return create_button
    
    def get_the_title_of_a_flow_template_in_project_page(self) -> str:
        """Returns the title of a flow template in new project page."""
        template_title = self.get_the_locator_of_flow_template_title().text
        return template_title

    def get_the_content_of_a_component_in_new_project_page(self, section_name: str, label_name: str) -> str:
        """Gets the text or number of a text box or number box in new project page."""
        content = self.get_element_locator_from_each_section(section_name, label_name).get_attribute('value')
        return content
    
    def get_create_button_rgb_color(self) -> str:
        """Gets the RGB color of the create button in new project page."""
        rgb_color = self.get_create_button().value_of_css_property('background-color')
        return rgb_color

    def get_the_label_rgb_color_of_each_component(self, section_name: str, label_name: str) -> str:
        """Gets the label RGB color of each component in a section in new project page when the mouse is over the component."""
        rgb_color = self.get_locator_from_the_label_of_each_component(section_name, label_name).value_of_css_property('color')
        return rgb_color
    
    def get_the_rgb_border_color_of_each_component(self, section_name: str, label_name: str) -> str:
        """Gets the RGB border color of each component in a section in new project page."""
        rgb_color = self.get_element_locator_from_each_section(section_name, label_name).value_of_css_property('border-color')
        return rgb_color

    def mouse_over_label_of_a_component_in_new_project_page(self, section_name: str, label_name: str) -> None:
        """Positions the mouse pointer over the label of a component in a section in new project page."""
        label = self.get_locator_from_the_label_of_each_component(section_name, label_name)
        self.action_chains.move_to_an_element(label)
        
    def mouse_over_input_text_box_of_a_component_new_project_page(self, section_name: str, label_name: str) -> None:
        """Positions the mouse pointer over the input text box of a component in a section in new project page."""
        text_box = self.get_element_locator_from_each_section(section_name, label_name)
        self.action_chains.move_to_an_element(text_box)
        
    def get_the_content_of_a_dropdown(self, section_name: str, label_name: str) -> str:
        """Gets the content present in the dropdown"""
        dropdown_content = self.get_element_locator_from_text_dropdown(section_name, label_name).get_attribute('textContent')
        return dropdown_content

    def click_in_the_dropdown(self, section_name: str, label_name: str):
        """Clicks in the specified dropdown"""
        self.dropdown.click_dropdown('TEXT_USER_NUMBER_DATE_BOX', section_name, label_name)
