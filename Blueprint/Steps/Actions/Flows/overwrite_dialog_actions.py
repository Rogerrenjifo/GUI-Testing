from Blueprint.PageObject.Flows.overwrite_draft_objects import OverwriteDraftDialogObjects


class OverwriteDraftDialogActions(OverwriteDraftDialogObjects):
    """This class represents the actions of the Overwrite Draft Dialog in flows page."""
       
    def click_cancel_button_in_overwrite_draft_dialog(self):
        """Clicks on the Cancel button of the Overwrite draft dialog."""
        cancel = self.get_overwrite_dialog_cancel_button()
        cancel.click()

    def click_confirm_button_in_overwrite_draft_dialog(self):
        """Clicks on the Confirm button of the Overwrite draft dialog."""
        confirm = self.get_overwrite_dialog_confirm_button()
        confirm.click()

    def click_close_button_in_overwrite_draft_dialog(self):
        """Clicks on the close button of the Overwrite draft dialog."""
        close = self.get_overwrite_dialog_close_button()
        close.click()

    def get_title_text_in_overwrite_draft_dialog(self) -> str:
        """Gets the title text of the Overwrite draft dialog."""
        title_text = self.get_overwrite_dialog_title().text
        return title_text
    
    def get_question_text_in_overwrite_draft_dialog(self) -> str:
        """Gets the question text of the Overwrite draft dialog."""
        question_text = self.get_overwrite_dialog_question().text
        return question_text
