from Libraries.DataProcessors.find_elements import FindElements
from Libraries.DataProcessors.browser import Browser
from selenium import webdriver
import time


class BasePage(object):

    def __init__(self, driver):
        self.find_element = FindElements(driver)


# class LoginPage(BasePage):
#     def __init__(self):
#         self.driver = self.get_driver()
#
#
# class MainPage(BasePage):
#     def __init__(self):
#         self.driver = self.get_driver()




