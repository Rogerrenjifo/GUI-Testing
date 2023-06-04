from Blueprint.Steps.Actions.Flows.header_actions import HeaderActions
from Libraries.Assertions.assertions import Verification


class HeaderVerifications:
    """This class represents the verifications of the Flow Header"""
    def __init__(self):        
        self.header = HeaderActions()
        self.verification = Verification()

    def flow_status_should_be_displayed(self):
        """Verifies that the status of the flow is displayed in the header."""        
        self.verification.element_should_be_displayed(self.header.get_flow_status())

    def flow_version_should_be_displayed(self):
        """Verifies that the version of the flow is displayed in the header."""        
        self.verification.element_should_be_displayed(self.header.get_flow_version())

    def flow_name_should_be_displayed(self):
        """Verifies that the name of the flow is displayed in the header."""        
        self.verification.element_should_be_displayed(self.header.get_flow_name())

    def dropdown_button_should_be_displayed(self):
        """Verifies that the dropdown button is displayed in the header."""        
        self.verification.element_should_be_displayed(self.header.get_dropdown_button())

    def flow_last_updated_text_should_be_displayed(self):
        """Verifies that last updated text of the flow is displayed in the header."""        
        self.verification.element_should_be_displayed(self.header.get_last_updated())
    
    def save_button_should_be_displayed(self):
        """Verifies that the save button is displayed in the header."""        
        self.verification.element_should_be_displayed(self.header.get_save_button())
    
    def save_button_color_should_be_equal(self, expected_color :str):
        """Verifies that the save button is displayed in the expected color"""
        actual_color = self.header.obtain_save_button_rgb_color_in_flow_header()
        self.verification.verify_equal_ignore(actual_color, expected_color)

    def save_next_button_should_be_displayed(self):
        """Verifies that the save & next button is displayed in the header."""        
        self.verification.element_should_be_displayed(self.header.get_save_next_button())

    def save_next_button_color_should_be_equal(self, expected_color :str):
        """Verifies that the save button is displayed in the expected color"""
        actual_color = self.header.obtain_save_next_button_rgb_color_in_flow_header()
        self.verification.verify_equal_ignore(actual_color, expected_color)
