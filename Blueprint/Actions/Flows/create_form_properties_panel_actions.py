from typing import List

from Blueprint.PageObject.Flows.create_form_properties_panel_objects import PropertiesPanelObjects
from Blueprint.PageObject.Flows.create_form_main_panel_objects import FormMainPanelPage
from robot.api import logger


class PropertiesPanelActions(PropertiesPanelObjects):
    """This class represents the properties panel on the create form tab in flow page."""
    def __init__(self):
        super().__init__()
        self.main_panel = FormMainPanelPage()
    
    def set_section_name(self, name: str):
        """"Sets section text name."""
        self.get_section_name_input().clear()
        self.get_section_name_input().send_keys(name)
    
    def set_name(self, name: str):
        """Sets element text name."""
        self.get_name_input().clear()
        self.get_name_input().send_keys(name)
    
    def set_placeholder(self, placeholder: str):
        """Sets element text placeholder."""
        self.get_placeholder_input().clear()
        self.get_placeholder_input().send_keys(placeholder)
        
    def set_default_value(self, default_value: str):
        """Sets default value text."""
        self.get_default_value_input().clear()
        self.get_default_value_input().send_keys(default_value)
        
    def select_field_type(self, field_type: str):
        """Selects field type option."""
        self.get_field_type_select().click()
        self.get_field_type_select_option(field_type).click()
    
    def click_required_field_label(self):
        """Clicks on required field label."""
        self.get_required_field_label().click()
    
    def select_number_format(self, number_format: str):
        """Selects number format value."""
        self.get_number_format_select().click()
        self.get_field_type_select_option(number_format).click()
    
    def get_number_default_value_formatted(self):
        """Gets number default value formatted."""
        return self.get_number_default_value_formatted_noedit().get_attribute("value")
    
    def click_checkbox_default_checked_label(self):
        """Clicks checkbox default checked label."""
        self.get_checkbox_default_checked_label().click()
    
    def click_date_default_value(self):
        """Clicks the date default value."""
        self.get_default_value_input().click()
    
    def set_date_default_value(self, year: str, month: str, day: str):
        """Sets date default value."""
        self.get_default_value_input().click()
        self.get_date_default_year_select().click()
        self.get_date_default_year_value(year).click()
        self.get_date_default_month_select().click()
        self.get_date_default_month_value(month).click()
        self.get_date_default_day_value(day).click()
        
    def select_date_format(self, date_format: str):
        """Selects date format."""
        self.get_date_format_select().click()
        self.get_field_type_select_option(date_format).click()
        
    def set_add_dropdown_value(self, new_value: str):
        """Sets a dropdown value on this input."""
        self.get_add_dropdown_value_input().send_keys(new_value)
        
    def click_add_dropdown_button(self):
        """Clicks add dropdown value button."""
        self.get_add_dropdown_value_button().click()
        
    def get_dropdown_values(self):
        """Gets added dropdown values."""
        self.get_dropdown_values_noedit()
    
    def get_dropdown_value(self, dropdown_value: str):
        """Gets added dropdown value."""
        return self.get_added_dropdown_value(dropdown_value).get_attribute("title")
    
    def delete_added_dropdown_value(self, dropdown_value: str):
        """Deletes added dropdown value."""
        self.get_added_dropdown_value_delete_button(dropdown_value).click()
    
    def select_default_dropdown_value(self, dropdown_value: str):
        """Selects default dropdown value."""
        self.get_default_value_select().click()
        self.get_default_value_select_value(dropdown_value).click()
    
    def select_userlist_value(self, name: str):
        """Selects userlist value."""
        self.get_userlist_values_select().click()
        self.get_userlist_value(name).click()
        
    def select_default_userlist_value(self, name: str):
        """Selects userlist default value."""
        self.get_default_value_select().click()
        self.get_userlist_default_value_option(name).click()

