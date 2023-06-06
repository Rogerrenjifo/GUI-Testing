from Blueprint.Steps.Actions.CommonElements.delete_dialog_actions import DeleteDialogActions
from Libraries.Assertions.assertions import Verification


class DeleteDialogVerifications:
    """This class represents the verifications of the delete dialog"""
    def __init__(self):        
        self.verification = Verification()
        self.delete_dialog = DeleteDialogActions()

    def delete_dialog_should_be_displayed(self):
        """Verifies that the delete dialog is displayed."""        
        self.verification.verify_element_is_displayed(self.delete_dialog.get_delete_dialog())

    def delete_dialog_title_should_be_displayed(self):
        """Verifies that the title of delete dialog is displayed."""        
        self.verification.verify_element_is_displayed(self.delete_dialog.get_dialog_title())

    def delete_dialog_question_should_be_displayed(self):
        """Verifies that the question text of delete dialog is displayed."""        
        self.verification.verify_element_is_displayed(self.delete_dialog.get_dialog_question())

    def delete_dialog_close_button_should_be_displayed(self):
        """Verifies that the close button of delete dialog is displayed."""        
        self.verification.verify_element_is_displayed(self.delete_dialog.get_close_dialog_button())
    
    def delete_dialog_cancel_button_should_be_displayed(self):
        """Verifies that the cancel button of delete dialog is displayed."""        
        self.verification.verify_element_is_displayed(self.delete_dialog.get_cancel_dialog_button())

    def delete_dialog_delete_button_should_be_displayed(self):
        """Verifies that the delete button of delete dialog is displayed."""        
        self.verification.verify_element_is_displayed(self.delete_dialog.get_delete_dialog_button())

    def delete_dialog_title_text_should_be_equal(self, expected_title_text: str):
        """Verifies that the text of the title is the expected in the delete dialog."""
        actual_title_text = self.delete_dialog.get_dialog_title_text()
        self.verification.verify_equal_ignore(actual_title_text, expected_title_text)

    def delete_dialog_question_text_should_be_equal(self, expected_question_text: str):
        """Verifies that the text of the question is the expected in the delete dialog."""
        actual_question_text = self.delete_dialog.get_dialog_question_text()
        self.verification.verify_equal_ignore(actual_question_text, expected_question_text)
