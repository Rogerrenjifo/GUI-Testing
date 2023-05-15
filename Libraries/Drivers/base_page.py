from Libraries.Drivers.find_elements import FindElements
from Libraries.Drivers.action_chains import ActionsChains


class BasePage(object):
    """Base class for pages that provides a common wrapper for functions"""
    def __init__(self, driver):
        self.find_element = FindElements(driver)
        self.action_chains = ActionsChains(driver)
