from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Flows import flows_page_locators as locators
from Libraries.Drivers.base_page import BasePage


class NewFlow(BasePage):
    """This class represents the login page of a Blueprint application"""

    def __init__(self, driver):
        super().__init__(driver)
        self.__drop_down_flow_menu = locators.DROP_DOWN_FLOW_MENU
        self.__new_flow_button = locators.NEW_FLOW_BUTTON
        self.__header_create_new_flow = locators.HEADER_CREATE_NEW_FLOW
        self.__input_new_flow_name = locators.INPUT_NEW_FLOW_NAME
        self.__input_new_flow_code = locators.INPUT_NEW_FLOW_CODE
        self.__cancel_button = locators.CANCEL_NEW_FLOW_BUTTON
        self.__create_button = locators.CREATE_NEW_FLOW_BUTTON
        self.__label_name = locators.LABEL_NAME
        self.__label_code = locators.LABEL_CODE

    def get_drop_down_flow_menu(self) -> WebElement:
        """Finds and returns the drop-down flow menu element of the page."""
        element = self.find_element.by_xpath(self.__drop_down_flow_menu)
        return element

    def get_new_flow_button(self) -> WebElement:
        """Finds and returns the new flow button element of the page."""
        element = self.find_element.by_xpath(self.__new_flow_button)
        return element

    def get_header_create_new_flow(self) -> WebElement:
        """Finds and returns the header element of the create new flow page."""
        element = self.find_element.by_xpath(self.__header_create_new_flow)
        return element

    def get_input_new_flow_name(self) -> WebElement:
        """Finds and returns the input element for the new flow name of the page."""
        element = self.find_element.by_xpath(self.__input_new_flow_name)
        return element

    def get_input_new_flow_code(self) -> WebElement:
        """Finds and returns the input element for the new flow code of the page."""
        element = self.find_element.by_xpath(self.__input_new_flow_code)
        return element

    def get_cancel_button(self) -> WebElement:
        """Finds and returns the cancel button element of the create new flow page."""
        element = self.find_element.by_xpath(self.__cancel_button)
        return element

    def get_create_button(self) -> WebElement:
        """Finds and returns the create button element of the create new flow page."""
        element = self.find_element.by_xpath(self.__create_button)
        return element

    def get_label_name(self) -> WebElement:
        """Finds and returns the input name label element for the new flow page."""
        element = self.find_element.by_xpath(self.__label_name)
        return element

    def get_label_code(self) -> WebElement:
        """Finds and returns the input code label element for the new flow page."""
        element = self.find_element.by_xpath(self.__label_code)
        return element
