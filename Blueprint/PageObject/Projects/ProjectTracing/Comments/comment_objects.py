from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Projects.ProjectTracing.Comments import comment_locators as locators
from Libraries.Drivers.base_page import BasePage


class Comment(BasePage):
    """This class represents a published comment in project-tracing page"""
    def __init__(self, index: str = "1"):
        super().__init__()
        self.index = index

    def get_content_xpath(self, content: str = None) -> str:
        """Returns the xpath of the comment depending on index or content"""
        if content is None:
            xpath = f"({locators.COMMENT_CONTENT['by_index']})[{str(self.index)}]"
        else:
            xpath = f"{locators.COMMENT_CONTENT['by_content'].replace('<<value>>', content)}"
        return xpath

    def get_date(self, content: str = None) -> WebElement:
        """Finds and returns the comment publish date"""
        xpath = self.get_content_xpath(content) + locators.COMMENT_DATE
        element = self.find_element.by_xpath(xpath)
        return element

    def get_comment_content(self) -> WebElement:
        """Finds and returns the comment content"""
        element = self.find_element.by_xpath(self.get_content_xpath())
        return element

    def get_owner_name(self, content: str = None) -> WebElement:
        """Finds and returns the owner username"""
        xpath = self.get_content_xpath(content) + locators.COMMENT_OWNER_NAME
        element = self.find_element.by_xpath(xpath)
        return element

    def get_owner_initials(self, content: str = None) -> WebElement:
        """Finds and returns the owner initials in the user avatar"""
        xpath = self.get_content_xpath(content) + locators.COMMENT_OWNER_INITIALS
        element = self.find_element.by_xpath(xpath)
        return element

    def get_edit_button(self, content: str = None) -> WebElement:
        """Finds and returns the "Edit" button that display the edit area"""
        xpath = self.get_content_xpath(content) + locators.EDIT_COMMENT_BUTTON
        element = self.find_element.by_xpath(xpath)
        return element

    def get_delete_button(self, content: str = None) -> WebElement:
        """Finds and returns the "Delete" button that display the delete dialog"""
        xpath = self.get_content_xpath(content) + locators.DELETE_COMMENT_BUTTON
        element = self.find_element.by_xpath(xpath)
        return element

    def get_edited_tag(self, content: str = None) -> WebElement:
        """Finds and returns tag "Edited" in a comment"""
        xpath = self.get_content_xpath(content) + locators.COMMENT_EDITED_TAG
        element = self.find_element.by_xpath(xpath)
        return element

    def get_text_area(self, index: str = "1") -> WebElement:
        """Finds and returns the text area for edit a comment"""
        element = self.find_element.by_xpath(f"({locators.EDIT_COMMENT_TEXT_AREA})[{str(index)}]")
        return element

    def get_cancel_button(self, index: str = "1") -> WebElement:
        """Finds and returns the "Cancel" button for cancel the edit process"""
        element = self.find_element.by_xpath(f"({locators.CANCEL_COMMENT_BUTTON})[{str(index)}]")
        return element

    def get_update_button(self, index: str = "1") -> WebElement:
        """Finds and returns the "Update" button for edit a comment"""
        element = self.find_element.by_xpath(f"({locators.UPDATE_COMMENT_BUTTON})[{str(index)}]")
        return element
