from selenium import webdriver
from os import getenv


class Browser(object):
    """A class that provides a browser instance"""
    _driver = None
    _webdriver_map = {"edge": {"driver": webdriver.Edge, "options": webdriver.EdgeOptions()},
                      "chrome": {"driver": webdriver.Chrome, "options": webdriver.ChromeOptions()},
                      "firefox": {"driver": webdriver.Firefox, "options": webdriver.FirefoxOptions()}}
    _devices = {
        "pixel s5": "--window-size=360,640",
        "iphone 12pro": "--window-size=390,844",
        "iphone xr": "--window-size=414,896",
        "galaxy s20 ultra": "--window-size=412,915",
        "ipad air": "--window-size=820,1180",
        "hub max": "--window-size=820,1180",
        "pc": "--start-maximized"}

    @classmethod
    def get_driver(cls):
        """ Returns an instance of the webdriver for the selected browser."""
        if cls._driver is None:
            cls._driver = cls.__create_instance()
        return cls._driver

    @classmethod
    def __create_instance(cls):
        """Creates an WebDriver customized instance"""
        browser = getenv("BROWSER", "chrome")
        device = getenv("DEVICE", "pc")
        driver_path = getenv("DRIVER_PATH", "./")
        implicit_timeout = int(getenv("IMPLICIT_TIMEOUT", 2))
        if browser.lower() in cls._webdriver_map:
            browser_config = cls._webdriver_map.get(browser)
            driver_class = browser_config.get("driver")
            options = browser_config.get("options")
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        options.add_argument(cls._devices.get(device.lower()))
        driver = driver_class(executable_path=driver_path, options=options)
        driver.implicitly_wait(implicit_timeout)
        cls._driver = driver
        return cls._driver

    @classmethod
    def add_device(cls, device_name: str, device_option: str):
        """Adds a new device to the _devices dictionary"""
        cls._devices[device_name] = device_option

    @classmethod
    def add_browser(cls, browser_name: str, driver: webdriver, options):
        """Adds a new browser to the _webdriver_map dictionary"""
        cls._webdriver_map[browser_name] = {"driver": driver, "options": options}

    def navigate_to_url(self, url: str):
        """Navigates to the given URL"""
        try:
            return self._driver.get(url)
        except Exception:
            raise Exception("It is not possible to navigate to" + url)

    def close_browser(self):
        """Closes the provided browser driver instance"""
        try:
            return self._driver.quit()
        except Exception:
            raise Exception("It is not possible close de browser")

    def go_back_to_previous_page(self):
        """Goes back to a previous page."""
        try:
            return self._driver.back()
        except Exception:
            raise Exception("It is not possible to go back")
        
    def reload_window(self):
        """Reloads page"""
        self._driver.refresh()
