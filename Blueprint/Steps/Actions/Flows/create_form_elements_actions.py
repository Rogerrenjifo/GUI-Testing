from Blueprint.Steps.Actions.CommonElements.popup_messages_actions import PopUpMessagesActions
from Blueprint.PageObject.Flows.create_form_elements_objects import CreateFormElementsObjects
from Blueprint.PageObject.Flows.create_form_main_panel_objects import FormMainPanelPage


class CreateFormElementsActions(CreateFormElementsObjects):
    """This class represents the create form elements of a Blueprint application"""
    def __init__(self):
        super().__init__()
        self.main_panel = FormMainPanelPage()
        self.pop_up_messages = PopUpMessagesActions()

    def select_element_type_in_create_form(self, element_type: str):
        """Returns the element according the type selected"""
        elements = {
            "text": self.get_input_text_element(),
            "date": self.get_input_date_element(),
            "checkbox": self.get_input_checkbox_element(),
            "dropdown": self.get_input_dropdown_element(),
            "multiline": self.get_input_multiline_element(),
            "numbers": self.get_input_numbers_element(),
            "user_list": self.get_input_user_list_element()
        }
        return elements.get(element_type)

    def add_element_to_column_section_in_create_form(self, element_type: str, section_column_id: str):
        """Adds a new element in a section form column, according the selected type"""
        section = self.main_panel.get_section_column(section_column_id)
        element = self.select_element_type_in_create_form(element_type)
        self.action_chains.custom_drag_and_drop(element, section)

    def add_element_down_existent_element_in_create_form(self, element_type: str, existent_element_title: str):
        """Adds a new element under an existing one, according to the selected type"""
        target = self.main_panel.get_component(existent_element_title)
        source = self.select_element_type_in_create_form(element_type)
        self.action_chains.drag_and_drop_element(source, target)

    def add_element_up_to_existent_element_in_create_form(self, element_type: str, existent_element_id: str):
        """Adds a new element on top of an existing one, according to the selected type"""
        target = self.main_panel.get_component(existent_element_id)
        source = self.select_element_type_in_create_form(element_type)
        self.action_chains.custom_drag_and_drop(source, target, direction="up")

    def add_new_section_in_create_form(self):
        """Adds a new section in a form"""
        target = self.get_drop_area()
        source = self.get_section_element()
        self.action_chains.drag_and_drop_element(source, target)

    def add_section_up_other_in_create_form(self, existing_section_title: str):
        """Adds a new section on top of an existing one"""
        source = self.get_section_element()
        target = self.main_panel.get_section_title(existing_section_title)
        self.action_chains.custom_drag_and_drop(source, target, direction="up")

    def add_section_down_other_in_create_form(self, existing_section_title: str):
        """Adds a new section under an existing one"""
        source = self.get_section_element()
        target = self.main_panel.get_section(existing_section_title)
        self.action_chains.custom_drag_and_drop(source, target)

    def close_pop_up_on_create_form_elements(self):
        """Selects the button for close the popup message"""
        self.pop_up_messages.click_to_close_popup_message()

    def obtain_pop_up_text_on_create_form_elements(self) -> str:
        """Gets the text displayed in the popup message"""
        pop_up_content = self.pop_up_messages.get_popup_message_text()
        return pop_up_content

    def obtain_pop_up_color_on_create_form_elements(self) -> str:
        """Gets the color of the displayed popup message"""
        pop_up_color = self.pop_up_messages.get_popup_message_color()
        return pop_up_color
