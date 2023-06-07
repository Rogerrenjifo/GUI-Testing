from Blueprint.Steps.Actions.Flows.publish_tab_actions import PublishTabActions
from Blueprint.Steps.Actions.CommonElements.popup_messages_actions import PopUpMessagesActions
from Libraries.Assertions.assertions import Verification
from time import sleep


class PublishVerifications:
    """This class represents the verifications of the Publish tab"""
    def __init__(self):        
        self.publish = PublishTabActions()
        self.verification = Verification()
        self.popup = PopUpMessagesActions()

    def save_and_publish_button_should_be_displayed(self):
        """Verifies that the save and publish button is displayed in the Publish tab."""        
        self.verification.verify_element_is_displayed(self.publish.get_save_and_publish_button())

    def popup_message_should_be_in_list(self, expected_message: str):
        """Verifies that the expected message is in the popups displayed."""        
        sleep(2)
        actual_list = self.popup.get_popup_messages_text_list()
        self.verification.verify_a_list_contains(actual_list, expected_message)
