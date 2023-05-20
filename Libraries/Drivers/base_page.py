from Libraries.Drivers.find_elements import FindElements
from Libraries.Drivers.action_chains import ActionsChains
from Libraries.Drivers.find_elements_list import FindElementsList


class BasePage(object):
    """Base class for pages that provides a common wrapper for functions"""
    def __init__(self, driver):
        self.driver = driver
        self.find_element = FindElements(self.driver)
        self.action_chains = ActionsChains(self.driver)
        self.find_elements = FindElementsList(self.driver)
