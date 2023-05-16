from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import publish_tab_locators as locators


class PublishTabObjects(BasePage):
    """This class represents the elements of publish tab in flow page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.__save_and_publish_button = locators.SAVE_AND_PUBLISH__BUTTON_LOCATOR

    def get_save_and_publish_button(self):
        """Returns the element of save and publish button"""
        element = self.find_element.by_xpath(self.__save_and_publish_button)
        return element
