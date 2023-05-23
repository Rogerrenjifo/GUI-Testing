from Blueprint.PageObject.Projects.ProjectTracing.Comments.delete_dialog_objects \
    import DeleteCommentDialog
from Blueprint.PageObject.Projects.ProjectTracing.Comments.comments_list_object import CommentsList
from Blueprint.Actions.elements.PopupMessages.popup_messages_actions import PopUpMessagesActions


class DialogDeleteCommentActions(DeleteCommentDialog):
    """Represents the actions of the "Delete comment" dialog in project tracing page"""
    def __init__(self, comments_list: CommentsList):
        super().__init__()
        self.comments_list = comments_list
        self.pop_up_messages = PopUpMessagesActions()

    def select_delete_button(self, index: int = 0):
        """Clicks on "Delete" button for delete the comment"""
        self.get_delete_button().click()
        del self.comments_list[index]

    def select_cancel_button(self):
        """Clicks on "Cancel" button for close the dialog"""
        self.get_cancel_button().click()

    def select_x_button(self):
        """Clicks on "x" button for close the dialog"""
        self.get_x_button().click()

    def obtain_title(self) -> str:
        """Gets the text displayed  in the title of the dialog"""
        title = self.get_title().text
        return title

    def obtain_description(self) -> str:
        """Gets the text displayed as description in the dialog"""
        description = self.get_description().text
        return description

    def close_pop_up(self):
        """Select the button for close the popup message"""
        self.pop_up_messages.click_close_popup_message()

    def obtain_pop_up_text(self):
        """Gets the text displayed in the popup message"""
        pop_up_content = self.pop_up_messages.get_popup_messages().text
        return pop_up_content
