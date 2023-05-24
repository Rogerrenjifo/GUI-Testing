from selenium.webdriver import Keys
from Blueprint.PageObject.Projects.ProjectTracing.Comments.comment_objects import Comment
from Blueprint.PageObject.Projects.ProjectTracing.Comments.comments_list_object import CommentsList
from robot.api import logger
from Blueprint.Actions.elements.PopupMessages.popup_messages_actions import PopUpMessagesActions


class CommentActions(Comment):
    """Represents the actions of the edit comment section in project tracing page"""
    def __init__(self, owner:str, comment_list: CommentsList):
        super().__init__()
        
        self.comment_list = comment_list
        self.owner = owner
        self.pop_up_messages = PopUpMessagesActions()

    def identify_own_comments(self, content: str = None, index: int = 0) -> bool:
        """Compare the given username with the displayed in the comment"""
        if self.obtain_owner(content, index) == self.owner:
            return True
        else:
            return False

    def obtain_content(self, index: int = 0) -> str:
        """Gets the text displayed as comment content"""
        content = self.comment_list[index].get_comment_content().text
        return content

    def obtain_owner(self, content: str = None, index: int = 0) -> str:
        """Gets the text displayed as owner name above the comment"""
        if content is None:
            owner = self.comment_list[index].get_owner_name().text
        else:
            owner = self.get_owner_name(content).text
        return owner

    def obtain_date(self, content: str = None, index: int = 0) -> str:
        """Gets the text displayed as date above the comment"""
        if content is None:
            date = self.comment_list[index].get_date().text
        else:
            date = self.get_date(content).text
        return date

    def obtain_owner_initials(self, content: str = None, index: int = 0) -> str:
        """Gets the text displayed as owner initials above the comment"""
        if content is None:
            owner_initials = self.comment_list[index].get_owner_initials().text
        else:
            owner_initials = self.get_owner_initials(content).text
        return owner_initials

    def select_edit_button(self, content:str = None, index: int = 0):
        """Clicks on edit comment button"""
        own_comment = self.identify_own_comments(content, index)
        if own_comment is True:
            if content is None:
                self.comment_list[index].get_edit_button().click()
            else:
                self.get_edit_button(content).click()
        else:
            logger.info("You can not edit other users' comment")

    def select_delete_button(self, content: str = None, index: int = 0):
        """Clicks on delete comment button"""
        own_comment = self.identify_own_comments(content, index)
        if own_comment is True:
            if content is None:
                self.comment_list[index].get_delete_button().click()
            else:
                self.get_delete_button(content).click()
        else:
            logger.info("You can not delete other users' comment")

    def obtain_edited_tag(self, content: str = None, index: int = 0) -> str:
        """Gets the text that indicating that the commentary was edited"""
        if content is None:
            tag = self.comment_list[index].get_edited_tag().text
        else:
            tag = self.get_edited_tag(content).text
        return tag

    def add_text(self, text: str, index_edit_box: str = "1"):
        """Append text at the end of the textbox"""
        self.get_text_area(index_edit_box).send_keys(Keys.END)
        self.get_text_area(index_edit_box).send_keys(text)

    def delete_a_number_of_characters(self, characters_number: int, index_edit_box: str = "1"):
        """Delete a specific number of characters"""
        for character in range(int(characters_number)):
            self.get_text_area(index_edit_box).send_keys(Keys.BACKSPACE)

    def delete_text(self, index_edit_box: str = "1"):
        """Delete the content of the textbox"""
        self.get_text_area(index_edit_box).clear()

    def select_update_button(self, index: int = 0, index_edit_box: str = "1"):
        """Clicks on "Update" button edit the comment"""
        self.get_update_button(index_edit_box).click()
        self.comment_list[index] = Comment(str(index + 1))

    def select_cancel_button(self, index: int = 0, index_edit_box: str = "1"):
        """Clicks on "Cancel" button for close the edit process"""
        self.get_cancel_button(index_edit_box).click()
        self.comment_list[index] = Comment(str(index + 1))

    def obtain_update_button_disabled_attribute(self) -> str:
        """Gets the status of the attribute "disabled" of the button update"""
        disabled = self.get_text_area().get_attribute("disabled")
        return disabled

    def close_pop_up(self):
        """Select the button for close the popup message"""
        self.pop_up_messages.click_close_popup_message()

    def obtain_pop_up_text(self):
        """Gets the text displayed in the popup message"""
        pop_up_content = self.pop_up_messages.get_popup_messages().text
        return pop_up_content
