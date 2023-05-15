from selenium import webdriver


class Browser(object):
    """A class that provides a browser instance"""
    driver = None

    def __init__(self, url, browser):
        self.driver = self.get_driver(browser)
        self.navigate_to_url(url)

    def get_driver(cls, browser):
        """ Returns an instance of the webdriver for the selected browser."""
        webdriver_map = {
            'firefox': webdriver.Firefox,
            'chrome': webdriver.Chrome,
            'edge': webdriver.Edge
        }
        driver_class = webdriver_map.get(browser.lower())
        if driver_class is None:
            raise ValueError(f"Unsupported browser: {browser}")
        if cls.driver is None:
            cls.driver = driver_class()
        return cls.driver

    def navigate_to_url(self, url: str):
        """Navigates to the given URL"""
        try:
            self.driver.maximize_window()
            return self.driver.get(url)
        except Exception as e:
            raise Exception("It is not possible to navigate to" + url)

    def close_browser(self):
        """Closes the provided browser driver instance"""
        try:
            return self.driver.quit()
        except Exception as e:
            raise Exception("It is not possible close de browser")
