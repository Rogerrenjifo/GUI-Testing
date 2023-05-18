from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from robot.api import logger


class ActionsChains(object):
    """A class that provides methods to use with element on a webpage."""
    def __init__(self, driver):
        self.driver = driver
        self.action_chains = ActionChains(self.driver)

    def drag_and_drop_element(self, source: WebElement, target: WebElement):
        """Drags and drops an element"""
        self.action_chains.click_and_hold(source).move_to_element(target).release(target).perform()

    def move_to_an_element(self, source: WebElement):
        self.action_chains.move_to_element(source).perform()

    def custom_drag_and_drop(self, source: WebElement, target: WebElement, direction="down"):
        """Drags and drops an element up or down other element"""
        if direction.lower() == "down":
            self.action_chains.click_and_hold(source).move_to_element(target).\
                move_by_offset(0, 10).release().perform()
        elif direction.lower() == "up":
            self.action_chains.click_and_hold(source).move_to_element(target).\
                move_by_offset(0, -10).release().perform()
        else:
            logger.info(f"The input '{direction}' is an invalid direction, "
                        f"please send 'up' or 'down'")

    def custom_click_element(self, source: WebElement):
        """Clicks on a side of an element"""
        self.action_chains.move_to_element(source).move_by_offset(0, 5).click().perform()
