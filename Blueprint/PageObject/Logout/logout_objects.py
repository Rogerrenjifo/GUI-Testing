from Blueprint.Locators.Logout import logout_locators as locators
from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage


class Logout(BasePage):
    """This class represents the logout elements of the application"""

    def get_username(self) -> WebElement:
        """Finds and returns the username displayed in the logout menu"""
        element = self.find_element.by_xpath(locators.USER_NAME)
        return element

    def get_profile_button(self) -> WebElement:
        """Finds and returns the profile button that display the logout menu"""
        element = self.find_element.by_class(locators.PROFILE_BUTTON)
        return element
