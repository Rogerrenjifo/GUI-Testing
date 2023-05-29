from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Projects import new_request_locators as locators
from Libraries.Drivers.base_page import BasePage


class NewRequestObject(BasePage):
    """This class represents the objects in new request page of projects """

    def get_create_button(self) -> WebElement:
        """Returns the xpath of create button."""
        element = self.find_element.by_xpath(locators.CREATE_BUTTON)
        return element
    
    def get_flow_template_title(self) -> WebElement:
        """Returns the xpath of the flow template title."""
        element = self.find_element.by_xpath(locators.TEMPLATE_TITLE)
        return element
    
    def get_checkbox_locator(self, section_name: str, label_name: str) -> WebElement:
        """Returns the xpath of a specific checkbox by section and label title."""
        locator = locators.CHECKBOX.replace("<<section_name>>", section_name).replace("<<label_name>>", label_name)
        element = self.find_element.by_xpath(locator)
        return element
    
    def get_element_locator_from_each_section(self, section_name: str, label_name: str) -> WebElement:
        """Returns the xpath of a specific textbox, numberbox, datebox or userlist by section and label title."""
        locator = locators.TEXT_USER_NUMBER_DATE_BOX.replace("<<section_name>>", section_name).replace("<<label_name>>", label_name)
        element = self.find_element.by_xpath(locator)
        return element
    
    def get_user_locator_from_dropdown(self, user: str) -> WebElement:
        """Returns the xpath of a specific user from the dropdown by name or email"""
        locator = locators.SELECT_USER.replace("<<user>>", user)
        element = self.find_element.by_xpath(locator)
        return element
    
    def get_locator_from_remove_user(self, section_name: str, label_name: str) -> WebElement:
        """Returns the xpath of the remove user from a userbox by section and label title."""
        locator = locators.REMOVE_USER_LOCATOR.replace("<<section_name>>", section_name).replace("<<label_name>>", label_name)
        element = self.find_element.by_xpath(locator)
    
    def get_locator_from_remove_user(self, section_name: str, label_name: str) -> WebElement:
        """Returns the xpath of the remove user from a userbox by section and label title."""
        locator = locators.REMOVE_USER_LOCATOR.replace("<<section_name>>", section_name).replace("<<label_name>>", label_name)
        element = self.find_element.by_xpath(locator)
        return element

    def get_css_selector_from_create_button(self) -> WebElement:
        """Returns the css selector from create button"""
        element = self.find_element.by_css_selector(locators.CREATE_BUTTON_CSS_SELECTOR)
        return element
