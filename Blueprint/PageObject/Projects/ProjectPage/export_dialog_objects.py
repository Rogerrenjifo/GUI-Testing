from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Projects.ProjectPage import export_dialog_locators as locators
from Libraries.Drivers.base_page import BasePage


class ExportDialogObjects(BasePage):
    """This class represents the export dialog in Blueprint."""

    def get_export_dialog(self) -> WebElement:
        """Finds and returns the Export dialog."""
        element = self.find_element.by_xpath(locators.EXPORT_DIALOG)
        return element

    def get_export_dialog_father_container(self) -> WebElement:
        """Finds and returns the Export dialog father container."""
        element = self.find_element.by_xpath(locators.EXPORT_DIALOG_CONTAINER)
        return element

    def get_cancel_export_dialog_button(self) -> WebElement:
        """Finds and returns the Cancel button element of the Export dialog."""
        element = self.find_element.by_xpath(locators.EXPORT_DIALOG_CANCEL_BUTTON)
        return element

    def get_export_dialog_button(self) -> WebElement:
        """Finds and returns the Export button element of the Export Process dialog."""
        element = self.find_element.by_xpath(locators.EXPORT_DIALOG_BUTTON)
        return element

    def get_close_export_dialog_button(self) -> WebElement:
        """Finds and returns the close button element of the Export Process dialog."""
        element = self.find_element.by_xpath(locators.EXPORT_DIALOG_CLOSE_BUTTON)
        return element

    def get_export_dialog_title(self) -> WebElement:
        """Finds and returns the title element of the Export dialog."""
        element = self.find_element.by_xpath(locators.EXPORT_DIALOG_TITLE)
        return element

    def get_export_dialog_label(self) -> WebElement:
        """Finds and returns the label element of the Export dialog."""
        element = self.find_element.by_xpath(locators.EXPORT_DIALOG_INPUT_LABEL)
        return element

    def get_export_dialog_input(self) -> WebElement:
        """Finds and returns the input text element of the Export dialog."""
        element = self.find_element.by_xpath(locators.EXPORT_DIALOG_INPUT)
        return element
