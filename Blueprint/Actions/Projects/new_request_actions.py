from Blueprint.PageObject.Projects.new_request_objects import NewRequestObject
from Blueprint.PageObject.Flows.Elements.dropdowns import Dropdownbox


class NewRequestActions(NewRequestObject, Dropdownbox):
    """This class represents the actions to create a request in project page."""

    def __init__(self):
        super().__init__()

    def click_create_button(self):
        """Clicks create button."""
        self.get_create_button().click()

    def insert_text_or_number_in_a_component(self, value: str, section_name: str, label_name: str):
        """Insert text or number in the component selected."""
        self.get_locator(section_name, label_name).send_keys(value)

    def click_a_component_inside_a_section(self, section_name: str, label_name: str):
        """Clicks on any component inside a section."""
        self.get_locator(section_name, label_name).click()
        
    def select_user_from_the_dropdown(self, user: str):
        """Selects a user from the userlist dropdown"""
        self.select_dropdown_user(user)

    def delete_user_selected(self):
        """Deletes the users selected."""
        self.delete_all_users(self)
