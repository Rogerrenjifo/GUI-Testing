import time
from Blueprint.Steps.Actions.CommonElements.popup_messages_actions import PopUpMessagesActions
from Blueprint.PageObject.UsersAndGroups.available_users_objects import AvailableUsersObjects


class AvailableUsersActions(AvailableUsersObjects):
    """This class represents the users column actions of the Blueprint application"""

    def __init__(self):
        super().__init__()
        self.pop_up_messages = PopUpMessagesActions()

    def create_new_user(self, username: str):
        """Creates a new user with the specified username."""
        self.click_on_new_user_button()
        self.insert_username_into_create_user_dialog(username)
        self.click_on_create_user_button()

    def insert_username_into_the_search_user_bar(self, username: str):
        """Inserts the specified username into the 'Search user' bar."""
        self.get_input_search_users().clear()
        self.get_input_search_users().send_keys(username)

    def click_on_add_button_of_user_result_by_index(self, index: str = "1"):
        """Clicks on the add button of the user result at the specified index (default: 1)"""
        self.get_user_result_add_button(index).click()

    def click_on_new_user_button(self):
        """Clicks on the 'New User' button"""
        self.get_new_user_button().click()

    def insert_username_into_create_user_dialog(self, username: str):
        """Inserts the specified username into the input field"""
        self.get_input_user_name().send_keys(username)

    def click_on_create_user_button(self):
        """Clicks on the create user button"""
        self.get_create_user_button().click()

    def click_on_cancel_create_user_button(self):
        """Clicks on the cancel user button"""
        self.get_cancel_create_user_button().click()

    def get_pop_up_text_user(self):
        """Returns the text of the pop-up message displayed."""
        text = self.pop_up_messages.get_popup_message_text()
        return text

    def close_pop_up(self):
        """Clicks on 'X' button of the popup message"""
        self.pop_up_messages.click_to_close_popup_message()

    def add_users_searched_in_a_group(self, users_list: list):
        """Adds to a group the users of a list"""
        for user in users_list:
            self.insert_username_into_the_search_user_bar(user)
            self.click_on_add_button_of_user_result_by_index()
            time.sleep(3)
