from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flows_properties_locators as locators


class SelectTypeDropbox(BasePage):
    """Selects type object for flows components properties, methods and attributes."""

    def __init__(self):
        super().__init__()
        self.__label: WebElement
        self.__combobox: WebElement
        self.__arrow: WebElement
        self.__option: WebElement
        self.__default: WebElement

    @property
    def label(self):
        """Finds and returns label for components type combobox."""
        self.__label = self.find_element.by_xpath(locators.TYPE_LBL)
        return self.__label

    @property
    def combobox(self) -> WebElement:
        """Finds and returns component type select combobox."""
        self.__combobox = self.find_element.by_xpath(locators.TYPE_CMB)
        return self.__combobox

    @property
    def arrow(self) -> WebElement:
        """Finds and returns component type select combobox arrow."""
        self.__arrow = self.find_element.by_xpath(locators.TYPE_CMB_ARROW)
        return self.__arrow

    @property
    def option(self) -> WebElement:
        """Finds and returns component type select combobox arrow."""
        self.__option = self.find_element.by_xpath(locators.TYPE_CMB_OPTION)
        return self.__option

    @property
    def default(self) -> WebElement:
        """Finds and returns type select default value."""
        self.__default = self.find_element.by_xpath(locators.TYPE_CMB_DEFAULT)
        return self.__default
