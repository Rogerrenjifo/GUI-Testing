from Blueprint.PageObject.Flows.process_permissions_objects import ProcessPermissions
from Blueprint.PageObject.Flows.Elements.dropdowns import Dropdownbox
from selenium.webdriver.remote.webelement import WebElement


class SectionsVisibilityActions(ProcessPermissions):
    """This class represents the section visibility of a Blueprint application"""
    def __init__(self):
        super().__init__()
        self.dropdown = Dropdownbox('permissions')

    def obtain_section_visibility_title_in_section_visibility(self) -> str:
        """Returns the section visibility title"""
        title_section_visibility = self.get_title_section_visibility().text
        return title_section_visibility
        
    def obtain_sections_title_dropdown_in_section_visibility(self, dropdown_index: str) -> str:
        """Gets the title of the sections visibility"""
        title = self.dropdown.get_title('TITLE', dropdown_index)
        return title
    
    def obtain_rgb_color_of_label_in_section_visibility(self, dropdown_index: str) -> str:
        """Retrieves the RGB color of a label element in the section visibility"""
        label_color = self.dropdown.get_rgb_color_label('TITLE', dropdown_index)
        return label_color
    
    def obtain_rgb_color_of_text_box_in_section_visibility(self, dropdown_index: str) -> str:
        """Retrieves the RGB color of a text box element in the section visibility"""
        element_color = self.dropdown.get_rgb_color_element_in_dropdown('TEXT_BOX', dropdown_index)
        return element_color
    
    def obtain_rgb_color_of_delete_button_in_section_visibility(self, name: str, dropdown_index: str) -> str:
        """ Retrieves the RGB background color of a delete button element for a specific user"""
        button_color = self.dropdown.get_rgb_background_color_element('DELETE_ONE_USER', name, dropdown_index)
        return button_color
    
    def obtain_user_list_selected_in_text_box_in_section_visibility(self, dropdown_index: str) -> list:
        """Retrieves the list of selected users in a text box element in the section visibility"""
        user_list = self.dropdown.get_user_list('USER_SELECTED', dropdown_index)
        return user_list
    
    def obtain_dropdown_options_in_section_visibility(self, dropdown_index: str) -> list:
        """Retrieves the available options from the dropdown"""
        dropdown_options = self.dropdown.get_available_options('DROPDOWN_LIST', dropdown_index)
        return dropdown_options
    
    def obtain_visible_element_in_section_visibility(self, dropdown_index: str) -> WebElement:
        """Retrieves the dropdown element"""
        element = self.dropdown.get_element('DROPDOWN_LIST', dropdown_index)
        return element

    def click_in_dropdown_in_section_visibility(self, dropdown_index: str):
        """Clicks in the dropdown of the sections visibility"""
        self.dropdown.click_dropdown('TEXT_BOX', dropdown_index)

    def type_name_user_from_dropdown_in_section_visibility(self, name: str, dropdown_index: str):
        """Types the name of a user in a dropdown of the sections visibility"""
        self.dropdown.type_characters_in_dropdown('INPUT_TEXT_BOX', name, dropdown_index)

    def delete_typed_name_from_dropdown_in_section_visibility(self, dropdown_index: str):
        """Deletes typed name from the dropdown of the sections visibility"""
        self.dropdown.delete_typed_characters_in_dropdown('INPUT_TEXT_BOX', dropdown_index)

    def obtain_typed_characters_from_dropdown_in_section_visibility(self, dropdown_index: str) -> str:
        """Retrieves the characters from the text box"""
        character = self.dropdown.get_characters_from_text_box('INPUT_TEXT_BOX', dropdown_index)
        self.delete_typed_name_from_dropdown_in_section_visibility(dropdown_index)
        return character

    def select_user_from_dropdown_in_section_visibility(self, user: str, dropdown_index: str):
        """Selects a user from the dropdown of the sections visibility"""
        self.dropdown.select_dropdown_option('SELECT_USER', user, dropdown_index)

    def delete_all_users_in_section_visibility(self, dropdown_index: str):
        """Deletes all name users from the dropdown of the sections visibility"""
        self.dropdown.delete_all_options('DELETE_ALL_USERS', dropdown_index=dropdown_index)
    
    def mouse_hover_delete_button_in_section_visibility(self, name: str, dropdown_index: str):
        """Performs a mouse hover action on the delete button associated with a specific user"""
        self.dropdown.move_mouse_to_delete_a_user('DELETE_ONE_USER', name, dropdown_index=dropdown_index)

    def obtain_message_empty_in_section_visibility(self, dropdown_index: str):
        """Gets the message when dropdown is empty of the sections visibility"""
        return self.dropdown.message_empty_in_dropdown('EMPTY_MESSAGE', dropdown_index)
    
    def obtain_message_in_empty_text_box_in_section_visibility(self, dropdown_index: str) -> str:
        """Retrieves the message displayed in an empty text box in the section visibility"""
        message = self.dropdown.message_in_dropdown_text_box('MESSAGE_IN_TEXT_BOX', dropdown_index)
        return message

    def delete_one_selected_user_in_dropdown_in_section_visibility(self, name: str, dropdown_index: str):
        """Delete one user from the dropdown of the sections visibility"""
        self.dropdown.delete_selected_option('DELETE_ONE_USER', name, dropdown_index)

    def delete_selected_users_in_dropdown_in_section_visibility(self, names: list, dropdown_index: str):
        """Delete users from the dropdown of the sections visibility"""
        for name in names:
            self.delete_one_selected_user_in_dropdown_in_section_visibility(name, dropdown_index)

    def scroll_to_user_in_section_visibility(self, name: str, dropdown_index: str):
        """Scroll and select a user of the sections visibility"""
        self.dropdown.scroll_down('SELECT_USER', name, dropdown_index)

    def click_dropdown_arrow_in_section_visibility(self, dropdown_index: str):
        """Clicks on dropdown arrow"""
        self.dropdown.click_drop_arrow('DROPDOWN_ARROW', dropdown_index)

    def add_user_to_section_visibility_by_typing_process_in_section_visibility(self, name: str, dropdown_index: str):
        """Adds a new user to section visibility process by typing the name"""
        self.type_name_user_from_dropdown_in_section_visibility(name, dropdown_index)
        self.select_user_from_dropdown_in_section_visibility(name, dropdown_index)

    def add_user_to_section_visibility_by_scrolling_process_in_section_visibility(self, name: str, dropdown_index: str):
        """Adds a new user to section visibility by scrolling to the name"""
        self.click_dropdown_arrow_in_section_visibility(dropdown_index)
        self.scroll_to_user_in_section_visibility(name, dropdown_index)
