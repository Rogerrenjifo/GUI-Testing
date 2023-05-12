from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver


class Browser(object):
    driver = None

    def __init__(self, url, browser):
        self.driver = self.get_driver(browser)
        self.navigate_to_url(url)
        # time.sleep(5)  # to do wait until
        #"https://test.blueprint.ses-unit.com/"

    def get_driver(cls, browser):
        print(browser)
        if cls.driver is None:
            cls.driver = webdriver.Firefox()
        return cls.driver

    # def get_driver(cls, browser):
    #     if cls.driver is None:
    #         cls.driver = webdriver.browser()
    #         return cls.driver
    #
    def navigate_to_url(self, url: str):
        """Navigates to the given URL"""
        # try:
        return self.driver.get(url)
        # except Exception as e:
        #     raise Exception("It is not possible to navigate to" + url)

    def close_browser(self):
        """Closes the provided browser driver instance"""
        try:
            return self.driver.quit()
        except Exception as e:
            raise Exception("It is not possible close de browser")
