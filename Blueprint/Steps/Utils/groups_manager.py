import time
from Blueprint.Steps.Actions.UsersAndGroups.groups_actions import GroupsActions
from Blueprint.Steps.Actions.UsersAndGroups.available_users_actions import AvailableUsersActions
from Blueprint.Steps.Actions.MainMenu.main_menu_actions import MainMenuActions


class GroupManager:
    """Manages actions and verifications in main menu"""
    def __init__(self):
        self.group = GroupsActions()
        self.user = AvailableUsersActions()
        self.main_menu = MainMenuActions()

    def create_group_if_not_exist(self, group_name: str, users_list: list):
        """Tries to create a group, and adds users if the group is created"""
        self.main_menu.click_on_users_and_groups_button()
        self.group.create_new_group(group_name)
        if self.group.get_pop_up_text_created_group() == "Group Created":
            time.sleep(3)
            self.user.add_users_searched_in_a_group(users_list)
        time.sleep(3)
