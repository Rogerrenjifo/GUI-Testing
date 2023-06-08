import time
from Blueprint.Steps.Actions.Flows.section_visibility_permissions_actions import SectionsVisibilityActions
from Libraries.Assertions.assertions import Verification


class SectionsVisibilityVerifications:
    """This class represents the verifications of the Flow Admin Permissions section"""
    def __init__(self):        
        self.actions = SectionsVisibilityActions()
        self.verification = Verification()

    def the_rgb_color_of_label_should_be_as_expected(self, expected_color: str, dropdown_index: str):
        """Verifies that the rgb color of label is displayed in the expected color"""
        actual_color = self.actions.obtain_rgb_color_of_label_in_section_visibility(dropdown_index)
        self.verification.verify_equal_ignore(actual_color, expected_color)

    def the_rgb_color_of_text_box_should_be_as_expected(self, expected_color: str, dropdown_index: str):
        """Verifies that the rgb color of text box is displayed in the expected color"""
        actual_color = self.actions.obtain_rgb_color_of_text_box_in_section_visibility(dropdown_index)
        self.verification.verify_equal_ignore(actual_color, expected_color)

    def the_rgb_color_of_delete_button_should_as_expected(self, name: str, expected_color: str, dropdown_index: str):
        """Verifies that the rgb color of delete button is displayed in the expected color"""
        actual_color = self.actions.obtain_rgb_color_of_delete_button_in_section_visibility(name, dropdown_index)
        self.verification.verify_equal_ignore(actual_color, expected_color)

    def users_selected_list_in_section_visibility_should_contain(self, name: str, dropdown_index: str):
        """Verifies that the users selected list contains a user"""
        time.sleep(2)
        users_list = self.actions.obtain_user_list_selected_in_text_box_in_section_visibility(dropdown_index)
        self.verification.verify_a_list_contains(users_list, name)
    
    def users_selected_list_in_section_visibility_should_not_contain(self, name: str, dropdown_index: str):
        """Verifies that the users selected list does not contain a user"""
        users_list = self.actions.obtain_user_list_selected_in_text_box_in_section_visibility(dropdown_index)
        self.verification.verify_a_list_does_not_contain(users_list, name)

    def users_selected_list_in_section_visibility_should_be_empty(self, dropdown_index: str):
        """Verifies that the users selected list is empty"""
        users_list = self.actions.obtain_user_list_selected_in_text_box_in_section_visibility(dropdown_index)
        self.verification.verify_a_list_is_empty(users_list)

    def dropdown_in_section_visibility_should_contain(self, name: str, dropdown_index: str):
        """Verifies that the dropdown contains a user or group"""
        dropdown_options = self.actions.obtain_dropdown_options_in_section_visibility(dropdown_index)
        self.verification.verify_a_list_contains(dropdown_options, name)

    def dropdown_in_section_visibility_should_not_contain(self, name: str, dropdown_index: str):
        """Verifies that the dropdown does not contain a user or group"""
        dropdown_options = self.actions.obtain_dropdown_options_in_section_visibility(dropdown_index)
        self.verification.verify_a_list_does_not_contain(dropdown_options, name)

    def message_in_empty_text_box_in_section_visibility_should_be_as_expected(self, expected_message: str, dropdown_index: str):
        """Verifies that the message in the empty text box is displayed as expected"""
        actual_message = self.actions.obtain_message_in_empty_text_box_in_section_visibility(dropdown_index)
        self.verification.verify_equal_ignore(actual_message, expected_message)

    def message_empty_dropdow_in_section_visibility_should_be_as_expected(self, expected_message: str, dropdown_index: str):
        """Verifies that the message is displayed as expected when the text box is empty"""
        actual_message = self.actions.obtain_message_empty_in_section_visibility(dropdown_index)
        self.verification.verify_equal_ignore(actual_message, expected_message)

    def dropdown_in_section_visibility_should_be_visible(self, dropdown_index: str):
        """Verifies that the dropdown is visible"""
        dropdown = self.actions.obtain_visible_element_in_section_visibility(dropdown_index)
        self.verification.verify_is_not_equal(dropdown, False)

    def dropdown_in_section_visibility_should_not_be_visible(self, dropdown_index: str):
        """Verifies that the dropdown is not visible"""
        dropdown = self.actions.obtain_visible_element_in_section_visibility(dropdown_index)
        self.verification.verify_equal_ignore(dropdown, False)

    def text_box_in_section_visibility_should_not_be_empty(self, dropdown_index: str):
        """Verifies that the text box is not empty"""
        result = self.actions.obtain_typed_characters_from_dropdown_in_section_visibility(dropdown_index)
        self.verification.verify_a_list_is_not_empty(result)
