from Libraries.Drivers.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
from Blueprint.Locators.Flows import dropdown_locators as locators
from robot.api import logger


class Dropdownbox(BasePage):
    """Represents the dropdowns base class"""

    def __init__(self, page: str):
        super().__init__()
        self.page = page

    def get_title(self, key: str, dropdown_index: str = None) -> str:
        """Gets the title of the dropdown"""
        xpath = self.__xpath_selector(key, dropdown_index=dropdown_index)
        title = self.find_element.by_xpath(xpath).text
        return title

    def click_dropdown(self, key: str, section_name: str = None, label_name: str = None, dropdown_index: str = None):
        """Clicks the dropdown"""
        xpath = self.__xpath_selector(key, section_name, label_name, dropdown_index)
        self.find_element.by_xpath(xpath).click()

    def select_dropdown_option(self, key: str, option: str, dropdown_index: str = None):
        """Selects an option from the dropdown"""
        try:
            xpath = self.__xpath_selector(key, option=option, dropdown_index=dropdown_index)
            self.find_element.by_xpath(xpath).click()
        except Exception:
            logger.info(f" option '{option}' does not exist")

    def type_characters_in_dropdown(self, key: str, characters: str, dropdown_index: str = None):
        """Types the name of a user in the dropdown """
        xpath = self.__xpath_selector(key, dropdown_index=dropdown_index)
        self.find_element.by_xpath(xpath).send_keys(characters)

    def get_rgb_color_label(self, key: str, dropdown_index: str = None) -> str:
        """Retrieves the RGB color value of a label element"""
        xpath = self.__xpath_selector(key, dropdown_index=dropdown_index)
        element = self.find_element.by_xpath(xpath)
        color = element.value_of_css_property('color')
        return color
    
    def get_rgb_color_element_in_dropdown(self, key: str, dropdown_index: str = None) -> str:
        """Retrieves the RGB color value of an element within a dropdown text box"""
        xpath = self.__xpath_selector(key, dropdown_index=dropdown_index)
        element = self.find_element.by_xpath(xpath)
        color = element.value_of_css_property('border-color')
        return color
    
    def get_rgb_background_color_element(self, key: str, option: str,dropdown_index: str = None) -> str:
        """Retrieves the RGB background color value of a specific button in dropdown text box"""
        xpath = self.__xpath_selector(key, option=option, dropdown_index=dropdown_index)
        element = self.find_element.by_xpath(xpath)
        color = element.value_of_css_property('background-color')
        return color

    def delete_typed_characters_in_dropdown(self, key: str, dropdown_index: str = None):
        """Deletes the typed name of the user in the dropdown"""
        xpath = self.__xpath_selector(key, dropdown_index=dropdown_index)
        self.find_element.by_xpath(xpath).clear()

    def delete_all_options(self, key: str, section_name: str = None, label_name: str = None, dropdown_index: str = None):
        """Deletes all selected users from the dropdown"""
        xpath = self.__xpath_selector(key, option=section_name, label_name=label_name, dropdown_index=dropdown_index)
        self.find_element.by_xpath(xpath).click()

    def move_mouse_to_delete_a_user(self, key: str, option: str, dropdown_index: str = None):
        """Moves the mouse pointer to the delete option"""
        xpath = self.__xpath_selector(key, option=option, dropdown_index=dropdown_index)
        element = self.find_element.by_xpath(xpath)
        self.action_chains.move_to_an_element(element)

    def message_empty_in_dropdown(self, key: str, dropdown_index: str = None) -> str:
        """Gets the message when dropdown textbox is empty"""
        xpath = self.__xpath_selector(key, dropdown_index=dropdown_index)
        message = self.find_element.by_xpath(xpath).text
        return message
    
    def message_in_dropdown_text_box(self, key: str, dropdown_index: str = None) -> str:
        """Gets the message displayed when the dropdown textbox is empty"""
        xpath = self.__xpath_selector(key, dropdown_index=dropdown_index)
        message = self.find_element.by_xpath(xpath).text
        return message

    def delete_selected_option(self, key: str, option: str, dropdown_index: str = None):
        """Deletes a specific user from dropdown"""
        try:
            xpath = self.__xpath_selector(key, option=option, dropdown_index=dropdown_index)
            self.find_element.by_xpath(xpath).click()
        except Exception:
            logger.info(f" option '{option}' does not exist")

    def scroll_down(self, key: str, option: str, dropdown_index: str = None):
        """Moves the scroll bar until the option sent"""
        try:
            xpath = self.__xpath_selector(key, option=option, dropdown_index=dropdown_index)
            user = self.find_element.by_xpath(xpath)
            self.action_chains.custom_scroll(user)
        except Exception:
            logger.info(f" option '{option}' does not exist")
            self.click_drop_arrow()

    def click_drop_arrow(self, key: str, dropdown_index: str = None):
        """Clicks on the dropdown arrow"""
        xpath = self.__xpath_selector(key, dropdown_index=dropdown_index)
        self.find_element.by_xpath(xpath).click()

    def get_available_options(self, key: str, dropdown_index: str = None) -> list:
        """Returns a list of available options of the dropdown"""
        xpath = self.__xpath_selector(key, dropdown_index=dropdown_index)
        options = self.find_elements.by_xpath(xpath)
        available_options = [option.text for option in options]
        option_list = available_options[0].split("\n")
        return option_list
        
    def get_user_list(self, key: str, dropdown_index: str = None) -> list:
        """Returns a user list from text box"""
        xpath = self.__xpath_selector(key, dropdown_index=dropdown_index)
        users = self.find_elements.by_xpath(xpath)
        users_selected = [user.text for user in users]
        return users_selected

    def get_element(self, key: str, dropdown_index: str = None) -> WebElement:
        """Returns an element of the dropdown"""
        try:
            xpath = self.__xpath_selector(key, dropdown_index=dropdown_index)
            element = self.find_element.by_xpath(xpath)
            return element
        except Exception:
            logger.info("Element not found")
            return False

    def get_characters_from_text_box(self, key: str, dropdown_index: str = None) -> str:
        """Returns characters from text box"""
        xpath = self.__xpath_selector(key, dropdown_index=dropdown_index)
        element = self.find_element.by_xpath(xpath)
        characters = element.get_attribute('value')
        return characters

    def __xpath_selector(self, key: str, option: str = None, label_name: str = None, dropdown_index: str = None) -> str:
        """Selects the corresponding xpath"""
        valid_pages = ['permissions', 'projects_tracing_system', 'projects_new_project']
        if self.page not in valid_pages:
            logger.info(f"Invalid page: {self.page}. Supported pages: {', '.join(valid_pages)}")
        if self.page == 'permissions':
            try:
                if key == 'SELECT_USER':
                    return locators.permissions[key].replace("<<user>>", option)
                elif key == 'DELETE_ONE_USER':
                    return locators.permissions[key].replace("<<number>>", str(dropdown_index)).replace("<<user>>", option)
                else:
                    return locators.permissions[key].replace("<<number>>", str(dropdown_index)) 
            except Exception:  
                logger.info(f"Invalid key: {key} not supported in {self.page} page")      
        if self.page == "projects_tracing_system":
            try:
                if key == 'OPTION':
                    return locators.projects_tracing_system[key].replace("<<option>>", option)
                else:
                    return locators.projects_tracing_system[key]
            except Exception:
                logger.info(f"Invalid key: {key} not supported in {self.page} page")
        if self.page == 'projects_new_project':
            try:
                if key == 'SELECT_USER':
                    return locators.projects_new_project[key].replace("<<user>>", option)
                else:
                    return locators.projects_new_project[key].replace("<<section_name>>", option).replace("<<label_name>>",
                                                                                                label_name)
            except Exception:
                logger.info(f"Invalid key: {key} not supported in {self.page} page")
