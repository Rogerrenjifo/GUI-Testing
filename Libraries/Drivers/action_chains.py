from selenium.webdriver import ActionChains

class ActionsChains(object):

    action_chains = None

    def __init__(self, driver, action_chains):
        self.action_chains = self.get_action_chains(action_chains)
        self.driver = driver

    def get_action_chains(self, cls, action_chains):
        if action_chains is None:
            cls.action_chains = ActionChains(self.driver)
        return cls.action_chains

    def drag_and_drop_element(self, element, target):
        self.action_chains.drag_and_drop(element, target).perform()
