from Blueprint.Steps.Actions.Projects.ProjectTracing.project_tracing_forms_actions import FormsActions
from Blueprint.PageObject.Projects.ProjectTracing.project_tracing_forms_objects import FormObjects
from Libraries.Assertions.assertions import Verification
from assertpy import assert_that, soft_assertions
from selenium.webdriver.remote.webelement import WebElement
from robot.api import logger


class ProjectTracingFormsVerifications:
    """This class represents the verifications made in the project traing forms page."""
    def __init__(self):
        super().__init__()
        self.forms_actions = FormsActions()
        self.forms_objects = FormObjects()
        self.verification = Verification()
    
    def edit_button_of_field_should_be_visible(self, field_title: str, section_title: str):
        """Verifies if the edit button of a field from section given with title given is visible."""
        edit_button = self.forms_objects.get_edit_button(field_title, section_title)
        self.web_element_should_be_visible(edit_button)
            
    def save_button_should_be_visible(self):
        """Verifies if the save button of a field from section given with title given is visible."""
        save_button = self.forms_objects.get_save_button()
        self.web_element_should_be_visible(save_button)
    
    def cancel_button_should_be_visible(self):
        """Verifies if the cancel button of a field from section given with title given is visible."""
        cancel_button = self.forms_objects.get_cancel_button()
        self.web_element_should_be_visible(cancel_button)
    
    def required_field_div_should_be_visible(self):
        """Verifies if "Required field" div is visible."""
        required_field = self.forms_objects.get_required_field_div()
        self.web_element_should_be_visible(required_field)
    
    def field_border_should_be_color(self, field_title: str, section_title: str, expected_color: str):
        """Verifies if the border of a field is the given color."""
        actual_color = self.forms_objects.get_input_field(field_title, section_title).value_of_css_property('border-bottom-color')
        self.verification.verify_equal_ignore(actual_color, expected_color)
    
    def save_button_should_be_color(self, expected_color: str):
        """Verifies if save button has expected color."""
        save_button = self.forms_objects.get_save_button()
        self.web_element_should_be_color(save_button, expected_color, css_attribute='stroke')
    
    def save_button_should_be_disabled(self):
        """Verifies if save button is disabled."""
        save_button = self.forms_objects.get_save_button()
        self.web_element_should_be_disabled(save_button)
    
    def cancel_button_should_be_enabled(self):
        """Verifies cancel button is enabled."""
        self.web_element_should_be_enabled(self.forms_objects.get_cancel_button())
    
    def editable_text_input_should_be(self, expected_value: str):
        """Verifies that text on editable field is the expected value."""
        actual_value = self.forms_actions.get_editable_input_text_in_project_forms()
        self.verification.verify_equal_ignore(actual_value, expected_value)
    
    def editable_text_input_should_be(self, expected_value: str):
        """Verifies that text on editable field is the expected value."""
        actual_value = self.forms_actions.get_editable_input_text_in_project_forms()
        self.verification.verify_equal_ignore(actual_value, expected_value)
    
    def editable_numeric_input_should_be(self, expected_value: str):
        """Verifies that numbers on editable field is the expected value."""
        actual_value = self.forms_actions.get_editable_input_number_in_project_forms()
        self.verification.verify_equal_ignore(actual_value, expected_value)
        
    def required_field_div_should_be_color(self, expected_color: str):
        """Verifies if required field has the expected color."""
        required_field = self.forms_objects.get_required_field_div()
        self.web_element_should_be_color(required_field, expected_color, css_attribute='color')
    
    def editable_text_input_border_should_be_color(self, expected_color: str):
        """Verifies if editable text input is equal to a given color."""
        editable_text_input = self.forms_objects.get_editable_text_input()
        self.web_element_should_be_color(editable_text_input, expected_color)
    
    def dropdown_box_1_options_should_be_visible(self):
        """Verifies that all the options from Dropdown Box 1 are visible."""
        self.web_element_should_be_visible(self.forms_objects.get_dropdown_option('xx'))
        self.web_element_should_be_visible(self.forms_objects.get_dropdown_option('xy'))
        self.web_element_should_be_visible(self.forms_objects.get_dropdown_option('yy'))
    
    def dropdown_box_1_x_options_should_be_visible(self):
        """Verifies that all the options from Dropdown Box 1 are visible."""
        self.web_element_should_be_visible(self.forms_objects.get_dropdown_option('xx'))
        self.web_element_should_be_visible(self.forms_objects.get_dropdown_option('xy'))
    
    def dropdown_no_items_found_label_should_be_visible(self):
        """Verifies that 'No items found label' is visible."""
        self.web_element_should_be_visible(self.forms_objects.get_no_items_found_dropdown_option())
    
    def checkbox_value_should_be(self, field_title: str, section_title: str, expected_value: str):
        """Verifies if the checkbox value is the expected value."""
        actual_value = self.forms_objects.get_checkbox_value(field_title, section_title)
        self.verification.verify_equal_ignore(actual_value, expected_value)
    
    def multiline_value_should_be(self, field_title: str, section_title: str, expected_value: str):
        """Verifies if the multiline value is the expected value."""
        actual_value = self.forms_objects.get_multiline_value(field_title, section_title)
        self.verification.verify_equal_ignore(actual_value, expected_value)
    
    def please_select_user_should_be_visible(self):
        """Verifies if 'Please select user from user list' element is visible."""
        element = self.forms_objects.get_please_select_user_div()
        self.web_element_should_be_visible(element)
    
    def web_element_should_be_enabled(self, element: WebElement):
        """Verifies that a web element is enabled."""
        with soft_assertions():
            logger.info("*****Expected element should be visible******")
            assert_that(element.is_enabled()).is_true()
    
    def web_element_should_be_disabled(self, element: WebElement):
        """Verifies that a web element is disabled."""
        with soft_assertions():
            logger.info("*****Expected element should be disabled******")
            assert_that(element.is_enabled()).is_false()
            
    def web_element_should_be_visible(self, element: WebElement):
        """Verifies that a web element is visible."""
        with soft_assertions():
            logger.info("*****Expected element should be displayed******")
            assert_that(element.is_displayed()).is_true()
    
    def web_element_should_not_be_visible(self, element: WebElement):
        """Verifies that a web element is visible."""
        with soft_assertions():
            logger.info("*****Expected element should not be disabled******")
            assert_that(element.is_displayed()).is_false()
    
    def web_element_should_be_color(self, element: WebElement, expected_color: str, css_attribute: str = 'border-bottom-color'):
        """Verifies if the actual color of a web element is the expected."""
        actual_color = element.value_of_css_property(css_attribute)
        self.verification.verify_equal_ignore(actual_color, expected_color)
