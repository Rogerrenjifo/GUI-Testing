from Blueprint.PageObject.Flows.Elements.Components.base_component import BaseComponent
from Libraries.Drivers.singleton import Singleton


class ComponentStorage(metaclass=Singleton):
    """This class storages objects in dictionaries"""

    def __init__(self) -> None:
        self.counter_action = 1
        self.counter_step = 1
        self.counter_end = 1
        self.component_dictionary = {}

    def increment_counter_action(self) -> None:
        """Increments the counter for actions"""
        self.counter_action += 1

    def increment_counter_step(self) -> None:
        """Implements the counter for steps"""
        self.counter_step += 1

    def increment_counter_end(self) -> None:
        """Increments the counter for end steps"""
        self.counter_end += 1

    def add_component(self, key: str, value: BaseComponent):
        """Adds component to the dictionary"""
        self.component_dictionary[key] = value
