from Blueprint.PageObject.Flows.popup_messages_objects import PopupMessagesObjects


class PopUpMessagesActions(PopupMessagesObjects):
    """This class represents the popup messages actions in flow page."""

    def __init__(self):
        super().__init__()
    
    def click_close_popup_message(self):
        """Clicks close popup messages."""
        self.get_close_popup_message().click()

    def get_popup_messages_color(self):
        """Gets the color of a popup message."""
        color = self.get_popup_messages().value_of_css_property('background-color')
        return color
