from Blueprint.PageObject.CommonElements.popup_messages_objects import PopupMessagesObjects


class PopUpMessagesActions(PopupMessagesObjects):
    """This class represents the popup messages actions in flow page."""

    def click_to_close_popup_message(self):
        """Closes the popup message, if more than one are displayed, the last one is closed."""
        self.get_close_popup_message(str(len(self.get_popup_messages_list()))).click()

    def get_popup_message_color(self, index: str = "1") -> str:
        """Gets the color of a popup message."""
        color = self.get_popup_message(index).value_of_css_property('background-color')
        return color

    def get_popup_message_text(self, index: str = "1") -> str:
        """Gets the text displayed in a popup message."""
        text = self.get_popup_message(index).text
        return text

    def get_popup_messages_color_list(self) -> list:
        """Gets a list with the color of each popup message displayed."""
        color_list = []
        for index in range(1, len(self.get_popup_messages_list()) + 1):
            color_list.append(self.get_popup_message_color(str(index)))
        return color_list

    def get_popup_messages_text_list(self) -> list:
        """Gets a list with the text of each popup message displayed."""
        text_list = []
        for index in range(1, len(self.get_popup_messages_list()) + 1):
            text_list.append(self.get_popup_message_text(str(index)))
        return text_list
