from Blueprint.PageObject.Flows.flows_properties_objects import FlowPropertiesObjects
from Blueprint.PageObject.Flows.Elements.Components.component_storage import ComponentStorage
from Blueprint.PageObject.Flows.Elements.Components.end_component import EndComponent
from Blueprint.Locators.Flows import flows_properties_locators as locators


class FlowPropertiesActions(FlowPropertiesObjects):
    """Flow properties actions on elements."""
    def __init__(self) -> None:
        super().__init__()
        self.index = ComponentStorage()
    
    def click_select_owner_menu_in_flow_properties(self) -> None:
        """Performs click on 'select owner' combobox."""
        self.find_element.by_xpath(locators.OWNER_COMBOBOX_MENU).click()
    
    def select_owner_in_menu_in_flow_properties(self):
        self.find_element.by_xpath(locators.SELECT_FIRST_USER).click()

    def search_owner_in_menu_in_flow_properties(self, user: str):
        self.find_element.by_xpath(locators.SEARCH_OWNER).send_keys(user)
    
    def change_component_name_in_flow_properties(self, new_name: str = "") -> None:
        """Changes component 'name'."""
        self.name_field.text_field.click()
        self.name_field.text_field.clear()
        self.name_field.text_field.send_keys(new_name)

    def click_select_type_in_flow_properties(self) -> None:
        """Performs click on 'select type' combobox."""
        self.select_type_dropbox.combobox.click()
    
    def change_component_type_in_flow_properties(self) -> None:
        """Performs click on 'select type' combobox item."""
        self.select_type_dropbox.combobox.click()
        self.select_type_dropbox.option.click()
    
    def click_end_step_checkbox_in_flow_properties(self, component_id: str) -> None:
        """Performs click on 'End Step' checkbox."""
        self.end_step_checkbox.checkbox.click()
        new_id = f"001END{self.index.counter_end}"
        self.index.component_dictionary.pop(component_id)
        self.index.add_component(new_id, EndComponent(new_id))
        self.index.increment_counter_end()

    def click_add_comment_checkbox_in_flow_properties(self) -> None:
        """Performs click on 'Force to add comment' checkbox."""
        self.add_comment_checkbox.checkbox.click()
    
    def click_required_fields_update_checkbox_in_flow_properties(self) -> None:
        """Performs click on 'Force to update required fields' checkbox."""
        self.required_fields_update_checkbox.checkbox.click()

    def click_select_owner_combobox_in_flow_properties(self) -> None:
        """Performs click on 'select owner' combobox."""
        self.select_owner_dropbox.owner_combobox.click()

    def click_select_owner_combobox_item_in_flow_properties(self) -> None:
        """Performs click on 'select owner' combobox."""
        self.select_owner_dropbox.select_owner_listbox.click()

    def obtain_select_owner_default_item_in_flow_properties(self) -> str:
        """Returns the default owner from 'select owner' list."""
        default_owner = self.select_owner_dropbox.select_owner_default_item.text
        return default_owner
    
    def select_owner_from_list_in_flow_properties(self, text: str = "", position: int = None) -> None:
        """Selects owner from list by text or position."""
        self.select_owner_dropbox.select_owner_item(text, str(position)).click()
    
    def click_owner_combobox_in_flow_properties(self) -> None:
        """Performs click on 'owner' combobox."""
        self.select_owner_dropbox.owner_combobox.click()
    
    def obtain_owner_default_item_in_flow_properties(self) -> str:
        """Returns the default owner from 'owner' list."""
        default_owner = self.select_owner_dropbox.owner_default_item.text
        return default_owner

    def select_owner_in_flow_properties(self, text: str = "", position: int = None) -> None:
        """Selects owner from list by text or position."""
        self.select_owner_dropbox.owner_item(text, str(position)).click()

    def click_add_fields_update_button_in_flow_properties(self) -> None:
        """Performs click on 'add fields to update' button."""
        self.required_fields_update.button.click()
    
    def obtain_error_message_in_flow_properties(self) -> str:
        """Verifies the error message."""
        error_message = self.error_message.message.text
        return error_message

    def obtain_update_field_label_in_flow_properties(self) -> str:
        """Returns label for 'field' list."""
        update_field_label = self.update_fields.form_field_label.text
        return update_field_label
    
    def click_field_combobox_in_flow_properties(self) -> None:
        """Performs click on 'field' combobox."""
        self.update_fields.form_field_combobox.click()

    def select_field_combobox_item_in_flow_properties(self) -> None:
        """Performs click on 'field' combobox."""
        self.update_fields.form_field_first_combobox_item.click()

    def click_field_clear_combobox_in_flow_properties(self) -> None:
        """Performs click on 'clear' button in combobox 'field'."""
        self.update_fields.form_field_clear_combobox.click()
    
    def click_field_combobox_arrow_in_flow_properties(self) -> None:
        """Performs click on dropdown arrow in combobox 'field'."""
        self.update_fields.form_field_combobox_arrow.click()

    def click_value_combobox_in_flow_properties(self) -> None:
        """Performs click on 'value' combobox."""
        self.update_values.form_value_combobox.click()

    def select__ask_user_item_in_flow_properties(self) -> None:
        """Performs click on 'value' combobox."""
        self.update_values.form_value_ask_user_item.click()

    def click_value_clear_combobox_in_flow_properties(self) -> None:
        """Performs click on 'clear' button in combobox 'value'."""
        self.update_values.form_value_clear_combobox.click()
    
    def click_value_combobox_arrow_in_flow_properties(self) -> None:
        """Performs click on dropdown arrow in combobox 'value'."""
        self.update_values.form_value_combobox_arrow.click()

    def click_trash_button_in_flow_properties(self) -> None:
        """Performs click on trash icon button."""
        self.required_fields_update.form_button_trash.click()

    def select_set_value_item_in_flow_properties(self) -> None:
        """Performs click on 'value' combobox."""
        self.update_values.form_value_set_value_item.click()

    def select_update_field_option_by_in_flow_properties(self, text: str = "", position: int = None) -> None:
        """Selects field combobox item by text or by position"""
        xpath = self.locators.REQ_FIELDS_FLD_CMB_ITEM
        if text != "":
            text = self.space_handler(text)
            add_path = self.locators.REQ_FIELDS_FLD_CMB_ITEM_R.replace("<<text>>", text)
        elif position:
            add_path = "[" + str(position) + "]"
        self.find_element.by_xpath(xpath + add_path).click()

    def click_update_fields_input_text_value_in_flow_properties(self) -> None:
        """Click on update text field"""
        self.update_values.text_type_field.click()

    def update_fields_input_text_value_in_flow_properties(self, text: str = "") -> None:
        """Input text into the update text field"""
        self.click_update_fields_input_text_value_in_flow_properties()
        self.update_values.text_type_field.clear()
        self.update_values.text_type_field.send_keys(text)

    def click_update_fields_input_number_value_in_flow_properties(self) -> None:
        """Click on update number field"""
        self.update_values.number_type_field.click()

    def update_fields_input_number_value_in_flow_properties(self, number: int = None) -> None:
        """Input number into the update text field."""
        self.click_update_fields_input_number_value_in_flow_properties()
        self.update_values.number_type_field.clear()
        self.update_values.number_type_field.send_keys(number)

    def click_update_fields_dropdown_list_in_flow_properties(self) -> None:
        """Click on update dropdown list"""
        self.update_values.dropdown_list_type_field.click()    

    def update_fields_select_dropdown_list_value_in_flow_properties(self) -> None:
        """Selects value from dropdown list."""
        self.click_update_fields_dropdown_list_in_flow_properties()

    def click_multiline_text_value_in_flow_properties(self) -> None:
        """Click on multiline text field."""
        self.update_values.multiline_type_field.click()

    def update_fields_multiline_text_value_in_flow_properties(self, text: str = "") -> None:
        """Input text into multiline text field."""
        self.click_multiline_text_value_in_flow_properties()
        self.update_values.multiline_type_field.clear()
        self.update_values.multiline_type_field.send_keys(text)

    def update_fields_checkbox_value_in_flow_properties(self) -> None:
        """Change checkbox state."""
        self.update_values.checkbox_type_field.click()

    def click_select_user_list_value_in_flow_properties(self) -> None:
        """Click on users list dropdown."""
        self.update_values.user_type_field.click()

    def update_fields_select_user_list_value_in_flow_properties(self) -> None:
        """Selects value from users dropdown list."""
        self.click_select_user_list_value_in_flow_properties()
    
    def set_date_value_in_flow_properties(self, day: int = 1, month: int = 1, year: int = 2023) -> None:
        """Updates the new date in update value field in 'action' component."""
        if (1 <= day <= 31) and (1 <= month <= 12):
            self.get_calendar_month_dropdown().click()
            self.get_calendar_month_dropdown_item(month).click()
            self.get_calendar_year_dropdown().click()
            self.get_calendar_year_dropdown_item(year).click()
            self.get_calendar_day(day).click()
        else:
            raise Exception("Invalid date.")

    def click_select_owner_menu_in_flow_properties(self) -> None:
        """Performs click on 'select owner' combobox."""
        self.find_element.by_xpath(locators.OWNER_COMBOBOX_MENU).click()

    def select_owner_in_menu_in_flow_properties(self):
        """Searches an owner in drop menu"""
        self.find_element.by_xpath(locators.SELECT_FIRST_USER).click()

    def search_owner_in_menu_in_flow_properties(self, user: str):
        """Selects an owner in drop menu"""
        self.find_element.by_xpath(locators.SEARCH_OWNER).send_keys(user)
