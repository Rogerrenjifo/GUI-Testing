from Blueprint.PageObject.Flows.Elements.FlowsProperties.name_field import NameField
from Blueprint.PageObject.Flows.Elements.FlowsProperties.select_type_dropbox import SelectTypeDropbox
from Blueprint.PageObject.Flows.Elements.FlowsProperties.end_checkbox import EndStepCheck
from Blueprint.PageObject.Flows.Elements.FlowsProperties.add_comment_checkbox import AddCommentCheck
from Blueprint.PageObject.Flows.Elements.FlowsProperties.update_fields_checkbox import UpdateFieldsCheck
from Blueprint.PageObject.Flows.Elements.FlowsProperties.select_owner_dropbox import SelectOwnerDropbox
from Blueprint.PageObject.Flows.Elements.FlowsProperties.req_update_fields import UpdateFieldsCommons
from Blueprint.PageObject.Flows.Elements.FlowsProperties.error_message_display import ErrorMessage
from Blueprint.PageObject.Flows.Elements.FlowsProperties.update_fields_combobox import ReqUpdateFields
from Blueprint.PageObject.Flows.Elements.FlowsProperties.update_value_combobox import ReqUpdateValues


class FlowElements():
    """This class represents objects in flow page"""

    def __init__(self):
        self.__name_field = NameField()
        self.__select_type_dropbox = SelectTypeDropbox()
        self.__end_step_checkbox = EndStepCheck()
        self.__add_comment_checkbox = AddCommentCheck()
        self.__update_fields_checkbox = UpdateFieldsCheck()
        self.__select_owner_dropbox = SelectOwnerDropbox()
        self.__required_fields_update = ReqUpdateFields()
        self.__error_message = ErrorMessage()
        self.__update_fields = ReqUpdateFields()
        self.__update_values = ReqUpdateValues()
        self.__update_commons = UpdateFieldsCommons()

    @property
    def name_field(self):
        """Attribute to control name object."""
        return self.__name_field
    
    @property
    def select_type_dropbox(self):
        """Attribute to control select type object."""
        return self.__select_type_dropbox

    @property
    def end_step_checkbox(self):
        """Attribute to control end step checkbox object."""
        return self.__end_step_checkbox

    @property
    def add_comment_checkbox(self):
        """Attribute to control add comment object."""
        return self.__add_comment_checkbox
    
    @property
    def update_fields_checkbox(self):
        """Attribute to control update fields object."""
        return self.__update_fields_checkbox
    
    @property
    def select_owner_dropbox(self):
        """Attribute to control slect owner object."""
        return self.__select_owner_dropbox
    
    @property
    def required_fields_update(self):
        """Attribute to control required fields to update object."""
        return self.__required_fields_update

    @property
    def error_message(self):
        """Attribute to verify errors messages."""
        return self.__error_message

    @property
    def update_fields(self):
        """Attribute to update required fields."""
        return self.__update_fields

    @property
    def update_values(self):
        """Attribute to update required field value."""
        return self.__update_values

    @property
    def update_commons(self):
        """Attribute to update required field value."""
        return self.__update_commons
