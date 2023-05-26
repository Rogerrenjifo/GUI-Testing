from Blueprint.PageObject.Flows.Elements.flows_properties.flow_elements import FlowElements


class EndFlowsProperties(FlowElements):
    """'End Step' component properties, methods and attributes."""

    def __init__(self):
        super().__init__()
        self.general_type = self.select_type_dropbox
        self.general_name = self.name_field
        self.general_end_step = self.end_step_checkbox
