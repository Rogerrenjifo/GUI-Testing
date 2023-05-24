from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flows_properties_locators as locators


class ReqUpdateFields(BasePage):
    """'Required to Update Fields'"""

    def __init__(self):
        super().__init__()
        self.__label: WebElement 
        self.__button: WebElement
        self.__button_text: WebElement
        self.__form_field_label: WebElement
        self.__form_field_combobox: WebElement
        self.__form_field_clear_combobox: WebElement
        self.__form_field_combobox_arrow: WebElement
        self.__form_field_first_combobox_item: WebElement
        self.__form_button_trash: WebElement

    @property
    def label(self):
        """Returns properties subtitle label for fields options."""
        self.__label = self.find_element.by_xpath(locators.REQ_FIELDS_LBL)
        return self.__label

    @property
    def button(self):
        """Required update fields button."""
        self.__button = self.find_element.by_xpath(locators.REQ_FIELDS_BTN)
        return self.__button
    
    @property
    def button_text(self):
        """Returns button's text."""
        self.__button_text = self.find_element.by_xpath(locators.REQ_FIELDS_BTN + "/text()")
        return self.__button_text

    @property
    def form_field_label(self):
        """Returns field label."""
        self.__form_field_label = self.find_element.by_xpath(locators.REQ_FIELDS_FLD_LBL)
        return self.__form_field_label

    @property
    def form_field_combobox(self):
        """Represents update fields form combobox."""
        self.__form_field_combobox = self.find_element.by_xpath(locators.REQ_FIELDS_FLD_CMB)
        return self.__form_field_combobox

    @property
    def form_field_clear_combobox(self):
        """Returns clear combobox 'x' button."""
        self.__form_field_clear_combobox = self.find_element.by_xpath(locators.REQ_FIELDS_FLD_CLEAR)
        return self.__form_field_clear_combobox
    
    @property
    def form_field_first_combobox_item(self):
        """Returns item from combobox."""
        self.__form_field_first_combobox_item = self.find_element.by_xpath(locators.REQ_FIELDS_FLD_CMB_ITEM)
        return self.__form_field_first_combobox_item

    @property
    def form_field_combobox_arrow(self):
        """Returns combobox drop down arrow."""
        self.__form_field_combobox_arrow = self.find_element.by_xpath(locators.REQ_FIELDS_FLD_ARROW)
        return self.__form_field_combobox_arrow 

    @property
    def form_button_trash(self):
        """Returns trash button element."""
        self.__form_button_trash = self.find_element.by_xpath(locators.REQ_FIELDS_TRASH)
        return self.__form_button_trash
