from selenium.webdriver.remote.webdriver import WebDriver


def navigate_to_url(driver: WebDriver, url: str):
    """Navigates to the given URL"""
    try:
        return driver.get(url)
    except Exception as e:
        raise Exception("It is not possible to navigate to" + url)


def close_browser(driver: WebDriver):
    """Closes the provided browser driver instance"""
    try:
        return driver.quit()
    except Exception as e:
        raise Exception("It is not possible close de browser")
