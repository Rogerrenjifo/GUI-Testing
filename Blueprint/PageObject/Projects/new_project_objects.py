from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Projects import new_project_locators as locators
from Libraries.Drivers.base_page import BasePage


class NewProjectObjects(BasePage):
    """This class represents the objects in new project page of Projects."""

    def get_create_button(self) -> WebElement:
        """Returns the xpath of create button."""
        element = self.find_element.by_xpath(locators.CREATE_BUTTON)
        return element
    
    def get_the_locator_of_flow_template_title(self) -> WebElement:
        """Returns the xpath of the flow template title."""
        element = self.find_element.by_xpath(locators.TEMPLATE_TITLE)
        return element
    
    def get_checkbox_locator(self, section_name: str, label_name: str) -> WebElement:
        """Returns the xpath of a specific checkbox by section and label title."""
        locator = locators.CHECKBOX.replace("<<section_name>>", section_name).replace("<<label_name>>", label_name)
        element = self.find_element.by_xpath(locator)
        return element
    
    def get_element_locator_from_each_section(self, section_name: str, label_name: str) -> WebElement:
        """Returns the xpath of a specific textbox, number box, datebox or user list by section and label title."""
        locator = locators.TEXT_USER_NUMBER_DATE_BOX.replace("<<section_name>>", section_name).replace("<<label_name>>",
                                                                                                       label_name)
        element = self.find_element.by_xpath(locator)
        return element
    
    def get_user_locator_from_dropdown(self, user: str) -> WebElement:
        """Returns the xpath of a specific user from the dropdown by name or email."""
        locator = locators.SELECT_USER.replace("<<user>>", user)
        element = self.find_element.by_xpath(locator)
        return element
    
    def get_css_selector_from_create_button(self) -> WebElement:
        """Returns the css selector from create button"""
        element = self.find_element.by_css_selector(locators.CREATE_BUTTON_CSS_SELECTOR)
        return element
    
    def get_element_locator_from_text_dropdown(self, section_name: str, label_name: str) -> WebElement:
        """Returns the xpath of the content visible in the dropdown"""
        locator = locators.TEXT_IN_DROPDOWN.replace("<<section_name>>", section_name).replace("<<label_name>>",
                                                                                                       label_name)
        element = self.find_element.by_xpath(locator)
        return element
    
    def get_locator_from_remove_user(self, section_name: str, label_name: str) -> WebElement:
        """Returns the xpath of the remove user from a userbox by section and label title."""
        locator = locators.REMOVE_USER_LOCATOR.replace("<<section_name>>", section_name).replace("<<label_name>>", label_name)
        element = self.find_element.by_xpath(locator)
        return element
    
    def get_locator_from_required_field_error_message(self) -> WebElement:
        """Returns the xpath of text 'Field required' error message."""
        element = self.find_element.by_xpath(locators.FIELD_REQUIRED_ERROR_MESSAGE_LOCATOR)
        return element
    
    def get_locator_from_error_message_icon(self) -> WebElement:
        """Returns the xpath of error message icon."""
        element = self.find_element.by_xpath(locators.ERROR_MESSAGE_ICON)
        return element
    
    def get_locator_from_the_label_of_each_component(self, section_name: str, label_name: str) -> WebElement:
        """Returns the xpath of the label of each component in a section."""
        locator = locators.LABEL_LOCATOR.replace("<<section_name>>", section_name).replace("<<label_name>>", label_name)
        element = self.find_element.by_xpath(locator)
        return element

    def get_tag_new(self) -> WebElement:
        """Finds and returns the tag new web element"""
        element = self.find_element.by_xpath(locators.TAG_NEW)
        return element

    def get_element_options_dropdown_list(self) -> WebElement:
        """Returns the web element user option list"""
        locator = locators.LIST_OPTIONS_DROPDOWN
        element = self.find_element.by_xpath(locator)
        return element
