from Blueprint.Steps.Actions.Flows.section_visibility_permissions_actions import SectionsVisibilityActions
from Libraries.Assertions.assertions import Verification


class SectionsVisibilityVerifications:
    """This class represents the verifications of the Flow Admin Permissions section"""
    def __init__(self):        
        self.actions = SectionsVisibilityActions()
        self.verification = Verification()

    def users_selected_list_in_section_visibility_should_contain(self, name: str, dropdown_index: str):
        """Verifies that the users selected list contains a user"""
        users_list = self.actions.obtain_user_list_selected_in_text_box_in_section_visibility(dropdown_index)
        self.verification.verify_a_list_contains(users_list, name)
