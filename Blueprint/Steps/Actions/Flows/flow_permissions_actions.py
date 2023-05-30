from Blueprint.PageObject.Flows.flow_permissions_objects import FlowPermissions
from Blueprint.PageObject.Flows.Elements.dropdowns import Dropdownbox


class FlowPermissionsActions(FlowPermissions):
    """This class represents the flow permissions of Blueprint application"""

    def __init__(self):
        super().__init__()
        self.dropdown = Dropdownbox('permissions')
        self.index_dropdown = '1'

    def get_flow_permissions_title(self) -> str:
        """Returns the flow permissions title"""
        title = self.get_title_flow_permissions().text
        return title

    def get_all_versions_title_in_flow_permissions(self) -> str:
        """Returns the (all versions) title"""
        title = self.get_title_all_versions().text
        return title

    def get_flow_admin_title_dropdown_in_flow_permissions(self) -> str:
        """Returns the flow admin dropdown title"""
        dropdown_title = self.dropdown.get_title('TITLE', self.index_dropdown)
        return dropdown_title

    def type_name_user_in_dropdown_in_flow_permissions(self, name: str):
        """Types into the dropdown text box"""
        self.dropdown.type_characters_in_dropdown('INPUT_TEXT_BOX', name, self.index_dropdown)

    def delete_typed_name_in_dropdown_in_flow_permissions(self):
        """Deletes which was typed into the dropdown text box"""
        self.dropdown.delete_typed_characters_in_dropdown('INPUT_TEXT_BOX', self.index_dropdown)

    def select_user_from_dropdown_in_flow_permissions(self, user: str):
        """Selects an user of the dropdown"""
        self.dropdown.select_dropdown_option('SELECT_USER', user, self.index_dropdown)

    def delete_all_users_in_dropdown_in_flow_permissions(self):
        """Deletes all user selected of the dropdown"""
        self.dropdown.delete_all_options('DELETE_ALL_USERS', dropdown_index=self.index_dropdown)

    def get_message_empty_dropdown_in_flow_permissions(self) -> str:
        """Gets the message when dropdown is empty"""
        message = self.dropdown.message_empty_in_dropdown('EMPTY_MESSAGE', self.index_dropdown)
        return message

    def delete_one_selected_user_in_dropdown_in_flow_permissions(self, name: str):
        """Deletes one user from the dropdown"""
        self.dropdown.delete_selected_option('DELETE_ONE_USER', name, self.index_dropdown)

    def delete_selected_users_in_dropdown_in_flow_permissions(self, names: list):
        """Deletes users from the dropdown"""
        for name in names:
            self.delete_one_selected_user_in_dropdown_in_flow_permissions(name)

    def scroll_to_user_in_flow_permissions(self, name: str):
        """Scrolls and select an user"""
        self.dropdown.scroll_down('SELECT_USER', name, self.index_dropdown)

    def click_dropdown_arrow_in_flow_permissions(self):
        """Clicks on dropdown arrow"""
        self.dropdown.click_drop_arrow('DROPDOWN_ARROW', self.index_dropdown)

    def add_new_flow_admin_by_typing_process_in_flow_permission(self, name: str):
        """Adds a new flow administrator by typing the name"""
        self.type_name_user_in_dropdown_in_flow_permissions(name)
        self.select_user_from_dropdown_in_flow_permissions(name)

    def add_new_flow_admin_by_scrolling_process_in_flow_permission(self, name: str):
        """Adds a new flow administrator by scrolling to the name"""
        self.click_dropdown_arrow_in_flow_permissions()
        self.scroll_to_user_in_flow_permissions(name)
