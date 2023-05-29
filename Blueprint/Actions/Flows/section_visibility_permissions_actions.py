from Blueprint.PageObject.Flows.process_permissions_objects import ProcessPermissions
from Blueprint.PageObject.Flows.Elements.dropdowns import Dropdownbox


class SectionsVisibilityActions(ProcessPermissions):
    """This class represents the section visibility of a Blueprint application"""

    def get_sections_title(self, number: int):
        """Gets the title of the sections visibility"""
        return Dropdownbox('permissions', number=number).get_title('TITLE')

    def click_in_section_dropdown(self, number: int):
        """Clicks in the dropdown of the sections visibility"""
        Dropdownbox('permissions', number=number).click_dropdown('TEXT_BOX')

    def type_name_user_in_section_dropdown(self, number: int, name: str):
        """Types the name of a user in a dropdown of the sections visibility"""
        Dropdownbox('permissions', number=number).type_characters_in_dropdown('INPUT_TEXT_BOX', name)

    def delete_typed_name_in_section_dropdown(self, number: int):
        """Deletes typed name from the dropdown of the sections visibility"""
        Dropdownbox('permissions', number=number).delete_typed_characters_in_dropdown('INPUT_TEXT_BOX')

    def select_user_in_section_dropdown(self, number: int, user: str):
        """Selects a user from the dropdown of the sections visibility"""
        Dropdownbox('permissions', number=number).select_dropdown_option('SELECT_USER', user)

    def delete_all_users_in_section_dropdown(self, number: int):
        """Deletes all name users from the dropdown of the sections visibility"""
        Dropdownbox('permissions', number=number).delete_all_options('DELETE_ALL_USERS')

    def get_message_empty_in_section_dropdown(self, number: int):
        """Gets the message when dropdown is empty of the sections visibility"""
        return Dropdownbox('permissions', number=number).message_empty_in_dropdown('EMPTY_MESSAGE')

    def delete_one_selected_user_in_dropdown(self, number: int, name: str):
        """Delete one user from the dropdown of the sections visibility"""
        Dropdownbox('permissions', number=number).delete_selected_option('DELETE_ONE_USER', name)

    def delete_selected_users_in_dropdown(self, number: int, names: list):
        """Delete users from the dropdown of the sections visibility"""
        for name in names:
            self.delete_one_selected_user_in_dropdown(number, name)

    def scroll_to_user(self, number: int, name: str):
        """Scroll and select a user of the sections visibility"""
        Dropdownbox('permissions', number=number).scroll_down('SELECT_USER', name)

    def click_dropdown_arrow(self, number: int):
        """Clicks on dropdown arrow"""
        Dropdownbox('permissions', number=number).click_drop_arrow('DROPDOWN_ARROW')

    def add_user_to_section_visibility_by_typing_process(self, number: int, name: str):
        """Adds a new user to section visibility process by typing the name"""
        self.type_name_user_in_section_dropdown(number, name)
        self.select_user_in_section_dropdown(number, name)

    def add_user_to_section_visibility_by_scrolling_process(self, number: int, name: str):
        """Adds a new user to section visibility by scrolling to the name"""
        self.click_dropdown_arrow(number)
        self.scroll_to_user(number, name)
