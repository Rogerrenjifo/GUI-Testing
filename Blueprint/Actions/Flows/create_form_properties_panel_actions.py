from Blueprint.PageObject.Flows.create_form_properties_panel_objects import PropertiesPanelObjects

class PropertiesPanelActions(PropertiesPanelObjects):
    """This class represents the properties panel on the create form tab in flow page."""
    
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
