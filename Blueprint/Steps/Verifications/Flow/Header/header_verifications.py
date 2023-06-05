from Blueprint.Steps.Actions.Flows.header_actions import HeaderActions
from Libraries.Assertions.assertions import Verification


class HeaderVerifications:
    """This class represents the verifications of the Flow Header"""
    def __init__(self):        
        self.header = HeaderActions()
        self.verification = Verification()

    def flow_status_should_be_displayed(self):
        """Verifies that the status of the flow is displayed in the header."""        
        self.verification.verify_element_is_displayed(self.header.get_flow_status())

    def flow_version_should_be_displayed(self):
        """Verifies that the version of the flow is displayed in the header."""        
        self.verification.verify_element_is_displayed(self.header.get_flow_version())

    def flow_name_should_be_displayed(self):
        """Verifies that the name of the flow is displayed in the header."""        
        self.verification.verify_element_is_displayed(self.header.get_flow_name())

    def dropdown_button_should_be_displayed(self):
        """Verifies that the dropdown button is displayed in the header."""        
        self.verification.verify_element_is_displayed(self.header.get_dropdown_button())

    def delete_option_should_be_displayed(self):
        """Verifies that 'Delete' option from the dropdown menu is displayed."""        
        self.verification.verify_element_is_displayed(self.header.get_delete_option())

    def select_version_option_should_be_displayed(self):
        """Verifies that 'Select Version' option from the dropdown menu is displayed."""        
        self.verification.verify_element_is_displayed(self.header.get_select_version_option())

    def version_list_should_be_displayed(self):
        """Verifies that the version list from the dropdown menu is displayed."""
        self.verification.verify_element_is_displayed(self.header.get_version_list())

    def flow_version_should_be_equal(self, expected_version :str):
        """Verifies that the flow version displayed is the expected."""        
        actual_version = self.header.get_flow_version_text_in_flow_header()
        self.verification.verify_equal_ignore(actual_version, expected_version.capitalize())

    def flow_last_updated_text_should_be_displayed(self):
        """Verifies that last updated text of the flow is displayed in the header."""        
        self.verification.verify_element_is_displayed(self.header.get_last_updated())
    
    def save_button_should_be_displayed(self):
        """Verifies that the save button is displayed in the header."""        
        self.verification.verify_element_is_displayed(self.header.get_save_button())
    
    def save_button_color_should_be_equal(self, expected_color :str):
        """Verifies that the save button is displayed in the expected color"""
        actual_color = self.header.obtain_save_button_rgb_color_in_flow_header()
        self.verification.verify_equal_ignore(actual_color, expected_color)

    def save_next_button_should_be_displayed(self):
        """Verifies that the save & next button is displayed in the header."""        
        self.verification.verify_element_is_displayed(self.header.get_save_next_button())

    def save_next_button_color_should_be_equal(self, expected_color :str):
        """Verifies that the save button is displayed in the expected color"""
        actual_color = self.header.obtain_save_next_button_rgb_color_in_flow_header()
        self.verification.verify_equal_ignore(actual_color, expected_color)

    def flow_tab_should_be_marked(self, tab_name :str):
        """Verifies that a flow tab is marked"""
        marked_tab = self.header.get_marked_tab_in_flow_header(tab_name)
        self.verification.verify_result_is_true(marked_tab)

    def flow_tab_should_not_be_marked(self, tab_name :str):
        """Verifies that a flow tab is not marked"""
        unmarked_tab = self.header.get_unmarked_tab_in_flow_header(tab_name)
        self.verification.verify_result_is_true(unmarked_tab)
