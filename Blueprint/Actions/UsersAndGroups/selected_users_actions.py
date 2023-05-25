from Blueprint.Actions.CommonElements.popup_messages_actions import PopUpMessagesActions
from Blueprint.PageObject.UsersAndGroups.selected_users_objects import SelectedUsersObjects


class SelectedUsersActions(SelectedUsersObjects):
    """This class represents the selected users column actions of the Blueprint application"""
    def __init__(self):
        super().__init__()
        self.pop_up_messages = PopUpMessagesActions()

    def insert_username_into_the_search_selected_bar(self, username: str):
        """Inserts the specified username into the search selected bar"""
        self.get_input_search_selected().clear()
        self.get_input_search_selected().send_keys(username)

    def click_on_remove_selected_user(self, index: str = "1"):
        """Clicks on the remove button for the selected user at the specified index (default: 1)"""
        self.get_selected_user_remove_button(index).click()

    def get_pop_up_text_user(self):
        """Returns the text of the pop-up message displayed."""
        text = self.pop_up_messages.get_popup_message_text()
        return text

    def close_pop_up(self):
        """Clicks on 'X' button of the popup message"""
        self.pop_up_messages.click_to_close_popup_message()
