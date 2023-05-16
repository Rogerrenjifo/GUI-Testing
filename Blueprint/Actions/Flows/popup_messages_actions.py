from Blueprint.PageObject.Flows.popup_messages_objects import PopupMessagesObjects


class PopUpMessages(PopupMessagesObjects):
    """This class represents the popup messages actions in flow page"""
    
    def click_close_popup_message(self):
        """Clicks close popup messages"""
        self.get_close_popup_message().click()
