
from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Flows import create_form_elements_locators as locators
from Libraries.Drivers.base_page import BasePage


class CreateFormElementsObjects(BasePage):
    """This class represents the create form Elements of a Blueprint application"""

    def __init__(self, driver):
        super().__init__(driver)
        self.__input_text_element = locators.INPUT_TEXT_ELEMENT
        self.__input_date_element = locators.INPUT_DATE_ELEMENT
        self.__input_numbers_element = locators.INPUT_NUMBERS_ELEMENT
        self.__input_checkbox_element = locators.INPUT_CHECKBOX_ELEMENT
        self.__input_dropdown_element = locators.INPUT_DROPDOWN_ELEMENT
        self.__input_multiline_element = locators.INPUT_MULTILINE_ELEMENT
        self.__input_user_list_element = locators.INPUT_USER_LIST_ELEMENT
        self.__section_element = locators.SECTION_ELEMENT
        self.__components_title = locators.COMPONENTS_TITLE
        self.__section_title = locators.SECTION_TITLE
        self.__drop_area = locators.DROP_AREA

    def get_input_text_element(self) -> WebElement:
        """Finds and returns the input text element of the page."""
        element = self.find_element.by_xpath(self.__input_text_element)
        return element

    def get_input_date_element(self) -> WebElement:
        """Finds and returns the input date element of the page."""
        element = self.find_element.by_xpath(self.__input_date_element)
        return element

    def get_input_numbers_element(self) -> WebElement:
        """Finds and returns the input number element of the page."""
        element = self.find_element.by_xpath(self.__input_numbers_element)
        return element

    def get_input_checkbox_element(self) -> WebElement:
        """Finds and returns the checkbox element of the page."""
        element = self.find_element.by_xpath(self.__input_checkbox_element)
        return element

    def get_input_dropdown_element(self) -> WebElement:
        """Finds and returns the dropdown element of the page."""
        element = self.find_element.by_xpath(self.__input_dropdown_element)
        return element

    def get_input_multiline_element(self) -> WebElement:
        """Finds and returns the input multiline element of the page."""
        element = self.find_element.by_xpath(self.__input_multiline_element)
        return element

    def get_input_user_list_element(self) -> WebElement:
        """Finds and returns the user list element of the page."""
        element = self.find_element.by_xpath(self.__input_user_list_element)
        return element

    def get_section_element(self) -> WebElement:
        """Finds and returns the section element of the page."""
        element = self.find_element.by_xpath(self.__section_element)
        return element

    def get_components_title(self) -> WebElement:
        """Finds and returns the components title element of the page."""
        element = self.find_element.by_xpath(self.__components_title)
        return element

    def get_section_title(self) -> WebElement:
        """Finds and returns the section title element of the page."""
        element = self.find_element.by_xpath(self.__section_title)
        return element

    def get_drop_area(self) -> WebElement:
        """Finds and returns the drop area element of the page."""
        element = self.find_element.by_xpath(self.__drop_area)
        return element
