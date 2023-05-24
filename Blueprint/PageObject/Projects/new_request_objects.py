from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Projects import new_request_locators as locators
from Libraries.Drivers.base_page import BasePage


class NewRequestObject(BasePage):
    """This class represents the objects in new request page of projects """

    def __init__(self):
        super().__init__()

    def get_create_button(self) -> WebElement:
        """Returns the xpath of create button."""
        element = self.find_element.by_xpath(locators.CREATE_BUTTON)
        return element
    
    def get_template_title(self) -> WebElement:
        """Returns the xpath of the template title."""
        element = self.find_element.by_xpath(locators.TEMPLATE_TITLE)
        return element
    
    def get_locator(self, section_name: str, label_name: str) -> WebElement:
        """Returns the xpath of a specific component by its sections and label title."""
        locator = locators.LABELS.replace("<<section_name>>", section_name).replace("<<label_name>>", label_name)
        element = self.find_element.by_xpath(locator)
        return element
