from Blueprint.PageObject.MainMenu.main_menu_objects import MainMenuObjects


class MainMenuActions(MainMenuObjects):
    """This class represents the main menu actions of the Blueprint application"""

    def click_on_my_inbox(self):
        """Clicks on the 'My Inbox' button."""
        self.get_my_inbox_button().click()

    def click_on_projects_button(self):
        """Clicks on the 'Projects' button."""
        self.get_projects_button().click()

    def insert_project_name(self, name: str):
        """Inserts the provided project name into the search input."""
        self.get_search_projects_input().send_keys(name)

    def click_on_first_project_result(self):
        """Clicks on the first project result."""
        self.get_first_project_result().click()

    def click_on_reports_button(self):
        """Clicks on the 'Reports' button."""
        self.get_reports_button().click()

    def click_on_flows_button(self):
        """Clicks on the 'Flows' button."""
        self.get_flows_button().click()

    def insert_flow_name(self, name: str):
        """Inserts the provided flow name into the search input."""
        self.get_search_flows_input().send_keys(name)

    def click_on_first_flow_result(self):
        """Clicks on the first flow result."""
        self.get_first_flow_result().click()

    def click_on_users_and_groups_button(self):
        """Clicks on the 'Users and Groups' button."""
        self.get_users_and_groups_button().click()
