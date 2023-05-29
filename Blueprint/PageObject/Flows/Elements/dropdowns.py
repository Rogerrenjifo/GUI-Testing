from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import dropdown_locators as locators
from robot.api import logger


class Dropdownbox(BasePage):
    """Represents the dropdowns base class"""

    def __init__(self, page: str, number: int = None):
        super().__init__()
        self.number = str(number)
        self.page = page

    def get_title(self, key: str) -> str:
        """Gets the title of the dropdown"""
        xpath = self.__xpath_selector(key)
        title = self.find_element.by_xpath(xpath).text
        return title

    def click_dropdown(self, key: str, name: str = None, label_name: str = None):
        """Clicks the dropdown"""
        xpath = self.__xpath_selector(key, name, label_name)
        self.find_element.by_xpath(xpath).click()

    def select_dropdown_option(self, key: str, user: str):
        """Selects an option from the dropdown"""
        try:
            xpath = self.__xpath_selector(key, user)
            self.find_element.by_xpath(xpath).click()
        except Exception:
            logger.info(f" option '{user}' does not exist")

    def type_characters_in_dropdown(self, key: str, name: str):
        """Types the name of a user in the dropdown """
        xpath = self.__xpath_selector(key)
        self.find_element.by_xpath(xpath).send_keys(name)

    def delete_typed_characters_in_dropdown(self, key: str):
        """Deletes the typed name of the user in the dropdown"""
        xpath = self.__xpath_selector(key)
        self.find_element.by_xpath(xpath).clear()

    def delete_all_options(self, key: str, name: str = None, label_name: str = None):
        """Deletes all selected users from the dropdown"""
        xpath = self.__xpath_selector(key, name, label_name)
        self.find_element.by_xpath(xpath).click()

    def message_empty_in_dropdown(self, key: str) -> str:
        """Gets the message when dropdown textbox is empty"""
        xpath = self.__xpath_selector(key)
        message = self.find_element.by_xpath(xpath).text
        return message

    def delete_selected_option(self, key: str, name: str):
        """Deletes a specific user from dropdown"""
        try:
            xpath = self.__xpath_selector(key, name)
            self.find_element.by_xpath(xpath).click()
        except Exception:
            logger.info(f" option '{name}' does not exist")

    def scroll_down(self, key: str, name: str):
        """Moves the scroll bar"""
        try:
            xpath = self.__xpath_selector(key, name)
            user = self.find_element.by_xpath(xpath)
            self.action_chains.custom_scroll(user)
        except Exception:
            logger.info(f" option '{name}' does not exist")
            self.click_drop_arrow()

    def click_drop_arrow(self, key: str):
        """Click on the dropdown arrow"""
        xpath = self.__xpath_selector(key)
        self.find_element.by_xpath(xpath).click()

    def get_available_options(self, key: str) -> list:
        """Return a list of available options of the dropdown"""
        xpath = self.__xpath_selector(key)
        options = self.find_elements.by_xpath(xpath)
        available_options = [option.text for option in options]
        option_list = available_options[0].split("\n")
        return option_list

    def __xpath_selector(self, key: str, name: str = None, label_name: str = None) -> str:
        """Selects the corresponding xpath"""
        if self.page == 'permissions':
            if key == 'SELECT_USER':
                return locators.permissions[key].replace("<<user>>", name)
            elif key == 'DELETE_ONE_USER':
                return locators.permissions[key].replace("<<number>>", self.number).replace("<<user>>", name)
            else:
                return locators.permissions[key].replace("<<number>>", self.number)

        if self.page == "projects_tracing_system":
            if key == 'OPTION':
                return locators.projects_tracing_system[key].replace("<<option>>", name)
            else:
                return locators.projects_tracing_system[key]

        if self.page == 'projects_new_project':
            if key == 'SELECT_USER':
                return locators.projects_new_project[key].replace("<<user>>", name)
            else:
                return locators.projects_new_project[key].replace("<<section_name>>", name).replace("<<label_name>>",
                                                                                                    label_name)