# <-------------------------------------------------------------------------------------------------->

    def define_section_name_process(self, section_current_name: str, section_new_name: str, index=None):
        """Sets the name on the selected section"""
        self.main_panel.get_section(section_current_name, index).click()
        self.set_section_name(section_new_name)

    def define_element_name_process(self, component_id: str, component_new_name):
        """Sets the name on the selected element"""
        self.main_panel.get_component(component_id).click()
        self.set_name(component_new_name)

    def define_element_type_process(self, component_id: str, field_type: str):
        self.main_panel.get_component(component_id).click()
        self.select_field_type(field_type)

    def define_element_placeholder_process(self, component_id: str, placeholder: str):
        self.main_panel.get_component(component_id).click()
        try:
            self.set_placeholder(placeholder)
        except Exception:
            logger.info(f" The element '{component_id}' does not have placeholder")

    def set_element_as_required(self, component_id: str):
        self.main_panel.get_component(component_id).click()
        try:
            self.click_required_field_label()
        except Exception:
            logger.info(f" The element '{component_id}' does not have required field label")

    def set_element_as_default_checked(self, component_id: str):
        self.main_panel.get_component(component_id).click()
        try:
            self.click_checkbox_default_checked_label()
        except Exception:
            logger.info(f" The element '{component_id}' does not have default checked label")

    def define_element_default_value_process(self, component_id: str, value: str):
        self.main_panel.get_component(component_id).click()
        try:
            self.set_default_value(value)
        except Exception:
            logger.info(f" The element '{component_id}' does not have default value label")

    def add_dropdown_values_process(self, component_id: str, values: List[str]):
        self.main_panel.get_component(component_id).click()
        try:
            for value in values:
                self.set_add_dropdown_value(value)
                self.click_add_dropdown_button()
        except Exception:
            logger.info(f" The element '{component_id}' does not have dropdown value label")

    def add_dropdown_single_value_process(self, component_id: str, value: str):
        self.main_panel.get_component(component_id).click()
        try:
            self.set_add_dropdown_value(value)
            self.click_add_dropdown_button()
        except Exception:
            logger.info(f" The element '{component_id}' does not have dropdown value label")

    def delete_dropdown_values_process(self, component_id: str, values: List[str]):
        self.main_panel.get_component(component_id).click()
        try:
            for value in values:
                self.delete_added_dropdown_value(value)
        except Exception:
            logger.info(f" The element '{component_id}' does not have delete value button")

    def define_dropdown_default_value_process(self, component_id: str, value: str):
        self.main_panel.get_component(component_id).click()
        try:
            self.select_default_dropdown_value(value)
        except Exception:
            logger.info(f" The element '{component_id}' does not have dropdown default value label")

    def define_number_format_process(self, component_id: str, number_format: str):
        self.main_panel.get_component(component_id).click()
        try:
            self.select_number_format(number_format)
        except Exception:
            logger.info(f" The element '{component_id}' does not have Format label")

    def define_date_default_value(self, component_id: str, year: str, month: str, day: str):
        self.main_panel.get_component(component_id)
        try:
            self.set_date_default_value(year, month, day)
        except Exception:
            logger.info(f" The element '{component_id}' does not have default Value label")

    def define_date_format(self, component_id: str, date_format: str):
        self.main_panel.get_component(component_id)
        try:
            self.select_date_format(date_format)
        except Exception:
            logger.info(f" The element '{component_id}' does not have default Value label")

    def add_single_user_to_userlist_process(self, component_id: str, name: str):
        self.main_panel.get_component(component_id)
        try:
            self.select_userlist_value(name)
        except Exception:
            logger.info(f" The element '{component_id}' does not have user list Values label")

    def add_users_to_userlist_process(self, component_id: str, users: List[str]):
        self.main_panel.get_component(component_id)
        try:
            for name in users:
                self.select_userlist_value(name)
        except Exception:
            logger.info(f" The element '{component_id}' does not have user list Values label")

    def define_userlist_default_value_process(self, component_id: str, name: str):
        self.main_panel.get_component(component_id)
        try:
            self.select_default_userlist_value(name)
        except Exception:
            logger.info(f" The element '{component_id}' does not have user list default Value label")
