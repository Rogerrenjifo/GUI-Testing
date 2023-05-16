from selenium.webdriver import ActionChains

class ActionsChains(object):
    """A class that provides methods to use with element on a webpage."""
    def __init__(self, driver):
        self.driver = driver
        self.action_chains = ActionChains(self.driver)

    def drag_and_drop_element(self, source, target):
        """Drags and drops an element"""
        self.action_chains.click_and_hold(source).move_to_element(target).release(target).perform()
