from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Flows import flow_permissions_locators as locators
from Libraries.Drivers.base_page import BasePage


class FlowPermissions(BasePage):
    """This class represents the flow permission of a Blueprint application"""
    def __init__(self, driver):
        super().__init__(driver)
        self.__title_flow_permissions = locators.TITLE_FLOW_PERMISSIONS
        self.__title_all_versions = locators.TITLE_ALL_VERSIONS
        self.__subtitle_flow_admin = locators.SUBTITLE_FLOW_ADMIN
        self.__empty_dropdownbox_message = locators.EMPTY_DROPDOWNBOX_MESSAGE
        self.__dropdownbox = locators.DROPDOWNBOX
        self.__save_button = locators.SAVE_BUTTON
        self.__scroll_bar = locators.SCROLL_BAR
        self.__permissions_tab = locators.PERMISSIONS_BUTTON

    def get_permissions_tab(self) -> WebElement:
        """Finds and returns the permissions tab object"""
        element = self.find_element.by_xpath(self.__permissions_tab)
        return element

    def get_title_flow_permissions(self) -> WebElement:
        """Finds and returns the flow permissions title object"""
        element = self.find_element.by_xpath(self.__title_flow_permissions)
        return element

    def get_title_all_versions(self) -> WebElement:
        """Finds and returns the all versions title object"""
        element = self.find_element.by_xpath(self.__title_all_versions)
        return element

    def get_subtitle_flow_admin(self) -> WebElement:
        """Finds and returns the flow admin subtitle object"""
        element = self.find_element.by_xpath(self.__subtitle_flow_admin)
        return element

    def get_empty_dropdownbox_message(self) -> WebElement:
        """Finds and returns the message when dropdownbox is empty object"""
        element = self.find_element.by_xpath(self.__empty_dropdownbox_message)
        return element

    def get_dropdown_box_narrow(self) -> WebElement:
        """Finds and returns the dropdownbox narrow object"""
        element = self.find_element.by_xpath(self.__dropdownbox)
        return element

    def get_save_button(self) -> WebElement:
        """Finds and returns the save button object"""
        element = self.find_element.by_xpath(self.__save_button)
        return element

    def get_scroll_bar(self) -> WebElement:
        """Finds and returns the scroll-bar object"""
        element = self.find_element.by_xpath(self.__scroll_bar)
        return element
