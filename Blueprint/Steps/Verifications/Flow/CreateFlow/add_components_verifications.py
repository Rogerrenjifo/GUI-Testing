from selenium.webdriver.remote.webelement import WebElement
from Blueprint.PageObject.Flows.flow_main_panel_object import FlowMainPanelObject
from Blueprint.PageObject.Flows.flow_components_object import FlowComponentObjects
from Libraries.Assertions.assertions import Verification


class AddComponentsVerification:
    """This class contains the method to verify the actions of flow main panel."""

    def __init__(self) -> None:
        self.verification = Verification()
        self.main_panel = FlowMainPanelObject()
        self.component = FlowComponentObjects()

    def the_component_should_be_added_to_the_main_board(self, step_id: str) -> None:
        """Verifies the component were added to canvas board."""
        elements_ids = self.main_panel.generate_components_ids()
        self.verification.verify_a_list_contain(elements_ids, step_id)

    def the_component_should_not_be_added_to_the_main_board(self, step_id: str) -> None:
        """Verifies the component were not added to canvas board."""
        elements_ids = self.main_panel.generate_components_ids()
        self.verification.verify_a_list_does_not_contain(elements_ids, step_id)

    def the_component_should_be_on_the_main_board(self, step_id: str) -> None:
        """Verifies the component were added to canvas board."""
        try:
            element = self.main_panel.find_element.by_id(step_id)
        except Exception:
            element = None
        self.verification.verify_the_element_exist(element, WebElement)

    def the_component_should_not_be_on_the_main_board(self, step_id: str) -> None:
        """Verifies the component were added to canvas board."""
        try:
            element = self.main_panel.find_element.by_id(step_id)
        except Exception:
            element = None
        self.verification.verify_equal_ignore(element, None)
