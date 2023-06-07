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

    def get_flows_button_label(self) -> str:
        """Gets the label of 'Flows' button in the Main Menu."""
        label = self.get_flows_button().text
        return label

    def insert_flow_name_into_the_search_bar(self, name: str):
        """Inserts the provided flow name into the search input."""
        self.get_search_flows_input().clear()
        self.get_search_flows_input().send_keys(name)

    def click_on_flow_result(self, index: str = "1"):
        """Clicks on a flow result by index (default: 1)"""
        self.get_flow_result(index).click()

    def click_on_users_and_groups_button(self):
        """Clicks on the 'Users and Groups' button in the Main Menu."""
        self.get_users_and_groups_button().click()

    def go_to_project_process_in_main_menu(self, project_name: str):
        """Goes to a specific project"""
        self.click_on_projects_button()
        self.insert_project_name_into_the_search_bar(project_name)
        self.click_on_a_project_result()
        self.click_on_projects_button()

    def go_to_flow_process_in_main_menu(self, flow_name: str):
        """Goes to a specific flow"""
        self.click_on_flows_button()
        self.insert_flow_name_into_the_search_bar(flow_name)
        self.click_on_flow_result()
        self.click_on_flows_button()

    def get_no_data_match_found_message_text(self) -> str:
        """Returns the text of the message 'No data match found'."""
        message = self.get_no_data_match_found_message().text
        return message
