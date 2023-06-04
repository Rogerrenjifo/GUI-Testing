from Blueprint.Steps.Actions.CommonElements.popup_messages_actions import PopUpMessagesActions
from Blueprint.PageObject.Flows.create_form_elements_objects import CreateFormElementsObjects
from Blueprint.PageObject.Flows.create_form_main_panel_objects import FormMainPanelPage
from Blueprint.PageObject.Flows.header_objects import Header
from Blueprint.PageObject.MainMenu.main_menu_objects import MainMenuObjects
from Blueprint.PageObject.Flows.Elements.FormElements.form_elements_storage import FormElementsStorage
from selenium.webdriver.remote.webelement import WebElement


class CreateFormElementsActions(CreateFormElementsObjects):
    """This class represents the create form elements of a Blueprint application"""
    def __init__(self):
        super().__init__()
        self.main_panel = FormMainPanelPage()
        self.pop_up_messages = PopUpMessagesActions()
        self.header = Header()
        self.main_menu = MainMenuObjects()
        self.element_storage = FormElementsStorage()
        self.sections_list = self.element_storage.sections_list
        self.components_in_section = self.element_storage.components_in_sections

    def select_component_type_in_create_form(self, component_type: str) -> WebElement:
        """Returns the element according the type selected"""
        components = {
            "textbox": self.get_input_text_element(),
            "date": self.get_input_date_element(),
            "checkbox": self.get_input_checkbox_element(),
            "dropdown": self.get_input_dropdown_element(),
            "multilinebox": self.get_input_multiline_element(),
            "numericbox": self.get_input_numbers_element(),
            "userlist": self.get_input_user_list_element()
        }
        return components.get(component_type)

    def add_component_to_column_section_in_create_form(self, component_type: str, section_column_id: str, component_number: str = "1"):
        """Adds a new element in a section form column, according the selected type"""
        section = self.main_panel.get_section_column(section_column_id)
        component = self.select_component_type_in_create_form(component_type)
        self.action_chains.custom_drag_and_drop(component, section)
        section = "-".join(section_column_id.split("-")[0:2])
        self.element_storage.add_component_to_section(component_type, section, component_number)

    def add_component_down_existent_component_in_create_form(self, component_type: str, existent_component_id: str, component_number: str = "1"):
        """Adds a new element under an existing one, according to the selected type"""
        target = self.main_panel.get_component(existent_component_id)
        source = self.select_component_type_in_create_form(component_type)
        self.action_chains.drag_and_drop_element(source, target)
        self.element_storage.add_component_to_section(component_type, existent_component_id, component_number)

    def add_component_up_to_existent_component_in_create_form(self, component_type: str, existent_component_id: str, component_number: str = "1"):
        """Adds a new element on top of an existing one, according to the selected type"""
        target = self.main_panel.get_component(existent_component_id)
        source = self.select_component_type_in_create_form(component_type)
        self.action_chains.custom_drag_and_drop(source, target, direction="up")
        if existent_component_id != 'section-1_textbox-1':
            self.element_storage.add_component_to_section(component_type, existent_component_id, component_number)

    def add_new_section_in_create_form(self):
        """Adds a new section at the end of a form"""
        target = self.main_panel.get_section(self.element_storage.get_sections_title()[-1])
        source = self.get_section_element()
        self.action_chains.drag_and_drop_element(source, target)
        self.element_storage.add_section()

    def add_section_up_other_in_create_form(self, existing_section_title: str):
        """Adds a new section on top of an existing one"""
        existing_section_index = self.element_storage.get_section_index(existing_section_title)
        source = self.get_section_element()
        target = self.main_panel.get_section_dropdown(existing_section_title)
        self.action_chains.custom_drag_and_drop(source, target, direction="up")
        self.element_storage.add_section("up", existing_section_index)

    def add_section_down_other_in_create_form(self, existing_section_title: str):
        """Adds a new section under an existing one"""
        existing_section_index = self.element_storage.get_section_index(existing_section_title)
        source = self.get_section_element()
        target = self.main_panel.get_section(existing_section_title)
        self.action_chains.custom_drag_and_drop(source, target)
        self.element_storage.add_section("down", existing_section_index)

    def close_pop_up_on_create_form_elements(self):
        """Selects the button for close the popup message"""
        self.pop_up_messages.click_to_close_popup_message()

    def obtain_pop_up_text_on_create_form_elements(self) -> str:
        """Gets the text displayed in the popup message"""
        pop_up_content = self.pop_up_messages.get_popup_message_text()
        return pop_up_content

    def obtain_pop_up_rgb_color_on_create_form_elements(self) -> str:
        """Gets the rgb color of the displayed popup message"""
        rgb_pop_up_color = self.pop_up_messages.get_popup_message_color()
        return rgb_pop_up_color

    def add_new_section_in_flow_page_header(self):
        """Adds a new section at page header"""
        target = self.header.get_flow_name()
        source = self.get_section_element()
        self.action_chains.drag_and_drop_element(source, target)

    def add_new_section_in_page_menu(self):
        """Adds a new section at page menu"""
        target = self.main_menu.get_main_menu_container()
        source = self.get_section_element()
        self.action_chains.drag_and_drop_element(source, target)

    def select_section_and_add_component_to_section_in_create_form(self, component_type: str, section_column_id: str, component_number: str = "1"):
        """CLicks on a section and adds a new component in a section form column, according the selected type"""
        self.main_panel.get_section_column(section_column_id).click()
        self.add_component_to_column_section_in_create_form(component_type, section_column_id, component_number)

    def add_new_component_in_flow_page_header(self, component_type: str):
        """Adds a new section at page header"""
        target = self.header.get_flow_name()
        source = self.select_component_type_in_create_form(component_type)
        self.action_chains.drag_and_drop_element(source, target)

    def add_new_component_in_page_menu(self, component_type: str):
        """Adds a new section at page menu"""
        target = self.main_menu.get_main_menu_container()
        source = self.select_component_type_in_create_form(component_type)
        self.action_chains.drag_and_drop_element(source, target)

    def add_component_in_main_panel_in_create_form(self, component_type: str):
        """Tries to add a new component in the main panel"""
        main_panel = self.get_drop_area()
        component = self.select_component_type_in_create_form(component_type)
        self.action_chains.custom_drag_and_drop(component, main_panel)
