from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Projects.ProjectTracing import flow_locators as locators
from Libraries.Drivers.base_page import BasePage
from robot.api import logger


class ProjectFlowObject(BasePage):
    """This class represents the Flow of the Project Tracing"""

    def get_title_project_flow(self) -> WebElement:
        """Finds and returns the flow title """
        element = self.find_element.by_xpath(locators.FLOW_TITLE)
        return element

    def get_start_element(self) -> WebElement:
        """Finds and returns the start element of the flow"""
        element = self.find_element.by_xpath(locators.START_ACTION)
        return element

    def get_final_step(self) -> WebElement:
        """Finds and returns the final element of the flow"""
        element = self.find_element.by_xpath(locators.FINAL_STEP)
        return element

    def get_flow_step(self, number: int) -> WebElement:
        """Finds and returns the step of the flow"""
        try:
            xpath = locators.STEPS.replace("<<number>>", str(number))
            element = self.find_element.by_xpath(xpath)
            return element
        except Exception:
            logger.info(f"'{number}' is not an available option")

    def get_flow_action(self, number: int) -> WebElement:
        """Finds and returns the action of the flow"""
        try:
            xpath = locators.ACTIONS.replace("<<number>>", str(number))
            element = self.find_element.by_xpath(xpath)
            return element
        except Exception:
            logger.info(f"'{number}' is not an available option")

    def get_popup_action(self) -> WebElement:
        """Finds and returns the popup of the actions"""
        element = self.find_element.by_xpath(locators.ACTION_POPUP)
        return element
