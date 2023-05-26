from Blueprint.PageObject.MainMenu.main_menu_objects import MainMenuObjects


class MainMenuActions(MainMenuObjects):
    """This class represents the main menu actions of the Blueprint application"""

    def click_on_my_inbox_button(self):
        """Clicks on the 'My Inbox' button in the Main Menu."""
        self.get_my_inbox_button().click()

    def click_on_projects_button(self):
        """Clicks on the 'Projects' button in the Main Menu."""
        self.get_projects_button().click()

    def insert_project_name_into_the_search_bar(self, name: str):
        """Inserts the provided project name into the search bar."""
        self.get_search_projects_input().clear()
        self.get_search_projects_input().send_keys(name)

    def click_on_a_project_result(self, index: str = "1"):
        """Clicks on a project result by index (default: 1)"""
        self.get_project_result(index).click()

    def click_on_reports_button(self):
        """Clicks on the 'Reports' button in the Main Menu."""
        self.get_reports_button().click()

    def click_on_flows_button(self):
        """Clicks on the 'Flows' button in the Main Menu."""
        self.get_flows_button().click()

    def insert_flow_name_into_the_search_bar(self, name: str):
        """Inserts the provided flow name into the search input."""
        self.get_search_flows_input().clear()
        self.get_search_flows_input().send_keys(name)

    def click_on_first_flow_result(self, index: str = "1"):
        """Clicks on a flow result by index (default: 1)"""
        self.get_flow_result(index).click()

    def click_on_users_and_groups_button(self):
        """Clicks on the 'Users and Groups' button in the Main Menu."""
        self.get_users_and_groups_button().click()

    def click_on_new_flow_button(self):
        """Clicks on the 'New Flow' button in the Main Menu."""
        self.get_new_flow_button().click()
