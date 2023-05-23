from Blueprint.Locators.Projects.ProjectTracing.Comments import comment_locators as locators
from Libraries.Drivers.base_page import BasePage
from Blueprint.PageObject.Projects.ProjectTracing.Comments.comment_objects import Comment


class CommentsList(BasePage):
    """This class represents the all the comments displayed in project tracing page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.comments_list = self.get_existing_comments()

    def get_existing_comments(self) -> list:
        """Generates a list with all the comment objects existing"""
        comments_list = []
        comments_len = len(self.find_elements.by_xpath(locators.COMMENT_OWNER_NAME))+1
        for comment_number in range(1, comments_len):
            comments_list.append(Comment(self.driver, str(comment_number)))
        return comments_list
