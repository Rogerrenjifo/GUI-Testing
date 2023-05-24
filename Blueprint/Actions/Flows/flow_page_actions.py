from Blueprint.PageObject.Flows.new_flow import NewFlow


class NewFlowActions(NewFlow):
    """This class represents the flow page of a Blueprint application"""
    def click_on_flows_drop_down_button(self):
        """Clicks on the 'Flows' drop-down button on the top navigation bar."""
        self.get_drop_down_flow_menu().click()

    def click_on_new_flow_button(self):
        """ Clicks on the 'New Flow' button in the 'Flows' drop-down menu."""
        self.get_new_flow_button().click()

    def insert_new_flow_name(self, name: str):
        """Inserts the given name into the 'Code' input field on the 'New Flow' page."""
        self.get_input_new_flow_name().send_keys(name)

    def insert_new_flow_code(self, code: str):
        """Inserts the given code into the 'Code' input field on the 'New Flow' page."""
        self.get_input_new_flow_code().send_keys(code)

    def click_on_create_button(self):
        """Clicks on the 'Create' button on the 'New Flow' page."""
        self.get_create_button().click()

    def click_on_cancel_button(self):
        """Clicks on the 'Cancel' button on the 'New Flow' page"""
        self.get_cancel_button().click()

    def create_new_flow_process(self, flow_name: str, flow_code: str):
        """Creates a new flow"""
        self.click_on_flows_drop_down_button()
        self.click_on_new_flow_button()
        self.insert_new_flow_name(flow_name)
        self.insert_new_flow_code(flow_code)
        self.click_on_create_button()

    def cancel_create_new_flow_process(self, flow_name: str, flow_code: str):
        """Cancel the creation of a new flow"""
        self.click_on_flows_drop_down_button()
        self.click_on_new_flow_button()
        self.click_on_cancel_button()

    def create_new_flow_without_name_process(self, flow_code: str):
        """Tries to create a new flow without name"""
        self.click_on_flows_drop_down_button()
        self.click_on_new_flow_button()
        self.insert_new_flow_code(flow_code)
        self.click_on_create_button()

    def create_new_flow_without_code_process(self, flow_name: str):
        """Tries to create a new flow without code"""
        self.click_on_flows_drop_down_button()
        self.click_on_new_flow_button()
        self.insert_new_flow_name(flow_name)
        self.click_on_create_button()
