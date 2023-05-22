from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.CommonElements import date_locators as locators
from Libraries.Drivers.base_page import BasePage

class DateObjects(BasePage):
    """This class represents the date selection on all the possible cases in Blueprint."""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.__date_default_year_select = locators.DEFAULT_DATE_YEAR_SELECT_LOCATOR
        self.__date_default_year_option = locators.DATE_DEFAULT_YEAR_OPTION_LOCATOR
        self.__date_default_month_select = locators.DEFAULT_DATE_MONTH_SELECT_LOCATOR
        self.__date_default_month_option = locators.DATE_DEFAULT_MONTH_OPTION_LOCATOR
        self.__date_default_day_option = locators.DATE_DEFAULT_DAY_OPTION_LOCATOR
        self.__prev_month_button = locators.PREV_MONTH_BUTTON_LOCATOR
        self.__next_month_button = locators.NEXT_MONTH_BUTTON_LOCATOR
    
    def get_prev_month_button(self) -> WebElement:
        """Finds and returns previous month button."""
        element = self.find_element.by_xpath(self.__prev_month_button)
        return element
    
    def get_next_month_button(self) -> WebElement:
        """Finds and returns nextious month button."""
        element = self.find_element.by_xpath(self.__next_month_button)
        return element
        
    def get_date_default_year_select(self) -> WebElement:
        """Finds and returns date default value year select."""
        element = self.find_element.by_xpath(self.__date_default_year_select)
        return element
    
    def get_date_default_year_value(self, year: str) -> WebElement:
        """Finds and returns a year option from the dropdown with the required value."""
        new_xpath = self.__date_default_year_option.replace("<<value>>", year)
        try:
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Year  " + year + " not found.")
        
    def get_date_default_month_select(self) -> WebElement:
        """Finds and returns date default value month select."""
        element = self.find_element.by_xpath(self.__date_default_month_select)
        return element
    
    def get_date_default_month_value(self, month: str) -> WebElement:
        """Finds and returns a month value from the dropdown with the required value."""
        new_xpath = self.__date_default_month_option.replace("<<value>>", month)
        try:
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Month  " + month + " not found.")
    
    def get_date_default_day_value(self, day: str) -> WebElement:
        """Finds and returns a day value from the dropdown with the required value."""
        new_xpath = self.__date_default_day_option.replace("<<value>>", day)
        try:
            element = self.find_element.by_xpath(new_xpath)
            return element
        except Exception:
            raise Exception("Day  " + day + " not found.")
