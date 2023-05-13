from Blueprint.PageObject.Flows.flows_page_objects import FlowsPageObjects


class FlowPageActions(FlowsPageObjects):

    def click_export_button(self):
        self.find_element.by_xpath(self.export_button).click()

    def click_publish_tab(self):
        self.find_element.by_xpath(self.__publish_tab).click()

    def click_save_and_publish_button(self):
        self.find_element.by_xpath(self.__save_and_publish_button).click()
    
    def click_close_popup_message(self):
        self.find_element.by_xpath(self.__close_popup_messages).click()