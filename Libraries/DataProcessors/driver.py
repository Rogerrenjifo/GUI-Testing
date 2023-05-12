from Libraries.DataProcessors.find_elements import FindElements
from Libraries.DataProcessors.browser import Browser
from selenium import webdriver


class Driver(object):

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.find_element = FindElements(self.driver)
        self.browser = Browser(self.driver)
