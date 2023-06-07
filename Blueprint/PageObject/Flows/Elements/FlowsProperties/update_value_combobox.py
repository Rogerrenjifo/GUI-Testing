from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flows_properties_locators as locators


class ReqUpdateValues(BasePage):
    """'Required to Update Fields'"""

    def __init__(self):
        super().__init__()
        self.__label: WebElement 
        self.__button: WebElement
        self.__button_text: WebElement
        self.__form_value_label: WebElement
        self.__form_value_combobox: WebElement
        self.__form_value_set_value_item: WebElement
        self.__form_value_ask_user_item: WebElement
        self.__form_value_clear_combobox: WebElement
        self.__form_value_combobox_arrow: WebElement
        self.__form_button_trash: WebElement
        self.__form_value_set_value: WebElement
        self.__value_get_text: WebElement
        self.__text_type_field: WebElement
        self.__number_type_field: WebElement
        self.__dropdown_list_type_field: WebElement
        self.__multiline_type_field: WebElement
        self.__date_type_field: WebElement
        self.__checkbox_type_field: WebElement
        self.__user_type_field: WebElement

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
    def form_value_label(self):
        """Returns value label for combobox."""
        self.__form_value_label = self.find_element.by_xpath(locators.REQ_FIELDS_VAL_LBL)
        return self.__form_value_label
    
    @property
    def form_value_combobox(self):
        """Returns combobox for value."""
        self.__form_value_combobox = self.find_element.by_xpath(locators.REQ_FIELDS_VAL_CMB)
        return self.__form_value_combobox

    @property
    def form_value_clear_combobox(self):
        """Returns click on ' X ' button to clear combobox content """
        self.__form_value_clear_combobox = self.find_element.by_xpath(locators.REQ_FIELDS_VAL_CLEAR)
        return self.__form_value_clear_combobox

    @property
    def form_value_combobox_arrow(self):
        """Rerturn value combobox arrow."""
        self.__form_value_combobox_arrow = self.find_element.by_xpath(locators.REQ_FIELDS_VAL_ARROW)
        return self.__form_value_combobox_arrow 

    @property
    def form_button_trash(self):
        """Returns trash button element."""
        self.__form_button_trash = self.find_element.by_xpath(locators.REQ_FIELDS_TRASH)
        return self.__form_button_trash

    @property
    def form_value_set_value_item(self):
        """Returns set value item element."""
        self.__form_value_set_value_item = self.find_element.by_xpath(locators.REQ_FIELDS_VAL_ITEM + "[2]")
        return self.__form_value_set_value_item

    @property
    def form_value_ask_user_item(self):
        """Returns ask user value element."""
        self.__form_value_ask_user_item = self.find_element.by_xpath(locators.REQ_FIELDS_VAL_ITEM + "[1]")
        return self.__form_value_ask_user_item

    @property
    def form_value_set_value(self):
        """Returns value element."""
        self.__form_value_set_value = self.find_element.by_xpath(locators.REQ_FIELDS_VAL_SELECTED)
        return self.__form_value_set_value
    
    @property
    def value_get_text(self):
        """Returns text value element of selected item."""
        self.__value_get_text = self.find_element.by_xpath(locators.REQ_FIELDS_VAL_TEXT)
        return self.__value_get_text

    @property
    def text_type_field(self):
        """Returns text type field to update element."""
        self.__text_type_field = self.find_element.by_xpath(locators.REQ_FIELDS_FRM_VAL_TEXT)
        return self.__text_type_field

    @property
    def number_type_field(self):
        """Returns text type field to update element."""
        self.__number_type_field = self.find_element.by_xpath(locators.REQ_FIELDS_FRM_VAL_NUMBER)
        return self.__number_type_field

    @property
    def dropdown_list_type_field(self):
        """Returns list type field to update element."""
        self.__dropdown_list_type_field = self.find_element.by_xpath(locators.REQ_FIELDS_FRM_VAL_DROP)
        return self.__dropdown_list_type_field

    @property
    def multiline_type_field(self):
        """Returns multiline type field to update element."""
        self.__multiline_type_field = self.find_element.by_xpath(locators.REQ_FIELDS_FRM_VAL_MULTI)
        return self.__multiline_type_field

    @property
    def date_type_field(self):
        """Returns date type field to update element."""
        self.__date_type_field = self.find_element.by_xpath(locators.REQ_FIELDS_FRM_VAL_DATE)
        return self.__date_type_field

    @property
    def checkbox_type_field(self):
        """Returns checkbox type field to update element."""
        self.__checkbox_type_field = self.find_element.by_xpath(locators.REQ_FIELDS_FRM_VAL_CHECK)
        return self.__checkbox_type_field

    @property
    def user_type_field(self):
        """Returns user type field to update element."""
        self.__user_type_field = self.find_element.by_xpath(locators.REQ_FIELDS_FRM_VAL_USER)
        return self.__user_type_field
