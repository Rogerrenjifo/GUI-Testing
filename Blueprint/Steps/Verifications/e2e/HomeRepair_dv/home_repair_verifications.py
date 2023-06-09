from time import sleep
from Blueprint.Steps.Actions.Flows.flow_page_actions import NewFlowActions
from Blueprint.Steps.Actions.Flows.header_actions import HeaderActions
from Libraries.Drivers.base_page import BasePage
from Libraries.Assertions.assertions import Verification
from Blueprint.Locators.Flows import flow_components_locators as locators


class HomeRepairVerifications(BasePage):
    """Class to perform verifications"""
    def __init__(self):
        super().__init__()
        self.assertion = Verification()
        self.header = HeaderActions()

    def action_component_should_be_visible_in_flow_panel(self, component_title: str = None):
        """Verifies if action component is on the flow panel."""
        sleep(1)
        xpath = locators.FLOW_COMPONENT_TITLE.replace("<<title>>", component_title)
        element = self.find_element.by_xpath(xpath)
        self.assertion.verify_element_is_displayed(element)

    def step_component_should_be_visible_in_flow_panel(self, component_title: str = None):
        """Verifies if step component is on the flow panel."""
        sleep(1)
        xpath = locators.FLOW_COMPONENT_TITLE.replace("<<title>>", component_title)
        element = self.find_element.by_xpath(xpath)
        self.assertion.verify_element_is_displayed(element)

    def page_header_title_shoul_be_flow_title(self, expected_title: str = None):
        """Verifies that the page header title is the same as the flow title."""
        actual_title = self.header.get_flow_name_text_in_flow_header()
        self.assertion.verify_equal_ignore(actual_title, expected_title)

