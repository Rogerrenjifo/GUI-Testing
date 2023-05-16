from Blueprint.PageObject.Flows.create_form_properties_panel_objects import PropertiesPanelObjects

class PropertiesPanelActions(PropertiesPanelObjects):
    """This class represents the properties panel on the create form tab in flow page"""
    
    def set_section_name(self, name):
        """"Sets section text name"""
        self.get_section_name_input().clear()
        self.get_section_name_input().send_keys(name)
    
    def set_name(self, name):
        """Sets element text name"""
        self.get_name_input().clear()
        self.get_name_input().send_keys(name)
    
    def set_placeholder(self, placeholder):
        """Sets element text placeholder"""
        self.get_placeholder_input().clear()
        self.get_placeholder_input().send_keys(placeholder)
        
    def set_default_value(self, default_value):
        """Sets default value text"""
        self.get_default_value_input().clear()
        self.get_default_value_input().send_keys(default_value)
        
    def select_field_type(self, value):
        """Selects field type option"""
        # TO DO 
    
    def click_required_field_label(self):
        """Clicks on required field label"""
        self.get_required_field_label().click()
    
    def select_number_format(self, value):
        """Selects number format value"""
        # TO DO
    
    def get_number_default_value_formatted(self):
        """Gets number default value formatted"""
        self.get_number_default_value_formatted_noedit().text
    
    def click_chackbox_default_checked_label(self):
        """Clicks checkbox default checked label"""
        self.get_checkbox_default_checked_label().click()
        
    def select_date_format(self, value):
        """Selects date format"""
        # TO DO
        
    def set_add_dropdown_value(self, value):
        """Sets a dropdown value on this input"""
        self.get_add_dropdown_value_input().send_keys(value)
        
    def click_add_dropdown_button(self):
        """Clicks add dropdown value button"""
        self.get_add_dropdown_value_button().click()
        
    def get_dropdown_values(self):
        """Gets added dropdown values"""
        # TO DO
    
    def select_default_dropdown_value(self, value):
        """Selects default dropdown value"""
        # TO DO
    
    def select_userlist_value(self, value):
        """Selects userlist value"""
        # TO DO
    