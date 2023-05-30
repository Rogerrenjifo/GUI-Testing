from Blueprint.PageObject.Flows.create_form_properties_panel_objects import PropertiesPanelObjects
from Blueprint.PageObject.Flows.create_form_main_panel_objects import FormMainPanelPage
from Blueprint.Steps.Actions.CommonElements.date_actions import DateActions
from robot.api import logger
from typing import List


class PropertiesPanelActions(PropertiesPanelObjects):
    """This class represents the properties panel on the create form tab in flow page."""
    def __init__(self):
        super().__init__()
        self.main_panel = FormMainPanelPage()
        self.date_actions = DateActions()
    
    def set_section_name_in_form_properties_panel(self, name: str):
        """Sets section text name."""
        self.get_section_name_input().clear()
        self.get_section_name_input().send_keys(name)
    
    def set_name_in_form_properties_panel(self, name: str):
        """Sets element text name."""
        self.get_name_input().clear()
        self.get_name_input().send_keys(name)
    
    def set_placeholder_in_form_properties_panel(self, placeholder: str):
        """Sets element text placeholder."""
        self.get_placeholder_input().clear()
        self.get_placeholder_input().send_keys(placeholder)
        
    def set_default_value_in_form_properties_panel(self, default_value: str):
        """Sets default value text."""
        self.get_default_value_input().clear()
        self.get_default_value_input().send_keys(default_value)
        
    def select_field_type_in_form_properties_panel(self, field_type: str):
        """Selects field type option."""
        self.get_field_type_select().click()
        self.get_field_type_select_option(field_type).click()
    
    def click_required_field_label_in_form_properties_panel(self):
        """Clicks on required field label."""
        self.get_required_field_label().click()
    
    def select_number_format_in_form_properties_panel(self, number_format: str):
        """Selects number format value."""
        self.get_number_format_select().click()
        self.get_field_type_select_option(number_format).click()
    
    def get_number_default_value_formatted_in_form_properties_panel(self):
        """Gets number default value formatted."""
        return self.get_number_default_value_formatted_noedit().get_attribute("value")
    
    def click_checkbox_default_checked_label_in_form_properties_panel(self):
        """Clicks checkbox default checked label."""
        self.get_checkbox_default_checked_label().click()
    
    def click_date_default_value_in_form_properties_panel(self):
        """Clicks the date default value."""
        self.get_default_value_input().click()
    
    def set_date_default_value_in_form_properties_panel(self, year: str, month: str, day: str):
        """Sets date default value."""
        self.get_default_value_input().click()
        self.date_actions.set_date(year, month, day)
        
    def select_date_format_in_form_properties_panel(self, date_format: str):
        """Selects date format."""
        self.get_date_format_select().click()
        self.get_field_type_select_option(date_format).click()
        
    def set_add_dropdown_value_in_form_properties_panel(self, new_value: str):
        """Sets a dropdown value on this input."""
        self.get_add_dropdown_value_input().send_keys(new_value)
        
    def click_add_dropdown_button_in_form_properties_panel(self):
        """Clicks add dropdown value button."""
        self.get_add_dropdown_value_button().click()
        
    def get_dropdown_values_in_form_properties_panel(self):
        """Gets added dropdown values."""
        self.get_dropdown_values_noedit()
    
    def get_dropdown_value_in_form_properties_panel(self, dropdown_value: str):
        """Gets added dropdown value."""
        return self.get_added_dropdown_value(dropdown_value).get_attribute("title")
    
    def delete_added_dropdown_value_in_form_properties_panel(self, dropdown_value: str):
        """Deletes added dropdown value."""
        self.get_added_dropdown_value_delete_button(dropdown_value).click()
    
    def select_default_dropdown_value_in_form_properties_panel(self, dropdown_value: str):
        """Selects default dropdown value."""
        self.get_default_value_select().click()
        self.get_default_value_select_value(dropdown_value).click()
    
    def select_userlist_value_in_form_properties_panel(self, name: str):
        """Selects userlist value."""
        self.get_userlist_values_select().click()
        self.get_userlist_value(name).click()
        
    def select_default_userlist_value_in_form_properties_panel(self, name: str):
        """Selects userlist default value."""
        self.get_default_value_select().click()
        self.get_userlist_default_value_option(name).click()

    def define_section_name_process_in_form_properties(self, section_name: str,
                                                       section_new_name: str):
        """Defines the name on the selected section"""
        self.main_panel.get_section(section_name).click()
        self.set_section_name_in_form_properties_panel(section_new_name)

    def define_element_name_process_in_form_properties(self, component_id: str, component_new_name):
        """Defines the name on the selected element"""
        self.main_panel.get_component(component_id).click()
        self.set_name_in_form_properties_panel(component_new_name)

    def define_element_type_process_in_form_properties(self, component_id: str, field_type: str):
        """Defines the type of selected element"""
        self.main_panel.get_component(component_id).click()
        self.select_field_type_in_form_properties_panel(field_type)

    def define_element_placeholder_process_in_form_properties(self, component_id: str,
                                                              placeholder: str):
        """Defines the placeholder of selected element"""
        self.main_panel.get_component(component_id).click()
        try:
            self.set_placeholder_in_form_properties_panel(placeholder)
        except Exception:
            logger.info(f" The element '{component_id}' does not have placeholder")

    def set_element_as_required_process_in_form_properties(self, component_id: str):
        """Sets the selected element as required"""
        self.main_panel.get_component(component_id).click()
        try:
            self.click_required_field_label_in_form_properties_panel()
        except Exception:
            logger.info(f" The element '{component_id}' does not have required field label")

    def set_element_as_default_checked_process_in_form_properties(self, component_id: str):
        """Sets the selected checkbox element as check by default"""
        self.main_panel.get_component(component_id).click()
        try:
            self.click_checkbox_default_checked_label_in_form_properties_panel()
        except Exception:
            logger.info(f" The element '{component_id}' does not have default checked label")

    def define_element_default_value_process_in_form_properties(self, component_id: str,
                                                                value: str):
        """Defines the default value of selected element"""
        self.main_panel.get_component(component_id).click()
        try:
            self.set_default_value_in_form_properties_panel(value)
        except Exception:
            logger.info(f" The element '{component_id}' does not have default value label")

    def add_dropdown_values_process_in_form_properties(self, component_id: str, values: List[str]):
        """Adds a list of values to a selected dropdown"""
        self.main_panel.get_component(component_id).click()
        try:
            for value in values:
                self.set_add_dropdown_value_in_form_properties_panel(value)
                self.click_add_dropdown_button_in_form_properties_panel()
        except Exception:
            logger.info(f" The element '{component_id}' does not have dropdown value label")

    def add_dropdown_single_value_process_in_form_properties(self, component_id: str, value: str):
        """Adds a single value to a selected dropdown"""
        self.main_panel.get_component(component_id).click()
        try:
            self.set_add_dropdown_value_in_form_properties_panel(value)
            self.click_add_dropdown_button_in_form_properties_panel()
        except Exception:
            logger.info(f" The element '{component_id}' does not have dropdown value label")

    def delete_dropdown_values_process_in_form_properties(self, component_id: str,
                                                          values: List[str]):
        """Deletes a list of values to a selected dropdown"""
        self.main_panel.get_component(component_id).click()
        try:
            for value in values:
                self.delete_added_dropdown_value_in_form_properties_panel(value)
        except Exception:
            logger.info(f" The element '{component_id}' does not have delete value button")

    def define_dropdown_default_value_process_in_form_properties(self, component_id: str,
                                                                 value: str):
        """Defines the default value of selected dropdown element"""
        self.main_panel.get_component(component_id).click()
        try:
            self.select_default_dropdown_value_in_form_properties_panel(value)
        except Exception:
            logger.info(f" The element '{component_id}' does not have dropdown default value label")

    def define_number_format_process_in_form_properties(self, component_id: str,
                                                        number_format: str):
        """Defines the format of selected number element"""
        self.main_panel.get_component(component_id).click()
        try:
            self.select_number_format_in_form_properties_panel(number_format)
        except Exception:
            logger.info(f" The element '{component_id}' does not have Format label")

    def define_date_default_value_process_in_form_properties(self, component_id: str,
                                                             year: str, month: str, day: str):
        """Defines the default value of selected date element"""
        self.main_panel.get_component(component_id).click()
        try:
            self.set_date_default_value_in_form_properties_panel(year, month, day)
        except Exception:
            logger.info(f" The element '{component_id}' does not have default Value label")

    def define_date_format_process_in_form_properties(self, component_id: str, date_format: str):
        """Defines the format of selected date element"""
        self.main_panel.get_component(component_id).click()
        try:
            self.select_date_format_in_form_properties_panel(date_format)
        except Exception:
            logger.info(f" The element '{component_id}' does not have default Value label")

    def add_single_user_to_userlist_process_in_form_properties(self, component_id: str, name: str):
        """Adds a single user value to a selected user list element"""
        self.main_panel.get_component(component_id).click()
        try:
            self.select_userlist_value_in_form_properties_panel(name)
        except Exception:
            logger.info(f" The element '{component_id}' does not have user list Values label")

    def add_users_to_userlist_process_in_form_properties(self, component_id: str, users: List[str]):
        """Adds a list of users values to a selected user list element"""
        self.main_panel.get_component(component_id).click()
        try:
            for name in users:
                self.select_userlist_value_in_form_properties_panel(name)
        except Exception:
            logger.info(f" The element '{component_id}' does not have user list Values label")

    def define_userlist_default_value_process_in_form_properties(self, component_id: str,
                                                                 name: str):
        """Defines the default value of selected user list element"""
        self.main_panel.get_component(component_id).click()
        try:
            self.select_default_userlist_value_in_form_properties_panel(name)
        except Exception:
            logger.info(f" The element '{component_id}'"
                        f" does not have user list default Value label")
