from Blueprint.PageObject.Flows.process_permissions_objects import ProcessPermissions
from Blueprint.PageObject.Flows.Elements.dropdowns import Dropdownbox


class ProcessPermissionsActions(ProcessPermissions):
    """This class represents the process permission of the Blueprint application"""
    def __init__(self):
        super().__init__()
        self.dropdown = Dropdownbox('permissions', number=2)

    def get_process_permissions_title(self) -> str:
        """Returns the process permissions title"""
        title_process_permissions = self.get_title_process_permissions().text
        return title_process_permissions

    def get_current_permissions_title(self) -> str:
        """Returns the current permissions title"""
        title_current_permissions = self.get_title_current_versions().text
        return title_current_permissions

    def get_section_visibility_title_in_flow_process_permission(self) -> str:
        """Returns the section visibility title"""
        title_section_visibility = self.get_title_section_visibility().text
        return title_section_visibility

    def get_initiate_process_title_in_flow_process_permission(self) -> str:
        """Returns the title of the initiate process dropdown"""
        dropdown_title = self.dropdown.get_title('TITLE')
        return dropdown_title

    def click_in_dropdown_in_flow_process_permission(self):
        """Clicks in the dropdown of the process permissions"""
        self.dropdown.click_dropdown('TEXT_BOX')

    def type_name_user_in_dropdown_in_flow_process_permission(self, name:str):
        """Types the name of a user in a dropdown of the process permissions"""
        self.dropdown.type_characters_in_dropdown('INPUT_TEXT_BOX', name)

    def delete_typed_name_in_dropdown_in_flow_process_permission(self):
        """Deletes typed name from the dropdown of the process permissions"""
        self.dropdown.delete_typed_characters_in_dropdown('INPUT_TEXT_BOX')

    def select_user_in_dropdown_in_flow_process_permission(self, user:str):
        """Selects a user from the dropdown of the process permissions"""
        self.dropdown.select_dropdown_option('SELECT_USER', user)

    def delete_all_users_in_dropdown_in_flow_process_permission(self):
        """Deletes all name users from the dropdown of the sections visibility"""
        self.dropdown.delete_all_options('DELETE_ALL_USERS')

    def get_message_empty_dropdown_in_flow_process_permission(self) -> str:
        """Gets the message when dropdown is empty"""
        message = self.dropdown.message_empty_in_dropdown('EMPTY_MESSAGE')
        return message

    def delete_one_selected_user_in_dropdown_in_flow_process_permission(self, name: str):
        """Delete one user from the dropdown"""
        self.dropdown.delete_selected_option('DELETE_ONE_USER', name)

    def delete_selected_users_in_dropdown_in_flow_process_permission(self, names: list):
        """Delete users from the dropdown"""
        for name in names:
            self.delete_one_selected_user_in_dropdown_in_flow_process_permission(name)

    def scroll_to_user_in_flow_process_permission(self, name: str):
        """Scroll and select a user"""
        self.dropdown.scroll_down('SELECT_USER', name)

    def click_dropdown_arrow_in_flow_process_permission(self):
        """Clicks on dropdown arrow"""
        self.dropdown.click_drop_arrow('DROPDOWN_ARROW')

    def add_user_to_initiate_process_by_typing_process_in_process_permissions(self, name: str):
        """Adds a new user to initiate process by typing the name"""
        self.type_name_user_in_dropdown_in_flow_process_permission(name)
        self.select_user_in_dropdown_in_flow_process_permission(name)

    def add_user_to_initiate_process_by_scrolling_process_in_process_permissions(self, name: str):
        """Adds a new user to initiate process by scrolling to the name"""
        self.click_dropdown_arrow_in_flow_process_permission()
        self.scroll_to_user_in_flow_process_permission(name)
