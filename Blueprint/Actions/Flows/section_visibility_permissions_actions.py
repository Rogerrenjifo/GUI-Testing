from Blueprint.PageObject.Flows.process_permissions_objects import ProcessPermissions
from Blueprint.PageObject.Flows.Elements.dropdowns import Dropdownbox


class SectionsVisibilityActions(ProcessPermissions):
    """This class represents the section visibility of a Blueprint application"""

    def __int__(self, driver):
        super().__init__(driver)

    def get_sections_title_(self, number: int):
        """Gets the title of the sections visibility"""
        return Dropdownbox(self.driver, number).get_title()

    def click_in_section_dropdown(self, number: int):
        """Clicks in the dropdown of the sections visibility"""
        Dropdownbox(self.driver, number).click_dropdown()

    def type_name_user_in_section_dropdown(self, number: int, name: str):
        """Types the name of a user in a dropdown of the sections visibility"""
        Dropdownbox(self.driver, number).type_name_user(name)

    def delete_typed_name_in_section_dropdown(self, number: int):
        """Deletes typed name from the dropdown of the sections visibility"""
        Dropdownbox(self.driver, number).delete_typed_name()

    def select_user_in_section_dropdown(self, number: int, user: str):
        """Selects a user from the dropdown of the sections visibility"""
        Dropdownbox(self.driver, number).select_dropdown_user(user)

    def delete_all_users_in_section_dropdown(self, number: int):
        """Deletes all name users from the dropdown of the sections visibility"""
        Dropdownbox(self.driver, number).delete_all_users()

    def get_message_empty_in_section_dropdown(self, number: str):
        """Gets the message when dropdown is empty of the sections visibility"""
        return Dropdownbox(self.driver, number).message_empty()

    def delete_one_selected_user_in_dropdown(self, number: int, name: str):
        """Delete one user from the dropdown of the sections visibility"""
        Dropdownbox(self.driver, number).delete_selected_user(name)

    def delete_selected_users_in_dropdown(self, number: int, names: list):
        """Delete users from the dropdown of the sections visibility"""
        Dropdownbox(self.driver, number).delete_selected_users(names)

    def scroll_to_user(self, number: int, name: str):
        """Scroll and select a user of the sections visibility"""
        Dropdownbox(self.driver, number).scroll_down(name)
