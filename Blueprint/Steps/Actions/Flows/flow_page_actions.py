import time
from Blueprint.PageObject.Flows.new_flow import NewFlow
from Libraries.Resources.random_flow_code import random_string_generator
from Blueprint.Steps.Actions.CommonElements.popup_messages_actions import PopUpMessagesActions
from Blueprint.PageObject.Flows.Elements.FormElements.form_elements_storage import FormElementsStorage


class NewFlowActions(NewFlow):
    """This class represents the flow page of a Blueprint application"""
    def __init__(self):
        super().__init__()
        self.pop_up_messages = PopUpMessagesActions()
        self.success_pop_up_rgb_color = "rgba(92, 184, 92, 1)"

    def click_on_flows_drop_down_button(self):
        """Clicks on the 'Flows' drop-down button on the navigation bar."""
        self.get_drop_down_flow_menu().click()

    def click_on_new_flow_button(self):
        """ Clicks on the 'New Flow' button in the 'Flows' drop-down menu."""
        self.get_new_flow_button().click()

    def insert_new_flow_name(self, name: str):
        """Inserts the given name into the 'Code' input field on the 'New Flow' page."""
        self.get_input_new_flow_name().clear()
        self.get_input_new_flow_name().send_keys(name)

    def insert_new_flow_code(self, code: str):
        """Inserts the given code into the 'Code' input field on the 'New Flow' page."""
        self.get_input_new_flow_code().send_keys(code)

    def click_on_create_new_flow_button(self):
        """Clicks on the 'Create' button on the 'New Flow' page."""
        self.get_create_button().click()

    def click_on_cancel_new_flow_button(self):
        """Clicks on the 'Cancel' button on the 'New Flow' page"""
        self.get_cancel_button().click()

    def create_new_flow_process_in_flow_page(self, flow_name: str, flow_code: str):
        """Creates a new flow"""
        self.click_on_flows_drop_down_button()
        self.click_on_new_flow_button()
        self.insert_new_flow_name(flow_name)
        self.insert_new_flow_code(flow_code)
        self.click_on_create_new_flow_button()
        self.click_on_flows_drop_down_button()

    def cancel_create_new_flow_process_in_flow_page(self):
        """Cancels the creation of a new flow"""
        self.click_on_flows_drop_down_button()
        self.click_on_new_flow_button()
        self.click_on_cancel_new_flow_button()

    def create_new_flow_without_name_process_in_flow_page(self, flow_code: str):
        """Tries to create a new flow without name"""
        self.click_on_flows_drop_down_button()
        self.click_on_new_flow_button()
        self.insert_new_flow_code(flow_code)
        self.click_on_create_new_flow_button()

    def create_new_flow_without_code_process_in_flow_page(self, flow_name: str):
        """Tries to create a new flow without code"""
        self.click_on_flows_drop_down_button()
        self.click_on_new_flow_button()
        self.insert_new_flow_name(flow_name)
        self.click_on_create_new_flow_button()

    def create_a_new_flow_with_random_code(self, flow_name: str = "AT19-GUITESTING-"):
        """Creates a new flow with a random code. If the code is in use, tries with other"""
        self.click_on_flows_drop_down_button()
        flow_was_created = False
        while not flow_was_created:
            flow_code = random_string_generator(3)
            flow_name = flow_name + flow_code
            self.click_on_new_flow_button()
            self.insert_new_flow_name(flow_name)
            self.insert_new_flow_code(flow_code)
            self.click_on_create_new_flow_button()
            self.wait_for_element.wait_for_result(self.pop_up_messages.get_popup_message())
            time.sleep(3)
            if self.pop_up_messages.get_popup_messages_text_list()[0] == "Process created":
                flow_was_created = True
                elements_storage = FormElementsStorage()
                elements_storage.add_default_section()
                elements_storage.add_default_component()
                self.click_on_flows_drop_down_button()
            self.pop_up_messages.click_to_close_popup_message()
        return flow_name

    def get_name_field_required_message_text(self) -> str:
        """Returns the text of the required message for the name field."""
        text = self.get_name_field_required_message().text
        return text

    def get_code_field_required_message_text(self) -> str:
        """Returns the text of the required message for the code field"""
        text = self.get_code_field_required_message().text
        return text
