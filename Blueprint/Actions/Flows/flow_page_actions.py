from Blueprint.PageObject.Flows.flows_page_objects import FlowsPageObjects


class FlowPageActions(FlowsPageObjects):

    def click_export_button(self):
        self.find_element.by_xpath(self.export_button).click()
