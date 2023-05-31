from Blueprint.Steps.Actions.Projects.new_project_actions import NewProjectActions
from Blueprint.PageObject.Projects.new_project_objects import NewProjectObjects
from Blueprint.PageObject.CommonElements.popup_messages_objects import PopupMessagesObjects
from Libraries.Assertions.assertions import Verification
from assertpy import assert_that


class NewProjectPageVerifications:
    """This class represents the verifications methods for new request page."""
    def __init__(self):
        super().__init__()
        self.new_request_actions = NewProjectActions()
        self.verifications = Verification()
        self.new_request_objects = NewProjectObjects()
        self.popup_message = PopupMessagesObjects()

    def the_content_of_a_component_should_be_empty(self, section_name: str, label_name: str) -> None:
        """Verifies the content of a textbox, numberbox is empty."""
        value = self.new_request_actions.get_the_content_of_a_component_in_new_project_page(section_name, label_name)
        assert_that(value).is_empty()
        
    def popup_message_should_be_displayed(self) -> None:
        """Verifies popup message is displayed by clicking on create button."""
        popup_message = self.popup_message.get_popup_message().is_displayed()
        assert_that(popup_message).is_true()

    def create_button_rgb_color_should_be_as_expected(self, expected_rgb_color: str) -> None:
        """Verifies the RGB background color of create button."""
        self.new_request_actions.mouse_over_create_button_in_new_project_page()
        actual_rgb_color = self.new_request_actions.get_create_button_rgb_color()
        self.verifications.verify_equal_ignore(actual_rgb_color, expected_rgb_color)

    def create_button_status_should_be_disabled(self) -> None:
        """Verifies the create button is disabled."""
        status = self.new_request_objects.get_create_button().is_enabled()
        assert_that(status).is_false()

    def create_button_text_should_be_as_expected(self, expected_text: str = "Create") -> None:
        """Verifies the text of create button."""
        actual_text = self.new_request_actions.get_text_of_create_button()
        self.verifications.verify_equal_ignore(actual_text, expected_text)

    def the_text_or_number_should_be_as_expected(self, section_name: str, label_name: str, expected_result: str) -> None:
        """Verifies the content of a textbox, numberbox."""
        actual_result = self.new_request_actions.get_the_content_of_a_component_in_new_project_page(section_name, label_name)
        self.verifications.verify_equal_ignore(actual_result, expected_result)
        
    def the_numberic_box_value_should_change(self, section_name: str, label_name: str, expected_result: str) -> None:
        """Verifies that the numberic value increased."""
        actual_result = self.new_request_actions.get_the_content_of_a_component_in_new_project_page(section_name, label_name)
        self.verifications.verify_equal_ignore(actual_result, expected_result)

    def field_required_message_should_be_displayed(self) -> None:
        """Verifies the 'field required' message is displayed."""
        message = self.new_request_objects.get_locator_from_required_field_error_message().is_displayed()
        assert_that(message).is_true()

    def field_required_icon_should_be_displayed(self) -> None:
        """Verifies the 'field required' icon is displayed."""
        message_icon = self.new_request_objects.get_locator_from_required_field_error_message().is_displayed()
        assert_that(message_icon).is_true()

    def the_rgb_color_of_a_label_should_be_as_expected(self, section_name: str, label_name: str, expected_rgb_color: str) -> None:
        """Verifies the RGB background color of a label of each component is as expected."""
        self.new_request_actions.mouse_over_label_of_a_component_in_new_project_page(section_name, label_name)
        actual_rgb_color = self.new_request_actions.get_the_label_rgb_color_of_each_component(section_name, label_name)
        self.verifications.verify_equal_ignore(actual_rgb_color, expected_rgb_color)

    def border_of_a_component_should_be_highlighted(self, section_name: str, label_name: str, expected_rgb_color: str) -> None:
        """Verifies the RGB border color of a component is highlighted."""
        self.new_request_actions.click_a_component_inside_a_section_in_new_project_page(section_name, label_name)
        actual_rgb_color = self.new_request_actions.get_the_rgb_border_color_of_each_component(section_name, label_name)
        self.verifications.verify_equal_ignore(actual_rgb_color, expected_rgb_color)

    def the_title_of_a_flow_template_should_be_as_expected(self, expected_text: str) -> None:
        """Verifies that the title of a flow template in project page be the same as expected."""
        actual_text = self.new_request_actions.get_the_title_of_a_flow_template_in_project_page()
        self.verifications.verify_equal_ignore(actual_text, expected_text)
