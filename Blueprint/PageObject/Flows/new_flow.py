from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Flows import flows_page_locators as locators
from Libraries.Drivers.base_page import BasePage


class NewFlow(BasePage):
    """This class represents the login page of a Blueprint application"""

    def __init__(self):
        super().__init__()

    def get_drop_down_flow_menu(self) -> WebElement:
        """Finds and returns the drop-down flow menu element of the page."""
        element = self.find_element.by_xpath(locators.DROP_DOWN_FLOW_MENU)
        return element

    def get_new_flow_button(self) -> WebElement:
        """Finds and returns the new flow button element of the page."""
        element = self.find_element.by_xpath(locators.NEW_FLOW_BUTTON)
        return element

    def get_header_create_new_flow(self) -> WebElement:
        """Finds and returns the header element of the create new flow page."""
        element = self.find_element.by_xpath(locators.HEADER_CREATE_NEW_FLOW)
        return element

    def get_input_new_flow_name(self) -> WebElement:
        """Finds and returns the input element for the new flow name of the page."""
        element = self.find_element.by_xpath(locators.INPUT_NEW_FLOW_NAME)
        return element

    def get_input_new_flow_code(self) -> WebElement:
        """Finds and returns the input element for the new flow code of the page."""
        element = self.find_element.by_xpath(locators.INPUT_NEW_FLOW_CODE)
        return element

    def get_cancel_button(self) -> WebElement:
        """Finds and returns the cancel button element of the create new flow page."""
        element = self.find_element.by_xpath(locators.CANCEL_NEW_FLOW_BUTTON)
        return element

    def get_create_button(self) -> WebElement:
        """Finds and returns the create button element of the create new flow page."""
        element = self.find_element.by_xpath(locators.CREATE_NEW_FLOW_BUTTON)
        return element

    def get_label_name(self) -> WebElement:
        """Finds and returns the input name label element for the new flow page."""
        element = self.find_element.by_xpath(locators.LABEL_NAME)
        return element

    def get_label_code(self) -> WebElement:
        """Finds and returns the input code label element for the new flow page."""
        element = self.find_element.by_xpath(locators.LABEL_CODE)
        return element

    def get_name_field_required_message(self) -> WebElement:
        """Finds and returns the name field required message in 'Create Flow' dialog."""
        element = self.find_element.by_xpath(locators.NAME_FIELD_REQUIRED_MESSAGE)
        return element

    def get_code_field_required_message(self) -> WebElement:
        """Finds and returns the name field required message in 'Create Flow' dialog."""
        element = self.find_element.by_xpath(locators.CODE_FIELD_REQUIRED_MESSAGE)
        return element
