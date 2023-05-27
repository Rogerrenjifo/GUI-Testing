from Blueprint.PageObject.Flows.flow_permissions_objects import FlowPermissions


class FlowPermissionsActions(FlowPermissions):
    """This class represents the flow permissions of Blueprint application"""

    def get_flow_permissions_title(self) -> str:
        """Returns the flow permissions title"""
        title = self.get_title_flow_permissions().text
        return title

    def get_all_versions_title_in_flow_permissions(self) -> str:
        """Returns the (all versions) title"""
        title = self.get_title_all_versions().text
        return title

    def get_flow_admin_title_in_flow_permissions(self) -> str:
        """Returns the flow admin title"""
        dropdown_title = self.dropdown_flow_admin.get_title()
        return dropdown_title

    def click_in_dropdown_in_flow_permissions(self):
        """Clicks to drop down the box"""
        self.dropdown_flow_admin.click_dropdown()

    def type_name_user_in_dropdown_in_flow_permissions(self, name: str):
        """Types into the dropdown text box"""
        self.dropdown_flow_admin.type_name_user(name)

    def delete_typed_name_in_dropdown_in_flow_permissions(self):
        """Deletes which was typed into the dropdown text box"""
        self.dropdown_flow_admin.delete_typed_name()

    def select_user_from_dropdown_in_flow_permissions(self, user: str):
        """Select a user of the dropdown"""
        self.dropdown_flow_admin.select_dropdown_user(user)

    def delete_all_users_in_dropdown_in_flow_permissions(self):
        """Deletes all user selected of the dropdown"""
        self.dropdown_flow_admin.delete_all_users()

    def get_message_empty_dropdown_in_flow_permissions(self) -> str:
        """Gets the message when dropdown is empty"""
        message = self.dropdown_flow_admin.message_empty()
        return message

    def delete_one_selected_user_in_dropdown_in_flow_permissions(self, name: str):
        """Delete one user from the dropdown"""
        self.dropdown_flow_admin.delete_selected_user(name)

    def delete_selected_users_in_dropdown_in_flow_permissions(self, names: list):
        """Delete users from the dropdown"""
        self.dropdown_flow_admin.delete_selected_users(names)

    def scroll_to_user_in_flow_permissions(self, name: str):
        """Scroll and select a user"""
        self.dropdown_flow_admin.scroll_down(name)
        
    def click_dropdown_arrow_in_flow_permissions(self):
        """Clicks on dropdown arrow"""
        self.dropdown_flow_admin.click_drop_arrow()

    def add_new_flow_admin_by_typing_process_in_flow_permission(self, name: str):
        """Adds a new flow administrator by typing the name"""
        self.type_name_user_in_dropdown_in_flow_permissions(name)
        self.select_user_from_dropdown_in_flow_permissions(name)

    def add_new_flow_admin_by_scrolling_process_in_flow_permission(self, name: str):
        """Adds a new flow administrator by scrolling to the name"""
        self.click_dropdown_arrow_in_flow_permissions()
        self.scroll_to_user_in_flow_permissions(name)
