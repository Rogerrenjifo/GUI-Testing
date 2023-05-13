from Libraries.Drivers.base_page import BasePage
from Blueprint.Locators.Flows import flow_locators as locators


class FlowsPageObjects(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__publish_tab =locators.PUBLISH_TAB
        self.__save_and_publish_button = locators.SAVE_AND_PUBLISH__BUTTON_LOCATOR
        self.__popup_messages = locators.POPUP_MESSAGES_LOCATOR
        self.__close_popup_messages = locators.CLOSE_POPUP_MESSAGES_LOCATOR
