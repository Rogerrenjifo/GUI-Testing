from Blueprint.PageObject.Flows.Elements.FlowsProperties.flow_elements import FlowElements

class FirstFlowsProperties(FlowElements):
    """'First' component properties, methods and attributes."""

    def __init__(self):
        super().__init__()
        self.general_name = self.name_field
        self.update_fields = self.update_fields_checkbox
        self.error_messages = self.error_message
