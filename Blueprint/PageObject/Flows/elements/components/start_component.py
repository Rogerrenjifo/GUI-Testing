from Blueprint.PageObject.Flows.elements.components.base_component import BaseComponent


class StartComponent(BaseComponent):
    """This class represents a step component"""
    def __init__(self, id, canvas, driver) -> None:
        super().__init__(id, canvas, driver)
        self.type = "Start"
