import time
from robot.api import logger
from Blueprint.PageObject.Flows.create_form_main_panel_objects import FormMainPanelPage


class FormMainPanelActions(FormMainPanelPage):
    """Represents the main panel actions of create form tab in flow page"""

    def select_component_in_form_main_panel(self, component_id: str):
        """Clicks a component from main panel for display its properties"""
        self.get_component(component_id).click()

    def select_section_in_form_main_panel(self, section_title: str):
        """Clicks a section from main panel for display its properties"""
        self.get_section(section_title).click()

    def move_component_between_sections_in_form_main_panel(self, component_id: str, column_id: str):
        """Moves a component from a section to other"""
        source = self.get_component(component_id)
        target = self.get_section_column(column_id)
        self.action_chains.drag_and_drop_element(source, target)

    def move_section_up_other_in_form_main_panel(self, source_section_title: str, target_section_title: str,
                                                 source_index=None, target_index=None):
        """Moves a section above another section"""
        source = self.get_section(source_section_title, source_index)
        target = self.get_section(target_section_title, target_index)
        self.action_chains.custom_drag_and_drop(source, target, direction="up")

    def move_section_down_other_in_form_main_panel(self, source_section_title: str, target_section_title: str,
                                                   source_index=None, target_index=None):
        """Moves a section below another section"""
        source = self.get_section(source_section_title, source_index)
        target = self.get_section(target_section_title, target_index)
        self.action_chains.custom_drag_and_drop(source, target)

    def move_component_up_other_in_form_main_panel(self, source_component_id: str, target_component_id: str):
        """Moves a component above another component"""
        source = self.get_component(source_component_id)
        target = self.get_component(target_component_id)
        self.action_chains.custom_drag_and_drop(source, target, direction="up")

    def move_component_down_other_in_form_main_panel(self, source_component_id: str, target_component_id: str):
        """Moves a component below another component"""
        source = self.get_component(source_component_id)
        target = self.get_component(target_component_id)
        self.action_chains.custom_drag_and_drop(source, target)

    def delete_section_in_form_main_panel(self, section_title: str, index=None):
        """Deletes a section from its drop-down menu"""
        self.display_section_delete_menu_in_form_main_panel(section_title, index)
        self.select_section_delete_button_in_form_main_panel()

    def delete_component_in_form_main_panel(self, component_id):
        """Deletes a component from its drop-down menu"""
        self.display_component_delete_menu_in_form_main_panel(component_id)
        self.select_component_delete_button_in_form_main_panel(component_id)

    def display_section_delete_menu_in_form_main_panel(self, section_title: str, index=None):
        """Clicks drop-down button, if it does not display, clicks on its corner"""
        drop_down_button = self.get_section_dropdown(section_title, index)
        self.action_chains.move_to_an_element(drop_down_button)
        drop_down_button.click()
        display_drop_down_menu = drop_down_button.get_attribute("aria-expanded")
        if display_drop_down_menu.lower() == "false":
            logger.info("Clicking on middle drop-down button failed, "
                        "It will try clicking on one side of the button")
            self.action_chains.custom_click_element(drop_down_button)
        time.sleep(2)

    def display_component_delete_menu_in_form_main_panel(self, component_id: str):
        """Displays component drop-down menu from its 3 dots button"""
        self.action_chains.move_to_an_element(self.get_component_dropdown(component_id))
        self.get_component_dropdown(component_id).click()
        time.sleep(2)

    def obtain_section_error_message_in_form_main_panel(self, section_title: str, index=None):
        """Returns section error message displayed in main panel"""
        message = self.get_section_error_message(section_title, index).text
        return message

    def obtain_section_title_in_form_main_panel(self, index: str):
        """Returns section title displayed in main panel"""
        section_title = self.get_section_title(index).text
        return section_title

    def obtain_component_title_in_form_main_panel(self, component_id: str):
        """Returns component title displayed in main panel"""
        component_title = self.get_component_title(component_id).text
        return component_title

    def select_section_delete_button_in_form_main_panel(self):
        """Clicks delete button from section drop-down menu"""
        self.get_section_delete_button().click()

    def select_component_delete_button_in_form_main_panel(self, component_id: str):
        """Clicks delete button from component drop-down menu"""
        self.get_component_delete_button(component_id).click()
