from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import publish_tab_locators as locators


class PublishTabObjects(BasePage):
    """This class represents the elements of publish tab in flow page."""

    def get_save_and_publish_button(self) -> WebElement:
        """Returns the element of save and publish button."""
        element = self.find_element.by_xpath(locators.SAVE_AND_PUBLISH__BUTTON_LOCATOR)
        return element
