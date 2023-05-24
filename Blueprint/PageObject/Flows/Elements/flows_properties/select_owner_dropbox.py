from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flows_properties_locators as locators


class SelectOwnerDropbox(BasePage):
    """Selects owner type object for flows components properties, methods and attributes."""

    def __init__(self):
        super().__init__()
        self.__select_owner_label: WebElement
        self.__select_owner_combobox: WebElement
        self.__select_owner_listbox: WebElement
        self.__select_owner_default_item: WebElement
        self.__select_owner_item: WebElement
        self.__owner_label: WebElement
        self.__owner_combobox: WebElement
        self.__owner_default_item: WebElement
        self.__owner_item: WebElement
        self.__owner_clear: WebElement
        self.__owner_arrow: WebElement

    def __build_locator(self, xpath: str="", base: str="", text: str="", position: str="", id: str="") -> WebElement:
        """Builds xpath replacing given arguments."""
        new_xpath = xpath.replace("<<base>>", base).replace("<<text>>", base).replace("<<position>>", base).replace("<<id>>", base)
        element = self.find_element.by_xpath(new_xpath)
        return element
    
    def space_handler(self, text: str="") -> str:
        """Returns text with added space at begining and the end of the string."""
        if not text.startswith(" ") and not text.endswith(" "):
            return " " + text + " "
        else:
            return text.strip()
    
    @property
    def select_owner_label(self) -> WebElement:
        """Finds and returns 'select owner' label."""
        self.__select_owner_label = self.__build_locator(locators.LBL_OWNER, locators.SEL_OWNER_BASE)
        return self.__select_owner_label

    @property
    def select_owner_combobox(self) -> WebElement:
        """Finds and returns 'select owner' combobox."""
        self.__select_owner_combobox = self.__build_locator(locators.CMB_OWNER, locators.SEL_OWNER_BASE)
        return self.__select_owner_combobox

    @property
    def select_owner_listbox(self) -> WebElement:
        """Finds and returns 'select owner' listbox."""
        self.__select_owner_listbox = self.__build_locator(locators.LST_OWNER, locators.SEL_OWNER_BASE)
        return self.__select_owner_listbox

    @property
    def select_owner_default_item(self) -> WebElement:
        """Finds and returns 'select owner' default value."""
        self.__select_owner_default_item = self.__build_locator(locators.LST_SEL_OWNER_DEFAULT_ITEM, locators.SEL_OWNER_BASE)        
        return self.__select_owner_default_item

    def select_owner_item(self, by_text: str="", by_position: int=None) -> WebElement:
        """Finds and returns 'select owner' item by given arguments as text or position."""
        base = locators.SEL_OWNER_BASE
        if by_text:
            self.__select_owner_item = self.__build_locator(locators.LST_SEL_OWNER_ITEMS_LBLS, base, by_text)
        elif by_position:
            self.__select_owner_item = self.__build_locator(locators.LST_SEL_OWNER_ITEMS + "[" + str(by_position) + "]", base)
        else:
            self.__select_owner_item = self.__select_owner_default_item
        return self.__select_owner_item

    @property
    def owner_label(self) -> WebElement:
        """Finds and returns 'owner' label."""
        self.__owner_label = self.__build_locator(locators.LBL_OWNER, locators.OWNER_BASE)
        return self.__owner_label

    @property
    def owner_combobox(self):
        """Finds and returns 'owner' combobox."""
        self.__owner_combobox = self.__build_locator(locators.CMB_OWNER, locators.OWNER_BASE)
        return self.__owner_combobox

    @property
    def owner_default_item(self) -> WebElement:
        """Finds and returns 'owner' default item."""
        self.__owner_default_item = self.__build_locator(locators.LST_OWNER_DEFAULT_ITEM, locators.OWNER_BASE)        
        return self.__owner_default_item

    def owner_item(self, by_text: str=None) -> WebElement:
        """Finds and returns 'owner' by given text."""
        if by_text:
            self.__owner_item = self.__owner_default_item()
        return self.__owner_item

    @property
    def owner_clear(self) -> WebElement:
        """Finds and returns 'owner' default item."""
        self.__owner_clear = self.__build_locator(locators.OWNER_CLEAR, locators.OWNER_BASE)        
        return self.__owner_clear
    
    @property
    def owner_arrow(self) -> WebElement:
        """Finds and returns 'owner' default item."""
        self.__owner_arrow = self.__build_locator(locators.OWNER_CLEAR, locators.OWNER_BASE)        
        return self.__owner_arrow
