from Blueprint.PageObject.Projects.new_request_objects import NewRequestObject
from selenium.webdriver.common.keys import Keys


class NewRequestActions(NewRequestObject):
    """This class represents the actions to create a request in project page."""

    def click_create_button(self) -> None:
        """Clicks create button."""
        self.get_create_button().click()

    def insert_text_or_number_in_a_component(self, value: str, section_name: str, label_name: str) -> None:
        """Inserts text or number in the textbox or numbericbox selected inside a section."""
        self.get_element_locator_from_each_section(section_name, label_name).send_keys(value)

    def click_a_component_inside_a_section(self, section_name: str, label_name: str)-> None:
        """Clicks on a specific textbox, numberbox, datebox or userlist inside a section."""
        self.get_element_locator_from_each_section(section_name, label_name).click()

    def click_a_checkbox_inside_a_section(self, section_name: str, label_name: str) -> None:
        """Clicks on any checkbox inside a section."""
        self.get_checkbox_locator(section_name, label_name).click()
        
    def select_user_from_the_dropdown(self, section_name: str, label_name: str, user: str) -> None:
        """Selects a user from the userlist dropdown."""
        self.get_element_locator_from_each_section(section_name, label_name).click()
        self.get_user_locator_from_dropdown(user).click()

    def delete_user_or_group_selected(self, section_name: str, label_name: str) -> None:
        """Deletes the users or group selected by clicking on the 'x' icon."""
        self.get_element_locator_from_each_section(section_name, label_name).click()
        self.get_locator_from_remove_user().click()

    def increase_numbericbox_value(self, section_name: str, label_name: str, number: int=1) -> None:
        """Increases the number value in a numbericbox inside a section."""
        element = self.get_element_locator_from_each_section(section_name, label_name)
        element.click()
        for _ in range(number): 
            element.send_keys(Keys.ARROW_UP)

    def decrease_numbericbox_value(self, section_name: str, label_name: str, number: int=1) -> None:
        """Decreases the number value in a numbericbox inside a section."""
        element = self.get_element_locator_from_each_section(section_name, label_name)
        element.click() 
        for _ in range(number):
            element.send_keys(Keys.ARROW_DOWN)
