from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flows_properties_locators as locators
from Blueprint.PageObject.Flows.Elements.flows_properties.flow_elements import FlowElements


class FlowPropertiesObjects(BasePage):
    """"Flows Properties objects representation."""

    def __init__(self):
        super().__init__()
        flow_elements = FlowElements()
        self.locators = locators
        self.name_field = flow_elements.name_field
        self.select_type_dropbox = flow_elements.select_type_dropbox
        self.end_step_checkbox = flow_elements.end_step_checkbox
        self.add_comment_checkbox = flow_elements.add_comment_checkbox
        self.required_fields_update_checkbox = flow_elements.update_fields_checkbox
        self.select_owner_dropbox = flow_elements.select_owner_dropbox
        self.required_fields_update = flow_elements.required_fields_update
        self.error_message = flow_elements.error_message
        self.update_fields = flow_elements.update_fields
        self.update_values = flow_elements.update_values
        self.update_commons = flow_elements.update_commons

    def space_handler(self, text: str = "") -> str:
        """Returns text with added space at begining and the end of the string."""
        if not text.startswith(" ") and not text.endswith(" "):
            return " " + text + " "
        else:
            return text.strip()
        
    def get_calendar_year_dropdown(self) -> WebElement:
        """Gets calendar's year dropdown list."""
        element = self.find_element.by_xpath(self.locators.DATE_PICKER_YEAR)
        return element
    
    def get_calendar_month_dropdown(self) -> WebElement:
        """Gets calendar's month dropdown list."""
        element = self.find_element.by_xpath(self.locators.DATE_PICKER_MONTH)
        return element
    
    def get_calendar_year_dropdown_item(self, year: int = None) -> WebElement:
        """Gets calendar's year dropdown list."""
        xpath = self.locators.DATE_PICKER_YEAR_ADD.replace("<<year>>", self.space_handler(str(year)))
        element = self.find_element.by_xpath(xpath)
        return element
    
    def get_calendar_month_dropdown_item(self, month: int = None) -> WebElement:
        """Gets calendar's month dropdown list."""
        month -= 1
        xpath = self.locators.DATE_PICKER_MONTH_ADD.replace("<<month>>", str(month))
        element = self.find_element.by_xpath(xpath)
        return element

    def get_calendar_day(self, day: int = None)-> WebElement:
        """Gets calendar's day table."""
        xpath = self.locators.DATE_PICKER_DAY.replace("<<day>>", self.space_handler(str(day)))
        element = self.find_element.by_xpath(xpath)
        return element
