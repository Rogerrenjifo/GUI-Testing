from Blueprint.PageObject.MainMenu.main_menu_objects import MainMenuObjects


class MainMenuActions(MainMenuObjects):
    """This class represents the login page of a Blueprint application"""

    def click_on_projects_button(self):
        self.get_projects_button().click()

    def get_projects_results_list(self):
        self.get_projects_results()
