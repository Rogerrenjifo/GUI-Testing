from Blueprint.PageObject.CommonElements.delete_dialog_objects import DeleteDialogObjects


class DeleteDialogActions(DeleteDialogObjects):
    """This class represents the actions of the Delete Dialog in Blueprint page."""
       
    def click_cancel_dialog_button(self):
        """Clicks on the Cancel button of the delete dialog."""
        cancel = self.get_cancel_dialog_button()
        cancel.click()

    def click_delete_dialog_button(self):
        """Clicks on the Delete button of the delete dialog."""
        delete = self.get_delete_dialog_button()
        delete.click()

    def click_close_dialog_button(self):
        """Clicks on the close button of the delete dialog."""
        close = self.get_close_dialog_button()
        close.click()

    def get_dialog_title_text(self) -> str:
        """Gets the title text of the delete dialog."""
        title_text = self.get_dialog_title().text
        return title_text
    
    def get_dialog_question_text(self) -> str:
        """Gets the question text of the delete dialog."""
        question_text = self.get_dialog_question().text
        return question_text
