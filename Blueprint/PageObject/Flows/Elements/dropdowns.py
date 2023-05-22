from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import dropdown_locators as locators


class Dropdownbox(BasePage):
    """Builds the class constructor"""
    def __init__(self, driver, number: int):
        """Builds the class constructor"""
        super().__init__(driver)
        self.number = number

    def get_title(self) -> str:
        """Gets the title of the dropdown"""
        xpath = locators.TITLE.replace("<<number>>", str(self.number))
        title = self.find_element.by_xpath(xpath).text
        return title

    def click_dropdown(self):
        """Clicks the dropdown"""
        xpath = locators.TEXT_BOX.replace("<<number>>", str(self.number))
        self.find_element.by_xpath(xpath).click()

    def select_dropdown_user(self, user: str):
        """Selects a user from the dropdown"""
        xpath = locators.SELECT_USER.replace("<<user>>", user)
        self.find_element.by_xpath(xpath).click()

    def type_name_user(self, name: str):
        """Types the name of a user in the dropdown """
        xpath = locators.INPUT_TEXT_BOX.replace("<<number>>", str(self.number))
        self.find_element.by_xpath(xpath).send_keys(name)

    def delete_typed_name(self):
        """Deletes the typed name of the user in the dropdown"""
        xpath = locators.INPUT_TEXT_BOX.replace("<<number>>", str(self.number))
        self.find_element.by_xpath(xpath).clear()

    def delete_all_users(self):
        """Deletes all selected users from the dropdown"""
        xpath = locators.DELETE_ALL_USERS.replace("<<number>>", str(self.number))
        self.find_element.by_xpath(xpath).click()

    def message_empty(self) -> str:
        """Gets the message when dropdown textbox is empty"""
        xpath = locators.EMPTY_MESSAGE.replace("<<number>>", str(self.number))
        message = self.find_element.by_xpath(xpath).text
        return message

    def delete_selected_user(self, name: str):
        """Deletes a specific user from dropdown"""
        try:
            xpath = locators.DELETE_ONE_USER.replace("<<number>>", str(self.number)).replace("<<user>>", name)
            self.find_element.by_xpath(xpath).click()
        except Exception:
            print("user " + name + " does not exist")

    def delete_selected_users(self, names: list):
        """Deletes specific users from dropdown"""
        for name in names:
            self.delete_selected_user(name)

    def scroll_down(self, name: str):
        """Moves the scroll bar"""
        xpath = locators.SELECT_USER.replace("<<user>>", name)
        user = self.find_element.by_xpath(xpath)
        self.action_chains.custom_scroll(user)
