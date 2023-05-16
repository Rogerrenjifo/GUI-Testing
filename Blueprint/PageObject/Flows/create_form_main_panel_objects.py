from Blueprint.Locators.Flows import create_form_main_panel_locators as locators
from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage


class FormMainPanelPage(BasePage):
    """This class represents the main panel of create form tab in flow page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.__section_locator = locators.SECTION_LOCATOR
        self.__section_title_locator = locators.SECTION_TITLE_LOCATOR
        self.__section_dropdown_locator = locators.SECTION_DROPDOWN_LOCATOR
        self.__section_delete_button_locator = locators.SECTION_DELETE_BUTTON_LOCATOR
        self.__section_error_message_locator = locators.SECTION_ERROR_MESSAGE_LOCATOR
        self.__component_locator = locators.COMPONENT_LOCATOR
        self.__component_title_locator = locators.COMPONENT_TITLE_LOCATOR
        self.__component_dropdown_locator = locators.COMPONENT_DROPDOWN_LOCATOR
        self.__component_delete_button_locator = locators.COMPONENT_DELETE_BUTTON_LOCATOR

    @staticmethod
    def get_locator(locator_model, replacement_attribute, index=None):
        """Returns the xpath of a specific section or component by its title and position"""
        if index is not None:
            locator = locator_model.replace('ToChange', replacement_attribute)
            locator = f'({locator})[{index}]'
        else:
            locator = locator_model.replace('ToChange', replacement_attribute)
        return locator

    def get_section(self, title, index=None) -> WebElement:
        """Finds and returns the section element from main panel of the page."""
        locator = self.get_locator(self.__section_locator, title, index)
        # TODO

    def get_section_colum(self, element_id) -> WebElement:
        """Finds and returns a column of a section from main panel of the page."""
        # TODO

    def get_section_title(self, title, index=None) -> WebElement:
        """Finds and returns the title element of a section from main panel of the page."""
        locator = self.get_locator(self.__section_title_locator, title, index)
        # TODO

    def get_section_dropdown(self, title, index=None) -> WebElement:
        """Finds and returns the dropdown of a section from main panel of the page."""
        locator = self.get_locator(self.__section_dropdown_locator, title, index)
        # TODO

    def get_section_delete_button(self, title) -> WebElement:
        """Finds and returns the delete button of a section from main panel of the page."""
        # TODO

    def get_section_error_message(self, title, index=None) -> WebElement:
        """Finds and returns the error message element of a section from main panel of the page."""
        locator = self.get_locator(self.__section_error_message_locator, title, index)
        # TODO

    def get_component(self, title, index=None) -> WebElement:
        """Finds and returns the component element of a section from main panel of the page."""
        locator = self.get_locator(self.__component_locator, title, index)
        # TODO

    def get_component_title(self, title, index=None) -> WebElement:
        """Finds and returns the title element of a component from main panel of the page."""
        locator = self.get_locator(self.__component_title_locator, title, index)
        # TODO

    def get_component_dropdown(self, title, index=None) -> WebElement:
        """Finds and returns the dropdown of a component from main panel of the page."""
        locator = self.get_locator(self.__component_dropdown_locator, title, index)
        # TODO

    def get_component_delete_button(self, title, index=None) -> WebElement:
        """Finds and returns the delete button of a component from main panel of the page."""
        locator = self.get_locator(self.__component_delete_button_locator, title, index)
        # TODO
