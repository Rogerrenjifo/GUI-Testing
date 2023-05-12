from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def find_element(driver: WebDriver, by: By, value: str) -> WebElement:
    """Finds and returns a web element by its locator type and value"""
    try:
        return driver.find_element(by=by, value=value)
    except Exception as e:
        raise Exception("It is not possible to find element" + value)


def find_element_by_id(driver: WebDriver, element_id: str, by: By = By.ID) -> WebElement:
    """Finds and returns a web element by its ID value."""
    try:
        return driver.find_element(by=by, value=element_id)
    except Exception as e:
        raise Exception("It is not possible to find element by id" + element_id)


def find_element_by_class(driver: WebDriver, class_name: str, by: By = By.CLASS_NAME) -> WebElement:
    """Finds and returns a web element by its Class name."""
    try:
        return driver.find_element(by=by, value=class_name)
    except Exception as e:
        raise Exception("It is not possible to find element by class" + class_name)


def find_element_by_tag_name(driver: WebDriver, tag_name: str, by: By = By.TAG_NAME) -> WebElement:
    """Finds and returns a web element by its Tag name."""
    try:
        return driver.find_element(by=by, value=tag_name)
    except Exception as e:
        raise Exception("It is not possible to find element by tag name" + tag_name)


def find_element_by_xpath(driver: WebDriver, xpath: str, by: By = By.XPATH) -> WebElement:
    """Finds and returns a web element by its Xpath."""
    try:
        return driver.find_element(by=by, value=xpath)
    except Exception as e:
        raise Exception("It is not possible to find element by xpath" + xpath)
