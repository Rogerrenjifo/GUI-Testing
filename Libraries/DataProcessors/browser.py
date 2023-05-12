from selenium.webdriver.remote.webdriver import WebDriver


class Browser(object):
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, url: str):
        """Navigates to the given URL"""
        try:
            return self.driver.get(url)
        except Exception as e:
            raise Exception("It is not possible to navigate to" + url)

    def close_browser(self):
        """Closes the provided browser driver instance"""
        try:
            return self.driver.quit()
        except Exception as e:
            raise Exception("It is not possible close de browser")
