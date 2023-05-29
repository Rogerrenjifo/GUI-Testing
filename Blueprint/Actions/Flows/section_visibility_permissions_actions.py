from Blueprint.PageObject.Flows.process_permissions_objects import ProcessPermissions
from Blueprint.PageObject.Flows.Elements.dropdowns import Dropdownbox


class SectionsVisibilityActions(ProcessPermissions):
    """This class represents the section visibility of a Blueprint application"""
    def __init__(self):
        super().__init__()
        self.dropdown = Dropdownbox('permissions')
        
    def get_sections_title(self, dropdown_index: str) -> str:
        """Gets the title of the sections visibility"""
        return self.dropdown.get_title('TITLE', dropdown_index)

    def click_in_section_dropdown(self, dropdown_index: str):
        """Clicks in the dropdown of the sections visibility"""
        self.dropdown.click_dropdown('TEXT_BOX', dropdown_index)

    def type_name_user_in_section_dropdown(self, name: str, dropdown_index: str):
        """Types the name of a user in a dropdown of the sections visibility"""
        self.dropdown.type_characters_in_dropdown('INPUT_TEXT_BOX', name, dropdown_index)

    def delete_typed_name_in_section_dropdown(self, dropdown_index: str):
        """Deletes typed name from the dropdown of the sections visibility"""
        self.dropdown.delete_typed_characters_in_dropdown('INPUT_TEXT_BOX', dropdown_index)

    def select_user_in_section_dropdown(self, user: str, dropdown_index: str):
        """Selects a user from the dropdown of the sections visibility"""
        self.dropdown.select_dropdown_option('SELECT_USER', user, dropdown_index)

    def delete_all_users_in_section_dropdown(self, dropdown_index: str):
        """Deletes all name users from the dropdown of the sections visibility"""
        self.dropdown.delete_all_options('DELETE_ALL_USERS', dropdown_index=dropdown_index)

    def get_message_empty_in_section_dropdown(self, dropdown_index: str):
        """Gets the message when dropdown is empty of the sections visibility"""
        return self.dropdown.message_empty_in_dropdown('EMPTY_MESSAGE', dropdown_index)

    def delete_one_selected_user_in_dropdown(self, name: str, dropdown_index: str):
        """Delete one user from the dropdown of the sections visibility"""
        self.dropdown.delete_selected_option('DELETE_ONE_USER', name, dropdown_index)

    def delete_selected_users_in_dropdown(self, names: list, dropdown_index: str):
        """Delete users from the dropdown of the sections visibility"""
        for name in names:
            self.delete_one_selected_user_in_dropdown(name, dropdown_index)

    def scroll_to_user(self, name: str, dropdown_index: str):
        """Scroll and select a user of the sections visibility"""
        self.dropdown.scroll_down('SELECT_USER', name, dropdown_index)

    def click_dropdown_arrow(self, dropdown_index: str):
        """Clicks on dropdown arrow"""
        self.dropdown.click_drop_arrow('DROPDOWN_ARROW', dropdown_index)

    def add_user_to_section_visibility_by_typing_process(self, name: str, dropdown_index: str):
        """Adds a new user to section visibility process by typing the name"""
        self.type_name_user_in_section_dropdown(name, dropdown_index)
        self.select_user_in_section_dropdown(name, dropdown_index)

    def add_user_to_section_visibility_by_scrolling_process(self, name: str, dropdown_index: str):
        """Adds a new user to section visibility by scrolling to the name"""
        self.click_dropdown_arrow(dropdown_index)
        self.scroll_to_user(name, dropdown_index)
