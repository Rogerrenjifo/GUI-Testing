from selenium.webdriver import ActionChains

class ActionsChains(object):
    """A class that provides methods to use with element on a webpage."""
    def __init__(self, driver):
        self.driver = driver
        self.action_chains = ActionChains(self.driver)

    def drag_and_drop_element(self, element, target):
        """Drags and drops an element"""
        self.action_chains.drag_and_drop(element, target).perform()
