import time

from Blueprint.Actions.CommonElements.popup_messages_actions import PopUpMessagesActions
from Blueprint.PageObject.UsersAndGroups.groups_objects import GroupsObjects
from robot.api import logger


class GroupsActions(GroupsObjects):
    """This class represents the actions of the groups column of the Blueprint application"""
    def __init__(self):
        super().__init__()
        self.pop_up_messages = PopUpMessagesActions()

    def create_new_group(self, name: str):
        """Creates a new group with the specified name."""
        self.click_on_new_group_button()
        self.insert_group_name(name)
        self.click_on_primary_button()

    def edit_group(self, name: str, new_name: str, index: str = "1"):
        """Edits an existing group with the specified name by changing it to a new name."""
        self.insert_search_in_groups_search_bar(name)
        self.click_on_dropdown_button_of_a_group_result(index)
        self.click_on_edit_button_of_a_group_result(index)
        self.get_input_group_name().clear()
        self.insert_group_name(new_name)
        self.click_on_primary_button()

    def delete_group(self, name: str, index: str = "1"):
        """Deletes an existing group with the specified name."""
        self.insert_search_in_groups_search_bar(name)
        self.click_on_dropdown_button_of_a_group_result(index)
        self.click_on_delete_button_of_a_group_result(index)
        self.click_on_primary_button()

    def click_on_new_group_button(self):
        """Clicks on the 'New Group' button."""
        self.get_new_group_button().click()

    def insert_group_name(self, name: str):
        """Inserts the specified group name into the input field."""
        self.get_input_group_name().send_keys(name)

    def click_on_primary_button(self):
        """Clicks on the 'Create', 'Update' or 'Delete' button."""
        self.get_create_group_button().click()

    def click_on_cancel_button(self):
        """Clicks on the cancel button in any groups page."""
        self.get_cancel_create_group_button().click()

    def insert_search_in_groups_search_bar(self, search: str):
        """Inserts the specified search string into the groups search bar."""
        self.get_input_search_groups().clear()
        self.get_input_search_groups().send_keys(search)

    def click_on_group_result(self, index: str = "1"):
        """Clicks on the first group result displayed, first by default."""
        self.get_group_result(index).click()

    def click_on_dropdown_button_of_a_group_result(self, index: str = "1"):
        """Clicks on a dropdown button group result, if it does not display, clicks on its corner, first by default."""
        self.get_group_result_dropdown_menu(index).click()
        if not self.get_group_result_edit_button(index).is_displayed():
            logger.info("Clicking on the middle of the drop-down button failed, \
                        I will try to click on one side of this tricky button...")
            self.action_chains.custom_click_element(self.get_group_result_dropdown_menu(index))
        time.sleep(2)

    def click_on_edit_button_of_a_group_result(self, index: str = "1"):
        """Clicks on the edit button of the first group result, first by default."""
        self.get_group_result_edit_button(index).click()

    def click_on_delete_button_of_a_group_result(self,  index: str = "1"):
        """Clicks on the delete button of the first group result, first by default."""
        self.get_group_result_delete_button(index).click()

    def get_pop_up_text_created_group(self):
        """Returns the text of the pop-up message displayed."""
        text = self.pop_up_messages.get_popup_message_text()
        return text

    def close_pop_up(self):
        """Clicks on 'X' button of the popup message"""
        self.pop_up_messages.click_to_close_popup_message()
