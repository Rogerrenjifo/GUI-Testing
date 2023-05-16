from Blueprint.PageObject.Flows.create_form_elements_objects import CreateFormElementsObjects


class CreateFormElementsActions(CreateFormElementsObjects):
    """This class represents the create form elements of a Blueprint application"""
    def select_element_type(self, element_type: str):
        """Returns the element according the type selected"""
        elements = {
            'text': self.get_input_text_element(),
            'date': self.get_input_date_element(),
            'checkbox': self.get_input_checkbox_element(),
            'dropdown': self.get_input_dropdown_element(),
            'multiline': self.get_input_multiline_element(),
            'numbers': self.get_input_numbers_element(),
            'user_list': self.get_input_user_list_element()
        }
        return elements.get(element_type)

    def add_element_to_section(self, element_type: str, section_locator: str):
        """Adds a new element in a section form, according the selected type"""
        # TODO

    def add_element_to_column_section(self, element_type: str, column_section_locator: str):
        """Adds a new element in a section form, according the selected type"""
        # TODO

    def add_element_before_existent_element(self, element_type: str, existent_element_locator: str):
        """Adds a new element before an existent one, according the selected type"""
        # TODO

    def add_new_section(self):
        """Adds a new section in a form"""
        # TODO

    def add_new_section_before_existent_section(self, existent_section_locator: str):
        """Adds a new section in a form"""
        # TODO
