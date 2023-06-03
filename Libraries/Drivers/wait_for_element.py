from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webelement import WebElement


class WaitForElement(object):
    """A class that provides methods to wait for elements to load on a webpage."""
    def __init__(self, driver):
        self.driver = driver
    
    def wait_for_element_with_xpath(self, xpath: str, timeout: int = 10):
        """Waits (timeout) seconds for element with given xpath to load."""
        WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(By.XPATH, xpath))

    def wait_for_element_with_web_element(self, element: WebElement, timeout: int = 10):
        """Waits (timeout) seconds for element with given a web element."""
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of(element))

    def wait_for_result(self, result: WebElement, timeout: int = 2):
        """Waits (timeout) seconds for the text of an element."""
        WebDriverWait(self.driver, timeout).until(lambda x: len(result.text) > 0)
