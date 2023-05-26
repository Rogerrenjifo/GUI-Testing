from Blueprint.PageObject.Flows.publish_tab_objects import PublishTabObjects


class PublishTabActions(PublishTabObjects):
    """This class represents the 'publish' tab actions in flow page."""

    def __init__(self):
        super().__init__()

    def click_save_publish_button(self):
        """Clicks save and publish button."""
        self.get_save_and_publish_button().click()
