from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Projects.ProjectTracing.Comments import section_add_comment_locators \
    as locators
from Libraries.Drivers.base_page import BasePage


class SectionAddComment(BasePage):
    """This class represents the section for write and add a new comment"""
    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self) -> WebElement:
        """Finds and returns text area for write a comment"""
        element = self.find_element.by_xpath(locators.COMMENTS_FIELD_TITLE)
        return element

    def get_text_area(self) -> WebElement:
        """Finds and returns text area for write a new comment"""
        element = self.find_element.by_xpath(locators.ADD_COMMENT_TEXT_AREA)
        return element

    def get_add_button(self) -> WebElement:
        """Finds and returns the "Add" button for post the new comment"""
        element = self.find_element.by_xpath(locators.ADD_COMMENT_BUTTON)
        return element
