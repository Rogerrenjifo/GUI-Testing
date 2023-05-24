from Blueprint.PageObject.Flows.process_permissions_objects import ProcessPermissions
from Blueprint.PageObject.Flows.Elements.dropdowns import Dropdownbox


class SectionsVisibilityActions(ProcessPermissions):
    """This class represents the section visibility of a Blueprint application"""

    def get_sections_title_(self, number: int):
        """Gets the title of the sections visibility"""
        return Dropdownbox(number).get_title()

    def click_in_section_dropdown(self, number: int):
        """Clicks in the dropdown of the sections visibility"""
        Dropdownbox(number).click_dropdown()

    def type_name_user_in_section_dropdown(self, number: int, name: str):
        """Types the name of a user in a dropdown of the sections visibility"""
        Dropdownbox(number).type_name_user(name)

    def delete_typed_name_in_section_dropdown(self, number: int):
        """Deletes typed name from the dropdown of the sections visibility"""
        Dropdownbox(number).delete_typed_name()

    def select_user_in_section_dropdown(self, number: int, user: str):
        """Selects a user from the dropdown of the sections visibility"""
        Dropdownbox(number).select_dropdown_user(user)

    def delete_all_users_in_section_dropdown(self, number: int):
        """Deletes all name users from the dropdown of the sections visibility"""
        Dropdownbox(number).delete_all_users()

    def get_message_empty_in_section_dropdown(self, number: int):
        """Gets the message when dropdown is empty of the sections visibility"""
        return Dropdownbox(number).message_empty()

    def delete_one_selected_user_in_dropdown(self, number: int, name: str):
        """Delete one user from the dropdown of the sections visibility"""
        Dropdownbox(number).delete_selected_user(name)

    def delete_selected_users_in_dropdown(self, number: int, names: list):
        """Delete users from the dropdown of the sections visibility"""
        Dropdownbox(number).delete_selected_users(names)

    def scroll_to_user(self, number: int, name: str):
        """Scroll and select a user of the sections visibility"""
        Dropdownbox(number).scroll_down(name)

    def click_dropdown_arrow(self, number: int):
        """Clicks on dropdown arrow"""
        Dropdownbox(number).click_drop_arrow()

    def add_user_to_section_visibility_by_typing(self, number: int, name: str):
        self.type_name_user_in_section_dropdown(number, name)
        self.select_user_in_section_dropdown(number, name)

    def add_user_to_section_visibility_by_scrolling(self, number: int, name: str):
        self.click_dropdown_arrow(number)
        self.scroll_to_user(number, name)
