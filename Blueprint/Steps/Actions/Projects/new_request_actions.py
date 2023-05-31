from Blueprint.PageObject.Projects.new_request_objects import NewRequestObject
from Blueprint.PageObject.Flows.Elements.dropdowns import Dropdownbox
from selenium.webdriver.common.keys import Keys


class NewRequestActions(NewRequestObject):
    """This class represents the actions to create a new request in project page."""
    def __init__(self):
        super().__init__()
        self.dropdown = Dropdownbox('projects_new_project')
        
    def click_create_button_in_new_request(self) -> None:
        """Clicks create button."""
        self.get_create_button().click()

    def insert_text_or_number_in_a_component_in_new_request(self, value: str, section_name: str, label_name: str) -> None:
        """Inserts text or number in the textbox or numeric box selected inside a section."""
        self.get_element_locator_from_each_section(section_name, label_name).send_keys(value)

    def click_a_component_inside_a_section_in_new_request(self, section_name: str, label_name: str) -> None:
        """Clicks on a specific textbox, number box, datebox or user list inside a section."""
        self.get_element_locator_from_each_section(section_name, label_name).click()

    def click_a_checkbox_inside_a_section_in_new_request(self, section_name: str, label_name: str) -> None:
        """Clicks on any checkbox inside a section."""
        self.get_checkbox_locator(section_name, label_name).click()
    
    def select_user_from_the_dropdown_in_new_request(self, section_name: str, label_name: str, user: str) -> None:
        """Selects a user from the userlist dropdown."""
        self.dropdown.click_dropdown('TEXT_USER_NUMBER_DATE_BOX', section_name, label_name)
        self.dropdown.scroll_down('SELECT_USER', user)
    
    def delete_user_or_group_selected_in_new_request(self, section_name: str, label_name: str) -> None:
        """Deletes the users or group selected by clicking on the 'x' icon."""
        self.dropdown.delete_all_options('REMOVE_USER_LOCATOR', section_name, label_name)

    def increase_numbericbox_value_in_new_request(self, section_name: str, label_name: str, number: int = 1) -> None:
        """Increases the number value in a numeric box inside a section."""
        element = self.get_element_locator_from_each_section(section_name, label_name)
        element.click()
        for _ in range(number): 
            element.send_keys(Keys.ARROW_UP)

    def decrease_numbericbox_value_in_new_request(self, section_name: str, label_name: str, number: int = 1) -> None:
        """Decreases the number value in a numeric box inside a section."""
        element = self.get_element_locator_from_each_section(section_name, label_name)
        element.click() 
        for _ in range(number):
            element.send_keys(Keys.ARROW_DOWN)

    def mouse_over_create_button_in_new_request_page(self) -> None:
        """Positions the mouse pointer over create button."""
        button = self.get_create_button()
        self.action_chains.move_to_an_element(button)
    
    def clear_the_content_of_a_component_in_new_request_page(self, section_name: str, label_name: str) -> None:
        """Removes the text or number in a textbox or numeric box in new request page."""
        self.get_element_locator_from_each_section(section_name, label_name).clear()
        
    def get_the_content_of_a_dropdown(self, section_name: str, label_name: str) -> str:
        dropdown_content = self.get_element_locator_from_Text_dropdown(section_name, label_name).get_attribute('textContent')
        return dropdown_content
