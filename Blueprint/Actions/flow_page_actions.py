import os
from Blueprint.PageObject import flow_locators as locators
from Libraries.DataProcessors.find_elements import *
from Blueprint.PageObject.base_page import BasePage


class FlowPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_flow_button(self):
        self.find_element.by_xpath("/html/body/app-root/main/div[2]/app-my-inbox/app-instance-header/div/div/div[3]/button").click()
