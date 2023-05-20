from Blueprint.PageObject.UsersAndGroups.selected_users_objects import SelectedUsersObjects


class SelectedUsersActions(SelectedUsersObjects):
    """This class represents the selected users column actions of the Blueprint application"""

    def insert_user_in_search_selected_bar(self, username: str):
        """Inserts the specified username into the search selected bar"""
        self.get_input_search_selected().clear()
        self.get_input_search_selected().send_keys(username)

    def click_on_remove_selected_user(self, index: str = "1"):
        """Clicks on the remove button for the selected user at the specified index (default: 1)"""
        self.get_selected_user_remove_button(index).click()
