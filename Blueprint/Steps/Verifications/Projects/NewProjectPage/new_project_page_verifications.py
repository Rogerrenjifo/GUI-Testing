from Blueprint.Steps.Actions.Projects.new_project_actions import NewProjectActions
from Blueprint.PageObject.Projects.new_project_objects import NewProjectObjects
from Blueprint.PageObject.CommonElements.popup_messages_objects import PopupMessagesObjects
from Blueprint.PageObject.CommonElements.date_objects import DateObjects
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
        self.date_objects = DateObjects()
        self.default_field_required_color = "rgba(255, 114, 105, 1)"
    
    def option_should_be_equal(self, actual_result: str, expected_result: str):
        """Verifies the actual string with expected string"""
        self.verifications.verify_equal_ignore(actual_result, expected_result)

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
        message = self.new_request_objects.get_locator_from_required_field_error_message()
        assert_that(message.is_displayed()).is_true()
        self.option_should_be_equal(message.text, "Field Required")
        self.option_should_be_equal(message.value_of_css_property('color'), self.default_field_required_color)

    def field_required_icon_should_be_displayed(self) -> None:
        """Verifies the 'field required' icon is displayed."""
        message_icon = self.new_request_objects.get_locator_from_error_message_icon()
        assert_that(message_icon.is_displayed).is_true()

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
    
    def border_component_should_be_as_expected_when_mouse_over(self, section_name: str, label_name: str, expected_rgb_color: str) -> None:
        """Verifies the RGB border color of an input is as expected when mouse over"""
        self.new_request_actions.mouse_over_input_text_box_of_a_component_new_project_page(section_name, label_name)
        actual_rgb_color = self.new_request_actions.get_the_rgb_border_color_of_each_component(section_name, label_name)
        self.verifications.verify_equal_ignore(actual_rgb_color, expected_rgb_color)

    def the_title_of_a_flow_template_should_be_as_expected(self, expected_text: str) -> None:
        """Verifies that the title of a flow template in project page be the same as expected."""
        actual_text = self.new_request_actions.get_the_title_of_a_flow_template_in_project_page()
        self.verifications.verify_equal_ignore(actual_text, expected_text)
    
    def the_options_list_in_dropdown_should_be_displayed(self) -> None:
        """Verifies if the option list of a dropdown is displayed"""
        option_list = self.new_request_objects.get_element_options_dropdown_list().is_displayed()
        assert_that(option_list).is_true()
    
    def the_datepicker_in_datebox_should_be_displayed(self) -> None:
        """Verifies if the option list of a dropdown is displayed"""
        option_list = self.new_request_objects.get_element_datebox_datepicker().is_displayed()
        assert_that(option_list).is_true()
    
    def month_or_year_in_datapicker_should_be_displayed(self) -> None:
        """Verifies if the month list in datapicker is displayed"""
        month_list_in_datapicker = self.date_objects.get_month_or_year_list()
        assert_that(month_list_in_datapicker).is_true()

    def month_value_should_be_the_selected(self, expected_month: str) -> None:
        """Verifies if the month value is the selected"""
        actual_month = self.date_objects.get_month_value().text
        self.option_should_be_equal(actual_month, expected_month)

    def year_value_should_be_the_selected(self, expected_year: str) -> None:
        """Verifies if the year value is the selected"""
        actual_year = self.date_objects.get_year_value().text
        self.option_should_be_equal(actual_year, expected_year)
        
    def checkbox_should_be_marked(self, section_name: str, label_name: str) -> None:
        """Verifies that the dropdown is marked"""
        checkbox_marked = self.new_request_objects.get_checkbox_status_locator(section_name, label_name).is_selected()
        assert_that(checkbox_marked).is_true()
    
    def checkbox_should_not_be_marked(self, section_name: str, label_name: str) -> None:
        """Verifies that the dropdown is not marked"""
        checkbox_marked = self.new_request_objects.get_checkbox_status_locator(section_name, label_name).is_selected()
        assert_that(checkbox_marked).is_false()
