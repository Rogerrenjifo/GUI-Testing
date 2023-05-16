from Blueprint.PageObject.Flows.permissions_objects import FlowPermissions


class FlowPermissionsActions(FlowPermissions):
    """This class represents the login page of a Blueprint application"""

    def get_permission_label(self):
        """Log in user with given credentials"""
        text = self.get_title_flow_permissions().text
        return text

    def click_on_permissions_tab(self):
        self.get_permissions_tab().click()

    def get_all_versions_title(self):
        # TODO

    def get_flow_admin_subtitle(self):
        # TODO

    def get_default_label(self):
        # TODO

    def set_text(self):
        # TODO

    def delete_text(self):
        # TODO

    def dropdown_narrow(self):
        # TODO

    def scroll(self):
        # TODO

    def select_user(self):
        # TODO

    def delete_user(self):
        # TODO

    def delete_all_users(self):
        # TODO

    def get_default_text_button(self):
        # TODO

    def click_save_button(self):
        # TODO
