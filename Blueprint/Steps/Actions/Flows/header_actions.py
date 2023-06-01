from Blueprint.PageObject.Flows.header_objects import Header
from Blueprint.Steps.Actions.CommonElements.delete_dialog_actions import DeleteDialogActions


class HeaderActions(Header):
    """This class represents the actions in the header of the flows page."""
    
    def __init__(self) -> None:
        super().__init__()
        self.delete_dialog = DeleteDialogActions()
    
    def get_flow_status_text_in_flow_header(self) -> str:
        """Gets the text of the flow status"""
        status_text = self.get_flow_status().text
        return status_text
    
    def get_flow_version_text_in_flow_header(self) -> str:
        """Gets the text of the flow version"""
        version_text = self.get_flow_version().text
        return version_text
    
    def get_flow_name_text_in_flow_header(self) -> str:
        """Gets the text of the flow name"""
        flow_name_text = self.get_flow_name().text
        return flow_name_text
    
    def display_header_dropdown_in_flow_header(self) -> None:
        """Displays the dropdown of the Flows header"""
        dropdown = self.get_dropdown_button()
        dropdown.click()

    def click_delete_option_in_flow_header(self) -> None:
        """Clicks on the Delete option. The "deploy_header_dropdown" method needs to be executed before."""
        delete = self.get_delete_option()
        delete.click()

    def click_cancel_button_in_delete_dialog(self) -> None:
        """Clicks on the Cancel button of the Delete Process dialog. The "click_delete_option" method needs to be
        executed before."""
        self.delete_dialog.click_cancel_dialog_button()

    def click_delete_button_in_delete_dialog(self) -> None:
        """Clicks on the Delete button of the Delete Process dialog. The "click_delete_option" method needs to be
        executed before."""
        self.delete_dialog.click_delete_dialog_button()

    def click_close_button_in_delete_dialog(self) -> None:
        """Clicks on the close button of the Delete Process dialog. The "click_delete_option" method needs to be
        executed before."""
        self.delete_dialog.click_close_dialog_button()    
   
    def display_select_version_in_flow_header(self) -> None:
        """Displays the Select Version option. The "deploy_header_dropdown" method needs to be executed before."""
        select_version = self.get_select_version_option()
        self.action_chains.move_to_an_element(select_version)

    def click_version_in_flow_header(self, version: str) -> None:
        """Clicks a version from the deployed versions list. The "deploy_select_version" method needs to be
        executed before."""
        selected_version = self.get_specific_version(version)
        selected_version.click()

    def get_last_updated_text_in_flow_header(self) -> str:
        """Gets the text of the flow version"""
        last_updated_text = self.get_last_updated().text
        return last_updated_text
        
    def click_save_button_in_flow_header(self) -> None:
        """Clicks on the Save button"""
        save_button = self.get_save_button()
        save_button.click()

    def click_save_next_button_in_flow_header(self) -> None:
        """Clicks on the Save & next button"""
        save_next_button = self.get_save_next_button()
        save_next_button.click()

    def click_tab_in_flow_header(self, tab_name: str) -> None:
        """Clicks on a selected tab"""
        selected_tab = self.get_tab(tab_name)
        selected_tab.click()

    def get_marked_tab_in_flow_header(self, tab_name: str) -> bool:
        """Gets the marked status from the selected tab"""        
        status_tab = self.is_marked_tab_elements(tab_name)
        return status_tab  
    
    def get_unmarked_tab_in_flow_header(self, tab_name: str) -> bool:
        """Gets the unmarked status from the selected tab"""
        status_tab = self.is_unmarked_tab_elements(tab_name)
        return status_tab 
    
    def get_error_marked_tab_in_flow_header(self, tab_name: str) -> bool:
        """Gets the marked status from the selected tab"""        
        status_tab = self.is_error_marked_tab_elements(tab_name)
        return status_tab  
    
    def get_error_unmarked_tab_in_flow_header(self, tab_name: str) -> bool:
        """Gets the unmarked status from the selected tab"""          
        status_tab = self.is_error_unmarked_tab_elements(tab_name)
        return status_tab

    def delete_flow_process_in_flow_header(self) -> None:
        """Executes the process to delete a flow"""
        self.display_header_dropdown_in_flow_header()
        self.click_delete_option_in_flow_header()
        self.click_delete_button_in_flow_header()

    def cancel_delete_flow_process_in_flow_header(self) -> None:
        """Cancels the process to delete a flow. The flow is not deleted"""
        self.display_header_dropdown_in_flow_header()
        self.click_delete_option_in_flow_header()
        self.click_cancel_button_in_flow_header()

    def close_delete_flow_process_in_flow_header(self) -> None:
        """Closes the delete dialog while delete flow process is running. The flow is not deleted"""
        self.display_header_dropdown_in_flow_header()
        self.click_delete_option_in_flow_header()
        self.click_close_button_in_flow_header()

    def change_flow_version_process_in_flow_header(self, version: str) -> None:
        """Changes the flow version selected"""
        self.display_header_dropdown_in_flow_header()
        self.display_select_version_in_flow_header()
        self.click_version_in_flow_header(version)

    def hover_save_button_in_flow_header(self) -> None:
        """Hovers on the Save button"""
        save_button = self.get_save_button()
        self.action_chains.move_to_an_element(save_button)

    def hover_save_next_button_in_flow_header(self) -> None:
        """Hovers on the Save & next button"""
        save_next_button = self.get_save_next_button()
        self.action_chains.move_to_an_element(save_next_button)
    
    def obtain_save_button_rgb_color_in_flow_header(self) -> str:
        """Gets the RGB color of save button in flow header"""
        color_save_button = self.get_save_button().value_of_css_property("background-color")
        return color_save_button
    
    def obtain_save_next_button_rgb_color_in_flow_header(self) -> str:
        """Gets the RGB color of save & next button in flow header"""
        color_save_next_button = self.get_save_next_button().value_of_css_property("background-color")
        return color_save_next_button
