from Blueprint.Steps.Actions.Flows.overwrite_dialog_actions import OverwriteDraftDialogActions
from Libraries.Assertions.assertions import Verification


class OverwriteDraftDialogVerifications:
    """This class represents the verifications of the overwrite draft dialog"""
    def __init__(self):        
        self.verification = Verification()
        self.overwrite_draft_dialog = OverwriteDraftDialogActions()

    def overwrite_draft_dialog_should_be_displayed(self):
        """Verifies that the overwrite draft dialog is displayed."""        
        self.verification.verify_element_is_displayed(self.overwrite_draft_dialog.get_overwrite_dialog())

    def overwrite_draft_should_not_be_displayed(self):
        """Verifies that the overwrite draft dialog is not displayed."""
        self.verification.verify_equal_ignore(self.overwrite_draft_dialog.get_overwrite_dialog(),False)

    def overwrite_draft_title_should_be_displayed(self):
        """Verifies that the title of the overwrite draft dialog is displayed."""        
        self.verification.verify_element_is_displayed(self.overwrite_draft_dialog.get_overwrite_dialog_title())

    def overwrite_draft_question_should_be_displayed(self):
        """Verifies that the question text of the overwrite draft dialog is displayed."""        
        self.verification.verify_element_is_displayed(self.overwrite_draft_dialog.get_overwrite_dialog_question())

    def overwrite_draft_dialog_close_button_should_be_displayed(self):
        """Verifies that the close button of the overwrite draft dialog is displayed."""        
        self.verification.verify_element_is_displayed(self.overwrite_draft_dialog.get_overwrite_dialog_close_button())
    
    def overwrite_draft_dialog_cancel_button_should_be_displayed(self):
        """Verifies that the cancel button of the overwrite draft dialog is displayed."""        
        self.verification.verify_element_is_displayed(self.overwrite_draft_dialog.get_overwrite_dialog_cancel_button())

    def overwrite_draft_dialog_confirm_button_should_be_displayed(self):
        """Verifies that the confirm button of the overwrite draft dialog is displayed."""        
        self.verification.verify_element_is_displayed(self.overwrite_draft_dialog.get_overwrite_dialog_confirm_button())

    def overwrite_draft_dialog_title_text_should_be_equal(self, expected_title_text: str):
        """Verifies that the text of the title is the expected in the overwrite draft dialog."""
        actual_title_text = self.overwrite_draft_dialog.get_title_text_in_overwrite_draft_dialog()
        self.verification.verify_equal_ignore(actual_title_text, expected_title_text)

    def overwrite_draft_dialog_question_text_should_be_equal(self, expected_question_text: str):
        """Verifies that the text of the question is the expected in the overwrite draft dialog."""
        actual_question_text = self.overwrite_draft_dialog.get_question_text_in_overwrite_draft_dialog()
        self.verification.verify_equal_ignore(actual_question_text, expected_question_text)
