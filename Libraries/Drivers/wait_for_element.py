from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class WaitForElement(object):
    """A class that provides methods to wait for elements to load on a webpage."""
    def __init__(self, driver):
        self.driver = driver
    
    def wait_for_element_with_xpath(self, xpath: str, timeout: int = 10):
        """Waits (timeout) seconds for element with given xpath to load."""
        WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(By.XPATH, xpath))
