from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flow_locators as locators


class FlowsPageObjects(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.export_button = locators.EXPORT_BUTTON_LOCATOR
        # self.find_element.by_xpath(self.export_button)
