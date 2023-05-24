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
        """Moves cursor to an element"""
        self.action_chains.move_to_element(source).perform()

    def custom_drag_and_drop(self, source: WebElement, target: WebElement, direction="down"):
        """Drags and drops an element up or down other element"""
        if direction.lower() == "down":
            self.action_chains.click_and_hold(source).move_to_element(target).\
                move_by_offset(0, 10).release().perform()
            logger.info(f"The element {source.text} is moved under of {target.text}")
        elif direction.lower() == "up":
            self.action_chains.click_and_hold(source).move_to_element(target).\
                move_by_offset(0, -10).release().perform()
            logger.info(f"The element {source.text} is moved up to {target.text}")
        else:
            logger.info(f"The input '{direction}' is an invalid direction, "
                        f"please send 'up' or 'down'")

    def custom_click_element(self, source: WebElement):
        """Clicks on a side of an element"""
        self.action_chains.move_to_element(source).move_by_offset(5, 5).click().perform()

    def drag_and_drop_by_position(self, source: WebElement, target: WebElement, x_percentage: int, y_percentage: int):
        """Drags and drops an element to target position"""
        x_position, y_position = self.__convert_percent_to_pixel(x_percentage, y_percentage, target)
        self.action_chains.click_and_hold(source).move_to_element(target).perform()
        self.action_chains.move_by_offset(x_position, y_position).release().perform()

    def __convert_percent_to_pixel(self, x_percentage: int, y_percentage: int, target: WebElement):
        """Converts percentage to pixels"""
        element_size = target.size
        width = element_size["width"] - 1
        height = element_size["height"] - 1
        x_pixels = ((x_percentage * (width - 166)) / 100) - (width / 2)
        y_pixels = ((y_percentage * (height - 23)) / 100) - (height / 2)
        return x_pixels, y_pixels

    def move_to_and_click(self, target: WebElement):
        """Moves the cursor to a target and clicks it"""
        self.action_chains.move_to_element(target).click()

    def custom_scroll(self, option: WebElement):
        """Scrolls and selects option"""
        self.action_chains.scroll_to_element(option).click(option).perform()
