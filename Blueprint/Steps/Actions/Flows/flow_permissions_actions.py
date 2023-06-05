from Blueprint.PageObject.Flows.flow_permissions_objects import FlowPermissions
from Blueprint.PageObject.Flows.Elements.dropdowns import Dropdownbox
from selenium.webdriver.remote.webelement import WebElement


class FlowPermissionsActions(FlowPermissions):
    """This class represents the flow permissions of Blueprint application"""

    def __init__(self):
        super().__init__()
        self.dropdown = Dropdownbox('permissions')
        self.index_dropdown = '1'

    def obtain_flow_permissions_title(self) -> str:
        """Returns the flow permissions title"""
        title = self.get_title_flow_permissions().text
        return title

    def obtain_all_versions_title_in_flow_permissions(self) -> str:
        """Returns the (all versions) title"""
        title = self.get_title_all_versions().text
        return title

    def obtain_flow_admin_title_dropdown_in_flow_permissions(self) -> str:
        """Returns the flow admin dropdown title"""
        dropdown_title = self.dropdown.get_title('TITLE', self.index_dropdown)
        return dropdown_title
    
    def obtain_rgb_color_of_label_in_flow_permissions(self) -> str:
        """Retrieves the RGB color of a label element in the flow admin section"""
        label_color = self.dropdown.get_rgb_color_label('TITLE', self.index_dropdown)
        return label_color
    
    def obtain_rgb_color_of_text_box_in_flow_permissions(self) -> str:
        """Retrieves the RGB color of a text box element in the flow admin section"""
        element_color = self.dropdown.get_rgb_color_element_in_dropdown('TEXT_BOX', self.index_dropdown)
        return element_color
    
    def obtain_rgb_color_of_delete_button_in_flow_permissions(self, name: str) -> str:
        """ Retrieves the RGB background color of a delete button element for a specific user"""
        button_color = self.dropdown.get_rgb_background_color_element('DELETE_ONE_USER', name, self.index_dropdown)
        return button_color
    
    def obtain_user_list_selected_in_text_box_in_flow_permissions(self) -> list:
        """Retrieves the list of selected users in a text box element in the flow admin section"""
        user_list = self.dropdown.get_user_list('USER_SELECTED', self.index_dropdown)
        return user_list
    
    def obtain_dropdown_options_in_flow_permissions(self) -> list:
        """Retrieves the available options from the dropdown"""
        dropdown_options = self.dropdown.get_available_options('DROPDOWN_LIST', self.index_dropdown)
        return dropdown_options
    
    def obtain_visible_element_in_flow_permissions(self) -> WebElement:
        """Retrieves the dropdown element"""
        element = self.dropdown.get_element('DROPDOWN_LIST', self.index_dropdown)
        return element

    def type_name_user_in_dropdown_in_flow_permissions(self, name: str):
        """Types into the dropdown text box"""
        self.dropdown.type_characters_in_dropdown('INPUT_TEXT_BOX', name, self.index_dropdown)

    def delete_typed_name_in_dropdown_in_flow_permissions(self):
        """Deletes which was typed into the dropdown text box"""
        self.dropdown.delete_typed_characters_in_dropdown('INPUT_TEXT_BOX', self.index_dropdown)

    def obtain_typed_characters_in_dropdown_in_flow_permissions(self) -> str:
        """Retrieves the characters from the text box"""
        character = self.dropdown.get_characters_from_text_box('INPUT_TEXT_BOX', self.index_dropdown)
        self.delete_typed_name_in_dropdown_in_flow_permissions()
        return character

    def select_user_from_dropdown_in_flow_permissions(self, user: str):
        """Selects an user of the dropdown"""
        self.dropdown.select_dropdown_option('SELECT_USER', user, self.index_dropdown)

    def delete_all_users_in_dropdown_in_flow_permissions(self):
        """Deletes all user selected of the dropdown"""
        self.dropdown.delete_all_options('DELETE_ALL_USERS', dropdown_index=self.index_dropdown)

    def mouse_hover_delete_button_in_flow_permissions(self, name: str):
        """Performs a mouse hover action on the delete button associated with a specific user"""
        self.dropdown.move_mouse_to_delete_a_user('DELETE_ONE_USER', name, dropdown_index=self.index_dropdown)

    def obtain_message_empty_dropdown_in_flow_permissions(self) -> str:
        """Gets the message when dropdown is empty"""
        message = self.dropdown.message_empty_in_dropdown('EMPTY_MESSAGE', self.index_dropdown)
        return message
    
    def obtain_message_in_empty_text_box_in_flow_permissions(self) -> str:
        """Retrieves the message displayed in an empty text box in the flow admin section"""
        message = self.dropdown.message_in_dropdown_text_box('MESSAGE_IN_TEXT_BOX', self.index_dropdown)
        return message

    def delete_one_selected_user_in_dropdown_in_flow_permissions(self, name: str):
        """Deletes one user from the dropdown"""
        self.dropdown.delete_selected_option('DELETE_ONE_USER', name, self.index_dropdown)

    def delete_selected_users_in_dropdown_in_flow_permissions(self, names: list):
        """Deletes users from the dropdown"""
        for name in names:
            self.delete_one_selected_user_in_dropdown_in_flow_permissions(name)

    def scroll_to_user_in_flow_permissions(self, name: str):
        """Scrolls and select an user"""
        self.dropdown.scroll_down('SELECT_USER', name, self.index_dropdown)

    def click_dropdown_arrow_in_flow_permissions(self):
        """Clicks on dropdown arrow"""
        self.dropdown.click_drop_arrow('DROPDOWN_ARROW', self.index_dropdown)

    def add_new_flow_admin_by_typing_process_in_flow_permission(self, name: str):
        """Adds a new flow administrator by typing the name"""
        self.type_name_user_in_dropdown_in_flow_permissions(name)
        self.select_user_from_dropdown_in_flow_permissions(name)

    def add_new_flow_admin_by_scrolling_process_in_flow_permission(self, name: str):
        """Adds a new flow administrator by scrolling to the name"""
        self.click_dropdown_arrow_in_flow_permissions()
        self.scroll_to_user_in_flow_permissions(name)
