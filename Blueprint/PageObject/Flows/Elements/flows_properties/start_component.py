from Blueprint.PageObject.Flows.Elements.flows_properties.flow_elements import FlowElements


class StartFlowsProperties(FlowElements):
    """'Start' component properties, methods and attributes."""

    def __init__(self):
        super().__init__()
        self.update_owner = self.select_owner_dropbox
