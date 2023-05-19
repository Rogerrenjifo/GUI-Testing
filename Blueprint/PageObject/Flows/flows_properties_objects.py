from selenium.webdriver.remote.webelement import WebElement
from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flows_properties_locators as locators


class FlowPropertiesObjects(BasePage):
    """"Properties container contents and Elements involved representation."""

    def __init__(self) -> None:
        self.__container = locators.CONTAINER
        self.__header_title = locators.HEADER_TITLE
        self.__body_properties = locators.BODY_PROPERTIES
        self.__body_uppper = locators.BODY_UPPPER
        self.__body_lower = locators.BODY_LOWER
        self.__chk_add_comment = locators.CHK_ADD_COMMENT
        self.__chk_update_fields = locators.CHK_UPDATE_FIELDS
        self.__owner = locators.OWNER
        self.__txt_cmp_name = locators.TXT_CMP_NAME
        self.__vasel_typer = locators.SEL_TYPE
        self.__sel_add_fields = locators.SEL_ADD_FIELDS

    def get_element_name(self) -> WebElement:
        """Finds and returns selected component name."""
        return self.find_element.by_xpath(self.__txt_cmp_name)

    def get_element_type(self) -> WebElement:
        """Finds and returns selected component type."""
        return self.find_element.by_xpath(self.__vasel_typer)

    def get_propeties_container(self) -> WebElement:
        """Finds and returns properties container"""
        return self.find_element.by_xpath(self.__container)

    def get_properties_header_title(self) -> WebElement:
        """Finds and returns properties container header title."""
        return self.find_element.by_xpath(self.__header_title)

    def get_properties_body_container(self) -> WebElement:
        """Finds and returns properties container full body."""
        return self.find_element.by_xpath(self.__body_properties)

    def get_properties_body_container_upper_section(self) -> WebElement:
        """Finds and returns properties container body upper section."""
        return self.find_element.by_xpath(self.__body_uppper)

    def get_properties_body_container_lower_section(self) -> WebElement:
        """Finds and returns properties container lower section."""
        return self.find_element.by_xpath(self.__body_lower)

    def get_add_comments_checkbox(self) -> WebElement:
        """Finds and returns properties container add comments ckeckbox."""
        return self.find_element.by_xpath(self.__chk_add_comment)

    def get_update_fields_checkbox(self) -> WebElement:
        """Finds and returns properties container update fields checkbox."""
        return self.find_element.by_xpath(self.__chk_update_fields)

    def get_owner_dropdown_list(self) -> WebElement:
        """Finds and returns owners dropdown list."""
        return self.find_element.by_xpath(self.__owner + "[1]")

    def get_owner_list_values(self) -> WebElement:
        """Finds and returns selected owners list."""
        return self.find_element.by_xpath(self.__owner + "[2]")

    def get_add_fields_button(self) -> WebElement:
        """Finds and returns add fields to selected components button."""
        return self.find_element.by_xpath(self.__sel_add_fields)
