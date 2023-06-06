from Blueprint.Steps.Actions.Flows.process_permissions_actions import ProcessPermissionsActions
from Libraries.Assertions.assertions import Verification


class ProcessPermissionsVerifications:
    """This class represents the verifications of the Flow Admin Permissions section"""
    def __init__(self):        
        self.actions = ProcessPermissionsActions()
        self.verification = Verification()

    def users_selected_list_process_permissions_should_contain(self, name: str):
        """Verifies that the users selected list contains a user"""
        users_list = self.actions.obtain_user_list_selected_in_text_box_in_process_permissions()
        self.verification.verify_a_list_contains(users_list, name)
