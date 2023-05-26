from Blueprint.Actions.CommonElements.delete_dialog_actions import DeleteDialogActions
from Blueprint.PageObject.Projects.ProjectTracing.Comments.comments_list_object import CommentsList
from Blueprint.Actions.CommonElements.popup_messages_actions import PopUpMessagesActions


class DeleteDialogCommentActions(DeleteDialogActions):
    """Represents the actions of the "Delete comment" dialog in project tracing page"""
    def __init__(self):
        super().__init__()
        self.comments_list = CommentsList().comments_list
        self.pop_up_messages = PopUpMessagesActions()

    def click_on_delete_button_in_delete_comment_dialog(self, index: int = 0):
        """Clicks on "Delete" button for delete the comment"""
        self.click_delete_dialog_button()
        del self.comments_list[index]

    def click_on_cancel_button_in_delete_comment_dialog(self):
        """Clicks on "Cancel" button for close the dialog"""
        self.click_cancel_dialog_button()

    def click_on_close_button_in_delete_comment_dialog(self):
        """Clicks on "x" button for close the dialog"""
        self.click_close_dialog_button()

    def obtain_title_in_delete_comment_dialog(self) -> str:
        """Gets the text displayed  in the title of the dialog"""
        title = self.get_dialog_title_text()
        return title

    def obtain_question_in_delete_comment_dialog(self) -> str:
        """Gets the text displayed as description in the dialog"""
        description = self.get_dialog_question_text()
        return description

    def click_on_close_button_in_delete_comment_popup_message(self):
        """Selects the button for close the popup message"""
        self.pop_up_messages.click_to_close_popup_message()

    def obtain_text_of_delete_comment_pop_up_message(self):
        """Gets the text displayed in the popup message"""
        pop_up_content = self.pop_up_messages.get_popup_message_text()
        return pop_up_content

    def obtain_color_of_delete_comment_pop_up_message(self):
        """Gets the text displayed in the popup message"""
        pop_up_color = self.pop_up_messages.get_popup_message_color()
        return pop_up_color
