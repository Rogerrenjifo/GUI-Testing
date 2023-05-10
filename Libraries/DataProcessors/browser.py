from selenium.webdriver.remote.webdriver import WebDriver


def close_browser(driver: WebDriver):
    """Closes the provided browser driver instance"""
    try:
        return driver.quit()
    except Exception as e:
        raise Exception("It is not possible close de browser")
