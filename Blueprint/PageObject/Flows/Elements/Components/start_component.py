from Blueprint.PageObject.Flows.Elements.Components.base_component import BaseComponent


class StartComponent(BaseComponent):
    """This class represents a step component"""
    def __init__(self, id) -> None:
        super().__init__(id)
        self.type = "Start"
