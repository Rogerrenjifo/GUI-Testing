from Libraries.Assertions.assertions import Verification
from Blueprint.Steps.Actions.Projects.new_request_actions import NewRequestActions

class NewProjectPage():
    """This clase represents the new project page verifications"""
    def __init__(self):
        super().__init__()
        self.new_page_project = NewRequestActions()
        self.verification = Verification()
        
    def option_should_be_equal(self, actual_result: str, expected_result: str):
        self.verification.verify_equal_ignore(actual_result, expected_result)
        