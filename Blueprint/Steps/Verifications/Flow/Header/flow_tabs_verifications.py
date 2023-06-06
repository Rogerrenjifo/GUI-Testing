from Blueprint.Steps.Actions.Flows.header_actions import HeaderActions
from Libraries.Assertions.assertions import Verification


class FlowTabsVerifications:
    """This class represents the verifications of the flow tabs"""
    def __init__(self):        
        self.header = HeaderActions()
        self.verification = Verification()

    def tab_bar_should_be_displayed(self, tab_name: str):
        """Verifies that the tab bar is displayed in the header."""        
        self.verification.verify_element_is_displayed(self.header.get_tab(tab_name))

    def tab_icon_should_be_displayed(self, tab_name: str):
        """Verifies that the tab icon is displayed in the header."""        
        self.verification.verify_element_is_displayed(self.header.get_icon(tab_name))

    def flow_tab_should_be_marked(self, tab_name: str):
        """Verifies that a flow tab is marked"""
        marked_tab = self.header.get_marked_tab_in_flow_header(tab_name)
        self.verification.verify_result_is_true(marked_tab)

    def flow_tab_should_not_be_marked(self, tab_name: str):
        """Verifies that a flow tab is not marked"""
        unmarked_tab = self.header.get_unmarked_tab_in_flow_header(tab_name)
        self.verification.verify_result_is_true(unmarked_tab)
