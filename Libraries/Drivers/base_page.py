from Libraries.Drivers.find_elements import FindElements


class BasePage(object):
    """Base class for pages that provides a common wrapper for functions"""
    def __init__(self, driver):
        self.find_element = FindElements(driver)
