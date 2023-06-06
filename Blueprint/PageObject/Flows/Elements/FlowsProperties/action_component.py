from Blueprint.PageObject.Flows.Elements.FlowsProperties.flow_elements import FlowElements


class ActionFlowsProperties(FlowElements):
    """'Action' component properties, methods and attributes."""

    def __init__(self):
        super().__init__()
        self.general_type = self.select_type_dropbox
        self.general_name = self.name_field
        self.update_owner = self.select_owner_dropbox
        self.comments = self.add_comment_checkbox
        self.update_fields = self.update_fields_checkbox
        self.error_messages = self.error_message
