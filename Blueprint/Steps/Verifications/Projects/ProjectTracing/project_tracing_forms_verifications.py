from Blueprint.Steps.Actions.Projects.ProjectTracing.project_tracing_forms_actions import FormsActions
from Blueprint.PageObject.Projects.ProjectTracing.project_tracing_forms_objects import FormObjects
from assertpy import assert_that, soft_assertions
from selenium.webdriver.remote.webelement import WebElement
from robot.api import logger


class ProjectTracingFormsVerifications:
    """This class represents the verifications made in the project traing forms page."""
    def __init__(self):
        super().__init__()
        self.forms_actions = FormsActions()
        self.forms_objects = FormObjects()
    
    def edit_button_of_field_should_be_visible(self, field_title: str, section_title: str):
        """Verifies if the edit button of a field from section given with title given is visible."""
        edit_button = self.forms_objects.get_edit_button(field_title, section_title)
        with soft_assertions():
            assert_that(edit_button.is_displayed()).is_true()
            
    def save_button_should_be_visible(self):
        """Verifies if the save button of a field from section given with title given is visible."""
        save_button = self.forms_objects.get_save_button()
        with soft_assertions():
            assert_that(save_button.is_displayed()).is_true()
    
    def cancel_button_should_be_visible(self):
        """Verifies if the cancel button of a field from section given with title given is visible."""
        cancel_button = self.forms_objects.get_cancel_button()
        with soft_assertions():
            assert_that(cancel_button.is_displayed()).is_true()
    
    def field_border_should_be_color(self, field_title: str, section_title: str, expected_color: str):
        """Verifies if the border of a field is the given color."""
        field_color = self.forms_objects.get_input_field(field_title, section_title).value_of_css_property('border-bottom-color')
        with soft_assertions():
            assert_that(field_color).is_equal_to(expected_color)
    
    def editable_text_input_border_should_be_color(self, expected_color: str):
        """Verifies if editable text input is equal to a given color."""
        input_color = self.forms_objects.get_editable_text_input().value_of_css_property('border-bottom-color')
        with soft_assertions():
            assert_that(input_color).is_equal_to(expected_color)
            
    def web_element_should_be_visible(self, element: WebElement):
        """Verifies that a web element is visible."""
        with soft_assertions():
            assert_that(element.is_displayed()).is_true()
