from selenium.webdriver import Keys
from Blueprint.PageObject.Projects.ProjectTracing.Comments.comment_objects import Comment
from Blueprint.PageObject.Projects.ProjectTracing.Comments.comments_list_object import CommentsList
from robot.api import logger
from Blueprint.Steps.Actions.CommonElements.popup_messages_actions import PopUpMessagesActions
from Blueprint.Steps.Actions.CommonElements.delete_dialog_actions import DeleteDialogActions


class CommentActions(Comment):
    """Represents the actions of the edit comment section in project tracing page"""
    def __init__(self):
        super().__init__()
        self.comment_list = CommentsList().comments_list
        self.pop_up_messages = PopUpMessagesActions()
        self.delete_dialog = DeleteDialogActions()

    def identify_own_comments(self, owner: str, content: str = None, index: int = 0) -> bool:
        """Compare the given username with the displayed in the comment"""
        if self.obtain_owner_of_a_comment(content, index) == owner:
            return True
        else:
            return False

    def obtain_content_of_a_comment(self, index: int = 0) -> str:
        """Gets the text displayed as comment content"""
        content = self.comment_list[index].get_comment_content().text
        return content

    def obtain_owner_of_a_comment(self, content: str = None, index: int = 0) -> str:
        """Gets the text displayed as owner name above the comment"""
        if content is None:
            owner = self.comment_list[index].get_owner_name().text
        else:
            owner = self.get_owner_name(content).text
        return owner

    def obtain_date_of_a_comment(self, content: str = None, index: int = 0) -> str:
        """Gets the text displayed as date above the comment"""
        if content is None:
            date = self.comment_list[index].get_date().text
        else:
            date = self.get_date(content).text
        return date

    def obtain_owner_initials_of_a_comment(self, content: str = None, index: int = 0) -> str:
        """Gets the text displayed as owner initials above the comment"""
        if content is None:
            owner_initials = self.comment_list[index].get_owner_initials().text
        else:
            owner_initials = self.get_owner_initials(content).text
        return owner_initials

    def click_on_edit_button_of_a_comment(self, owner: str, content:str = None, index: int = 0):
        """Clicks on edit comment button"""
        own_comment = self.identify_own_comments(owner, content, index)
        if own_comment is True:
            if content is None:
                self.comment_list[index].get_edit_button().click()
            else:
                self.get_edit_button(content).click()
        else:
            logger.info("You can not edit other users' comment")

    def click_on_delete_button_of_a_comment(self, owner: str, content: str = None, index: int = 0):
        """Clicks on delete comment button"""
        own_comment = self.identify_own_comments(owner, content, index)
        if own_comment is True:
            if content is None:
                self.comment_list[index].get_delete_button().click()
            else:
                self.get_delete_button(content).click()
        else:
            logger.info("You can not delete other users' comment")

    def obtain_edited_tag_of_a_comment(self, content: str = None, index: int = 0) -> str:
        """Gets the text that indicating that the commentary was edited"""
        if content is None:
            tag = self.comment_list[index].get_edited_tag().text
        else:
            tag = self.get_edited_tag(content).text
        return tag

    def add_text_to_edit_comment_text_box(self, text: str, index_edit_box: str = "1"):
        """Append text at the end of the textbox"""
        self.get_text_area(index_edit_box).send_keys(Keys.END)
        self.get_text_area(index_edit_box).send_keys(text)

    def delete_a_number_of_characters_to_edit_comment_text_box(self, characters_number: int, index_edit_box: str = "1"):
        """Delete a specific number of characters"""
        for character in range(int(characters_number)):
            self.get_text_area(index_edit_box).send_keys(Keys.BACKSPACE)

    def delete_all_text_to_edit_comment_text_box(self, index_edit_box: str = "1"):
        """Delete the content of the textbox"""
        self.get_text_area(index_edit_box).clear()

    def click_on_update_button_of_edit_comment_section(self, index: int = 0, index_edit_box: str = "1"):
        """Clicks on "Update" button edit the comment"""
        self.get_update_button(index_edit_box).click()
        self.comment_list[index] = Comment(str(index + 1))

    def click_on_cancel_button_of_edit_comment_section(self, index: int = 0, index_edit_box: str = "1"):
        """Clicks on "Cancel" button for close the edit process"""
        self.get_cancel_button(index_edit_box).click()
        self.comment_list[index] = Comment(str(index + 1))

    def obtain_update_button_disabled_attribute_of_edit_comment_section(self) -> str:
        """Gets the status of the attribute "disabled" of the button update"""
        disabled = self.get_text_area().get_attribute("disabled")
        return disabled

    def click_on_close_button_in_edit_comment_popup_message(self):
        """Selects the button for close the popup message"""
        self.pop_up_messages.click_to_close_popup_message()

    def obtain_text_of_edit_comment_pop_up_message(self):
        """Gets the text displayed in the popup message"""
        pop_up_content = self.pop_up_messages.get_popup_message_text()
        return pop_up_content

    def obtain_color_of_edit_comment_pop_up_message(self):
        """Gets the text displayed in the popup message"""
        pop_up_color = self.pop_up_messages.get_popup_message_color()
        return pop_up_color

    def click_on_delete_button_in_delete_comment_dialog(self, index: int = 0):
        """Clicks on "Delete" button for delete the comment"""
        self.delete_dialog.click_delete_dialog_button()
        del self.comment_list[index]

    def click_on_cancel_button_in_delete_comment_dialog(self):
        """Clicks on "Cancel" button for close the dialog"""
        self.delete_dialog.click_cancel_dialog_button()

    def click_on_close_button_in_delete_comment_dialog(self):
        """Clicks on "x" button for close the dialog"""
        self.delete_dialog.click_close_dialog_button()

    def obtain_title_in_delete_comment_dialog(self) -> str:
        """Gets the text displayed  in the title of the dialog"""
        title = self.delete_dialog.get_dialog_title_text()
        return title

    def obtain_question_in_delete_comment_dialog(self) -> str:
        """Gets the text displayed as description in the dialog"""
        description = self.delete_dialog.get_dialog_question_text()
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

    def edit_full_comment_by_index_process(self, new_content: str, owner: str, index: int = 0):
        """Edits all the text of a comment selected by its index"""
        self.click_on_edit_button_of_a_comment(owner=owner, index=index)
        self.delete_all_text_to_edit_comment_text_box()
        self.add_text_to_edit_comment_text_box(new_content)
        self.click_on_update_button_of_edit_comment_section()

    def edit_full_comment_by_content_process(self, new_content: str, owner: str, existent_content: str):
        """Edits all the text of a comment selected by its content"""
        self.click_on_edit_button_of_a_comment(owner=owner, content=existent_content)
        self.delete_all_text_to_edit_comment_text_box()
        self.add_text_to_edit_comment_text_box(new_content)
        self.click_on_update_button_of_edit_comment_section()

    def edit_partially_comment_by_index_process(self, new_content: str, number_characters: int, owner: str, index: int = 0):
        """Edits part of the text of a comment selected by its index"""
        self.click_on_edit_button_of_a_comment(owner=owner, index=index)
        self.delete_a_number_of_characters_to_edit_comment_text_box(characters_number=number_characters)
        self.add_text_to_edit_comment_text_box(new_content)
        self.click_on_update_button_of_edit_comment_section()

    def edit_partially_comment_by_content_process(self, new_content: str, number_characters: int, owner: str, existent_content: str):
        """Edits part of the text of a comment selected by its content"""
        self.click_on_edit_button_of_a_comment(owner=owner, content=existent_content)
        self.delete_a_number_of_characters_to_edit_comment_text_box(characters_number=number_characters)
        self.add_text_to_edit_comment_text_box(new_content)
        self.click_on_update_button_of_edit_comment_section()

    def delete_comment_by_index_process(self, owner: str, index: int):
        """Deletes a comment from the list of comments selected by its index"""
        self.click_on_delete_button_of_a_comment(owner=owner, index=index)
        self.click_on_delete_button_in_delete_comment_dialog()

    def delete_comment_by_content_process(self, owner: str, existent_content: str):
        """Deletes a comment from the list of comments selected by its content"""
        self.click_on_delete_button_of_a_comment(owner=owner, content=existent_content)
        self.click_on_delete_button_in_delete_comment_dialog()

    def cancel_delete_comment_by_index_process(self, owner: str, index: int):
        """Cancels the process of delete a comment selected by its index"""
        self.click_on_delete_button_of_a_comment(owner=owner, index=index)
        self.click_on_cancel_button_in_delete_comment_dialog()

    def cancel_delete_comment_by_content_process(self, owner: str, existent_content: str):
        """Cancels the process of delete a comment selected by its content"""
        self.click_on_delete_button_of_a_comment(owner=owner, content=existent_content)
        self.click_on_cancel_button_in_delete_comment_dialog()

    def close_delete_comment_by_index_process(self, owner: str, index: int):
        """Closes the process of delete a comment selected by its index"""
        self.click_on_delete_button_of_a_comment(owner=owner, index=index)
        self.click_on_close_button_in_delete_comment_dialog()

    def close_delete_comment_by_content_process(self, owner: str, existent_content: str):
        """Closes the process of delete a comment selected by its content"""
        self.click_on_delete_button_of_a_comment(owner=owner, content=existent_content)
        self.click_on_close_button_in_delete_comment_dialog()
