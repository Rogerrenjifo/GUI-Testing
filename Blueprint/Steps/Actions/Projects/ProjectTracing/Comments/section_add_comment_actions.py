from selenium.webdriver import Keys
from Blueprint.PageObject.Projects.ProjectTracing.Comments.section_add_comment_objects \
    import SectionAddComment
from Blueprint.PageObject.Projects.ProjectTracing.Comments.comments_list_object import CommentsList
from Blueprint.PageObject.Projects.ProjectTracing.Comments.comment_objects import Comment
from Blueprint.Actions.CommonElements.popup_messages_actions import PopUpMessagesActions


class SectionAddCommentActions(SectionAddComment):
    """Represents the actions of the edit comment section in project tracing page"""
    def __init__(self):
        super().__init__()
        self.comments_list = CommentsList().comments_list
        self.pop_up_messages = PopUpMessagesActions()

    def obtain_comments_section_title(self) -> str:
        """Gets the text displayed  in the title"""
        title = self.get_title().text
        return title

    def add_text_to_add_comment_text_box(self, text: str):
        """Append text at the end of the textbox"""
        self.get_text_area().send_keys(Keys.END)
        self.get_text_area().send_keys(text)

    def delete_a_number_of_characters_in_add_comment_text_box(self, characters_number: int):
        """Delete a specific number of characters"""
        for character in range(int(characters_number)):
            self.get_text_area().send_keys(Keys.BACKSPACE)

    def delete_all_text_in_add_comment_text_box(self):
        """Delete all the content of the textbox"""
        self.get_text_area().clear()

    def click_on_add_button_of_add_comment_section(self):
        """Clicks on add button to post the comment"""
        self.get_add_button().click()
        index = len(self.comments_list) + 1
        self.comments_list.append(Comment(str(index)))

    def obtain_the_placeholder_of_add_comment_text_box(self) -> str:
        """Clicks on add button to post the comment"""
        placeholder = self.get_text_area().get_attribute("placeholder")
        return placeholder

    def obtain_add_button_disabled_attribute_of_add_comment_section(self) -> str:
        """Gets the status of the attribute "disabled" of the button add"""
        disabled = self.get_add_button().get_attribute("disabled")
        return disabled

    def click_on_close_button_in_add_comment_popup_message(self):
        """Selects the button for close the popup message"""
        self.pop_up_messages.click_to_close_popup_message()

    def obtain_text_of_add_comment_pop_up_message(self):
        """Gets the text displayed in the popup message"""
        pop_up_content = self.pop_up_messages.get_popup_message_text()
        return pop_up_content

    def obtain_color_of_add_comment_pop_up_message(self):
        """Gets the text displayed in the popup message"""
        pop_up_color = self.pop_up_messages.get_popup_message_color()
        return pop_up_color

    def add_new_comment_process(self, text: str):
        """Adds a new comment"""
        self.add_text_to_add_comment_text_box(text)
        self.click_on_add_button_of_add_comment_section()
