from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class WaitForElement(object):
    """A class that provides methods to wait for elements to load on a webpage."""
    def __init__(self, driver):
        self.driver = driver
    
    def wait_for_element_with_xpath(self, xpath: str, timeout: int = 10):
        """Waits (timeout) seconds for element with given xpath to load."""
        wait = WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(By.XPATH, xpath))

    def wait_for_element_with_web_element(self, element, timeout: int = 20):
        """Waits (timeout) seconds for element with given xpath to load."""
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of(element))

    def wait_for_element_clickable_with_web_element(self, element, timeout: int = 20):
        """Waits (timeout) seconds for element with given xpath to load."""
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(element))
