import time
import random

from Blueprint.Steps.Actions.MainMenu.main_menu_actions import MainMenuActions
from Blueprint.Steps.Actions.Projects.ProjectPage.project_page_actions import ProjectPageActions
from Blueprint.Steps.Actions.Projects.new_project_actions import NewProjectActions


class InstanceManager:
    def __init__(self):
        self.main_menu = MainMenuActions()
        self.project_page = ProjectPageActions()
        self.new_project = NewProjectActions()

    def create_list_of_project_instance(self, project_name: str, number_of_instances: int):
        """Creates a list of projects with just a title and section"""
        for i in range(number_of_instances):
            time.sleep(3)
            self.main_menu.go_to_project_process_in_main_menu(project_name)
            self.project_page.click_on_new_request_button()
            self.new_project.insert_text_or_number_in_a_component_in_new_project_page(
                "Section 1", "Title", f"Project to delete {i+1}")
            self.new_project.click_create_button_in_new_project_page()
        time.sleep(3)
        self.main_menu.go_to_project_process_in_main_menu(project_name)

    def delete_list_of_instances(self, instance_ids: list):
        """Deletes a list of instances"""
        if len(instance_ids) != 0:
            for instance_id in instance_ids:
                time.sleep(5)
                self.project_page.delete_project_instance_process_in_project_page(instance_id)

    def obtain_random_id(self, instance_ids: list):
        """Obtains a random id from a given list of ids"""
        list_length = len(instance_ids)
        index = random.randint(0, list_length-1)
        return instance_ids[index]
