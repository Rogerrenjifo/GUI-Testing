from Blueprint.PageObject.Flows.header_objects import Header


class HeaderActions(Header):
    """This class represents the actions in the header of Flows page"""
    
    def get_status_text(self):
        """Gets the text of the flow status"""
        status_text = self.get_status().text
        return status_text
    
    def get_version_text(self):
        """Gets the text of the flow version"""
        version_text = self.get_version().text
        return version_text
    
    def get_flow_name_text(self):
        """Gets the text of the flow name"""
        flow_name_text = self.get_flow_name().text
        return flow_name_text
    
    def display_header_dropdown(self):
        """Displays the dropdown of the Flows header"""
        dropdown = self.get_dropdown_button()
        dropdown.click()

    def click_delete_option(self):
        """Clicks on the Delete option. The "deploy_header_dropdown" method needs to be executed before."""
        delete = self.get_delete_option()
        delete.click()

    def click_cancel_button(self):
        """Clicks on the Cancel button of the Delete Process dialog. The "click_delete_option" method needs to be executed before."""
        delete = self.get_cancel_button()
        delete.click()

    def click_delete_button(self):
        """Clicks on the Delete button of the Delete Process dialog. The "click_delete_option" method needs to be executed before."""
        delete = self.get_delete_button()
        delete.click()

    def click_close_button(self):
        """Clicks on the close button of the Delete Process dialog. The "click_delete_option" method needs to be executed before."""
        delete = self.get_close_button()
        delete.click()    
   
    def display_select_version(self):
        """Displays the Select Version option. The "deploy_header_dropdown" method needs to be executed before."""
        select_version = self.get_select_version_option()
        self.action_chains.move_to_an_element(select_version)

    def click_version(self, version: str):
        """Clicks a version from the deployed versions list. The "deploy_select_version" method needs to be executed before."""
        selected_version = self.get_specific_version(version)
        selected_version.click()

    def get_last_updated_text(self):
        """Gets the text of the flow version"""
        last_updated_text = self.get_last_updated().text
        return last_updated_text
        
    def click_save_button(self):
        """Clicks on the Save button"""
        save_button = self.get_save_button()
        save_button.click()

    def click_save_next_button(self):
        """Clicks on the Save & next button"""
        save_next_button = self.get_save_next_button()
        save_next_button.click()

    def click_tab(self, tab_name: str):
        """Clicks on a selected tab"""
        selected_tab = self.get_tab(tab_name)
        selected_tab.click()

    def get_marked_tab(self, tab_name: str):
        """Gets the marked status from the selected tab"""        
        status_tab = self.is_marked_tab_elements(tab_name)
        return status_tab  
    
    def get_unmarked_tab(self, tab_name: str):
        """Gets the unmarked status from the selected tab"""          
        status_tab = self.is_unmarked_tab_elements(tab_name)
        return status_tab 
    
    def get_error_marked_tab(self, tab_name: str):
        """Gets the marked status from the selected tab"""        
        status_tab = self.is_error_marked_tab_elements(tab_name)
        return status_tab  
    
    def get_error_unmarked_tab(self, tab_name: str):
        """Gets the unmarked status from the selected tab"""          
        status_tab = self.is_error_unmarked_tab_elements(tab_name)
        return status_tab

    def delete_flow_process_in_flow_header(self):
        """Executes the process to delete a flow"""
        self.display_header_dropdown()
        self.click_delete_option()
        self.click_delete_button()

    def cancel_delete_flow_process_in_flow_header(self):
        """Cancels the process to delete a flow. The flow is not deleted"""
        self.display_header_dropdown()
        self.click_delete_option()
        self.click_cancel_button()

    def close_delete_flow_process_in_flow_header(self):
        """Closes the delete dialog while delete flow process is running. The flow is not deleted"""
        self.display_header_dropdown()
        self.click_delete_option()
        self.click_close_button()

    def change_flow_version_process_in_flow_header(self, version: str):
        """Changes the flow version selected"""
        self.display_header_dropdown()
        self.display_select_version()
        self.click_version(version)
