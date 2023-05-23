from Blueprint.PageObject.Flows.process_permissions_objects import ProcessPermissions


class ProcessPermissionsActions(ProcessPermissions):
    """This class represents the process permission of a Blueprint application"""

    def __int__(self, driver):
        super().__init__(driver)

    def get_process_permissions_title(self) -> str:
        """Returns the process permissions title"""
        title_process_permissions = self.get_title_process_permissions().text
        return title_process_permissions

    def get_current_permissions_title(self) -> str:
        """Returns the current permissions title"""
        title_current_permissions = self.get_title_current_versions().text
        return title_current_permissions

    def get_section_visibility_title(self) -> str:
        """Returns the section visibility title"""
        title_section_visibility = self.get_title_section_visibility().text
        return title_section_visibility

    def get_initiate_process_title(self) -> str:
        """Returns the title of the initiate process dropdown"""
        dropdown_title = self.dropdown_process_admin.get_title()
        return dropdown_title

    def click_in_dropdown(self):
        """Clicks in the dropdown of the process permissions"""
        self.dropdown_process_admin.click_dropdown()

    def type_name_user_in_dropdown(self, name:str):
        """Types the name of a user in a dropdown of the process permissions"""
        self.dropdown_process_admin.type_name_user(name)

    def delete_typed_name_in_dropdown(self):
        """Deletes typed name from the dropdown of the process permissions"""
        self.dropdown_process_admin.delete_typed_name()

    def select_user_in_dropdown(self, user:str):
        """Selects a user from the dropdown of the process permissions"""
        self.dropdown_process_admin.select_dropdown_user(user)

    def delete_all_users_in_dropdown(self):
        """Deletes all name users from the dropdown of the sections visibility"""
        self.dropdown_process_admin.delete_all_users()

    def get_message_empty_dropdown(self) -> str:
        """Gets the message when dropdown is empty"""
        message = self.dropdown_process_admin.message_empty()
        return message

    def delete_one_selected_user_in_dropdown(self, name: str):
        """Delete one user from the dropdown"""
        self.dropdown_process_admin.delete_selected_user(name)

    def delete_selected_users_in_dropdown(self, names: list):
        """Delete users from the dropdown"""
        self.dropdown_process_admin.delete_selected_users(names)

    def scroll_to_user(self, name: str):
        """Scroll and select a user"""
        self.dropdown_process_admin.scroll_down(name)

    def click_dropdown_arrow(self):
        """Clicks on dropdown arrow"""
        self.dropdown_process_admin.click_drop_arrow()
