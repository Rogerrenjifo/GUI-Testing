from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class FindElements(object):
    """A class that provides methods to locate web elements on a webpage."""
    def __init__(self, driver):
        self.driver = driver

    def by(self, by: By, value: str) -> WebElement:
        """Finds and returns a web element by its locator type and value"""
        try:
            return self.driver.find_element(by=by, value=value)
        except Exception:
            raise Exception("It is not possible to find element " + value)

    def by_id(self, element_id: str, by: By = By.ID) -> WebElement:
        """Finds and returns a web element by its ID value."""
        try:
            return self.driver.find_element(by=by, value=element_id)
        except Exception:
            raise Exception("It is not possible to find element by id " + element_id)

    def by_class(self, class_name: str, by: By = By.CLASS_NAME) -> WebElement:
        """Finds and returns a web element by its Class name."""
        try:
            return self.driver.find_element(by=by, value=class_name)
        except Exception:
            raise Exception("It is not possible to find element by class " + class_name)

    def by_tag_name(self, tag_name: str, by: By = By.TAG_NAME) -> WebElement:
        """Finds and returns a web element by its Tag name."""
        try:
            return self.driver.find_element(by=by, value=tag_name)
        except Exception:
            raise Exception("It is not possible to find element by tag name " + tag_name)

    def by_xpath(self, xpath: str, by: By = By.XPATH) -> WebElement:
        """Finds and returns a web element by its Xpath."""
        try:
            return self.driver.find_element(by=by, value=xpath)
        except Exception:
            raise Exception("It is not possible to find element by xpath " + xpath)
