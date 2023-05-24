from Blueprint.Actions.CommonElements.popup_messages_actions import PopUpMessagesActions
from Blueprint.PageObject.UsersAndGroups.available_users_objects import AvailableUsersObjects


class AvailableUsersActions(AvailableUsersObjects):
    """This class represents the users column actions of the Blueprint application"""

    def __init__(self):
        super().__init__()
        self.pop_up_messages = PopUpMessagesActions()

    def create_new_user(self, username: str):
        """Creates a new user with the specified username."""
        self.click_on_new_user_button()
        self.insert_username(username)
        self.click_on_create_user_button()
        self.pop_up_messages = PopUpMessagesActions()

    def insert_user_in_search_user_bar(self, username: str):
        """Inserts the specified username into the search user bar."""
        self.get_input_search_users().clear()
        self.get_input_search_users().send_keys(username)

    def click_on_user_result_add_button(self, index: str = "1"):
        """Clicks on the add button of the user result at the specified index (default: 1)"""
        self.get_user_result_add_button(index).click()

    def click_on_new_user_button(self):
        """Clicks on the 'New User' button"""
        self.get_new_user_button().click()

    def insert_username(self, username: str):
        """Inserts the specified username into the input field"""
        self.get_input_user_name().send_keys(username)

    def click_on_create_user_button(self):
        """Clicks on the create user button"""
        self.get_create_user_button().click()

    def click_on_cancel_user_button(self):
        """Clicks on the cancel user button"""
        self.get_cancel_create_user_button().click()

    def get_pop_up_text_user(self):
        """Returns the text of the pop-up message displayed."""
        text = self.pop_up_messages.get_popup_message_text()
        return text

    def close_pop_up(self):
        """Clicks on 'X' button of the popup message"""
        self.pop_up_messages.click_to_close_popup_message()
