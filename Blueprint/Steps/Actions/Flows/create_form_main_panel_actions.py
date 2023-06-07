from robot.api import logger
from Blueprint.PageObject.Flows.create_form_main_panel_objects import FormMainPanelPage
from Blueprint.Steps.Actions.CommonElements.popup_messages_actions import PopUpMessagesActions
from Blueprint.PageObject.Flows.Elements.FormElements.form_elements_storage import FormElementsStorage
from Blueprint.PageObject.Flows.create_form_elements_objects import CreateFormElementsObjects
from Blueprint.Steps.Actions.Flows.create_form_properties_panel_actions import PropertiesPanelActions


class FormMainPanelActions(FormMainPanelPage):
    """Represents the main panel actions of create form tab in flow page"""
    def __init__(self):
        super().__init__()
        self.pop_up_messages = PopUpMessagesActions()
        self.element_storage = FormElementsStorage()
        self.sections_list = self.element_storage.sections_list
        self.components_list = self.element_storage.components_in_sections
        self.properties = PropertiesPanelActions()

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
        section_index = self.element_storage.get_section_index(section_title)
        if section_index != 0:
            del self.sections_list[section_index]
            section_key = section_title.lower().replace(" ", "-")
            try:
                del self.components_list[section_key]
            except:
                logger.info(f"Not component in section: {section_key}")
        self.display_section_delete_menu_in_form_main_panel(section_title, index)
        self.select_section_delete_button_in_form_main_panel()

    def delete_component_in_form_main_panel(self, component_id):
        """Deletes a component from its drop-down menu"""
        self.display_component_delete_menu_in_form_main_panel(component_id)
        self.select_component_delete_button_in_form_main_panel(component_id)
        for section in self.components_list:
            try:
                del self.components_list[section][component_id]
            except:
                logger.info(f"Not component in section: {section}")

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

    def display_component_delete_menu_in_form_main_panel(self, component_id: str):
        """Displays component drop-down menu from its 3 dots button"""
        self.action_chains.move_to_an_element(self.get_component_dropdown(component_id))
        self.get_component_dropdown(component_id).click()

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

    def get_all_sections_title_in_form_main_panel(self) -> list:
        """Returns all the sections title displayed in main panel"""
        sections_title_list = []
        for section_index in range(1, len(self.get_all_sections())+1):
            sections_title_list.append(self.get_section_title(str(section_index)).text)
        return sections_title_list

    def get_all_components_title_in_a_section_in_form_main_panel(self, section_title: str = "section-1") -> list:
        """Returns all the components title displayed in a section"""
        components_title_list = []
        for component in self.get_all_components_in_a_section(section_title):
            components_title_list.append(component.text)
        return components_title_list

    def click_on_close_button_in_form_main_panel_popup_message(self):
        """Selects the button for close the popup message"""
        self.pop_up_messages.click_to_close_popup_message()

    def obtain_text_of_form_main_panel_pop_up_message(self):
        """Gets the text displayed in the popup message"""
        pop_up_content = self.pop_up_messages.get_popup_message_text()
        return pop_up_content

    def obtain_rgb_color_of_form_main_panel_pop_up_message(self):
        """Gets the RGB color of the popup message background"""
        pop_up_rgb_color = self.pop_up_messages.get_popup_message_color()
        return pop_up_rgb_color

    def obtain_section_error_message_rgb_color_in_form_main_panel(self, section_title: str, index=None):
        """Gets the RGB color of the error message"""
        rgb_color = self.get_section_error_message(section_title, index).value_of_css_property('color')
        return rgb_color

    def obtain_section_rgb_color_in_form_main_panel(self, index: str):
        """Gets the RGB color of the section title"""
        rgb_color = self.get_section_title(index).value_of_css_property('color')
        return rgb_color

    def delete_all_sections_created_in_form_main_panel(self):
        """Deletes all the sections in form main panel, except the default one"""
        section_list_to_delete = self.element_storage.get_sections_title()[1:]
        for section in section_list_to_delete:
            self.delete_section_in_form_main_panel(section)

    def delete_components_added_in_section_in_form_main_panel(self, section: str = "section-1"):
        """Deletes all the components created in a section"""
        components_list_to_delete = list(self.components_list[section].keys())
        for component in components_list_to_delete:
            if component != "section-1_textbox-1":
                self.delete_component_in_form_main_panel(component)

    def delete_components_and_sections_added_in_form_main_panel(self):
        """Deletes all the components and sections created in form main panel"""
        section_list = self.element_storage.get_sections_title()
        for section in section_list:
            if section != "Section 1":
                self.delete_section_in_form_main_panel(section)
            else:
                section = section.lower().replace(" ", "-")
                self.delete_components_added_in_section_in_form_main_panel(section)

    def hover_section_in_form_main_panel(self, section_title: str):
        """Moves to a section in form main panel"""
        self.action_chains.move_to_an_element(self.get_section(section_title))

    def hover_component_in_form_main_panel(self, component_id: str):
        """Moves to a component in form main panel"""
        self.action_chains.move_to_an_element(self.get_component(component_id))

    def move_component_in_main_panel_in_create_form(self, component_id: str):
        """Tries to move a component in the main panel"""
        main_panel = CreateFormElementsObjects().get_drop_area()
        component = self.get_component(component_id)
        self.action_chains.custom_drag_and_drop(component, main_panel)

    def get_all_components_type_in_a_section_in_form_main_panel(self, section_title: str = "section-1") -> list:
        """Returns all the components types displayed in properties panel"""
        components_type_list = []
        if section_title == "section-1":
            components_in_section = self.get_all_components_in_a_section(section_title)[1:]
        else:
            components_in_section = self.get_all_components_in_a_section(section_title)
        for component in components_in_section:
            component.click()
            self.wait_for_element.wait_for_element_with_web_element(self.properties.get_field_type_select())
            components_type_list.append(self.properties.get_field_type_select().text)
        return components_type_list

    def delete_form_storage(self):
        """Clean the elements storage in create form tab"""
        self.element_storage.components_in_sections = {}
        self.element_storage.sections_list = []
