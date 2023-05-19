from Blueprint.PageObject.Flows.elements.components.base_component import BaseComponent


class ActionComponent(BaseComponent):
    """This class represents an action component"""
    def __init__(self, id, canvas, driver) -> None:
        super().__init__(id, canvas, driver)
        self.type = "Action"
