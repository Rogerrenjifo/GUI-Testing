from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flows_properties_locators as locators


class EndStepCheck(BasePage):
    """'End Step' checkbox for 'Step' component."""
    
    def __init__(self):
        super().__init__()
        self.__label: WebElement 
        self.__checkbox: WebElement

    @property
    def label(self):
        """End Step checkbox label text."""
        self.__label = self.find_element.by_xpath(locators.END_STEP_LBL)
        return self.__label

    @property
    def checkbox(self):
        """End Step checkbox ticker."""
        self.__checkbox = self.find_element.by_xpath(locators.END_STEP_CHK)
        return self.__checkbox
