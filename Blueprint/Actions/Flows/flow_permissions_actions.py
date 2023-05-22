from Blueprint.PageObject.Flows.flow_permissions_objects import FlowPermissions


class FlowPermissionsActions(FlowPermissions):
    """This class represents the flow permissions of Blueprint application"""
    def __init__(self, driver):
        """Builds the class constructor"""
        super().__init__(driver)

    def get_flow_permissions_title(self) -> str:
        """returns the flow permissions title"""
        title = self.get_title_flow_permissions().text
        return title

    def get_all_versions_title(self) -> str:
        """returns the (all versions) title"""
        title = self.get_title_all_versions().text
        return title

    def get_flow_admin_title(self) -> str:
        """returns the flow admin title"""
        dropdown_title = self.dropdown_flow_admin.get_title()
        return dropdown_title

    def click_in_dropdown(self):
        """clicks to drop down the box"""
        self.dropdown_flow_admin.click_dropdown()

    def type_name_user_in_dropdown(self, name: str):
        """Types into the dropdown text box"""
        self.dropdown_flow_admin.type_name_user(name)

    def delete_typed_name_in_dropdown(self):
        """Deletes which was typed into the dropdown text box"""
        self.dropdown_flow_admin.delete_typed_name()

    def select_user_in_dropdown(self, user: str):
        """Select a user of the dropdown"""
        self.dropdown_flow_admin.select_dropdown_user(user)

    def delete_all_users_in_dropdown(self):
        """Deletes all user selected of the dropdown"""
        self.dropdown_flow_admin.delete_all_users()

    def get_message_empty_dropdown(self) -> str:
        """Gets the message when dropdown is empty"""
        message = self.dropdown_flow_admin.message_empty()
        return message

    def delete_one_selected_user_in_dropdown(self, name: str):
        """Delete one user from the dropdown"""
        self.dropdown_flow_admin.delete_selected_user(name)

    def delete_selected_users_in_dropdown(self, names: list):
        """Delete users from the dropdown"""
        self.dropdown_flow_admin.delete_selected_users(names)

    def scroll_to_user(self, name: str):
        """Scroll and select a user"""
        self.dropdown_flow_admin.scroll_down(name)


    def click_on_permissions_tab(self):
        self.get_permissions_tab().click()
