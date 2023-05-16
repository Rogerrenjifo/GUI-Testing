from Blueprint.PageObject.Flows.publish_tab_objects import PublishTabObjects


class PublishTab(PublishTabObjects):
    """This class represents the publish tab actions in flow page"""
    
    def click_save_publish_button(self):
        """Clicks save and publish button"""
        self.get_save_and_publish_button().click()
