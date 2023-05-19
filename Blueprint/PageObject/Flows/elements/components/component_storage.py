from Blueprint.PageObject.Flows.elements.components.base_component import BaseComponent


class ComponentStorage:
    """This class storages objects in dictionaries"""
    def __init__(self): 
        self.counter_action = 1
        self.counter_step = 1
        self.counter_end = 1
        self.action_dictionary = {}
        self.step_dictionary = {}

    def increment_counter_action(self) -> None: 
        """Increments the counter for actions"""
        self.counter_action += 1

    def increment_counter_step(self) -> None:
        """Implements the counter for steps""" 
        self.counter_step += 1

    def increment_counter_end(self) -> None:
        """Increments the counter for end steps"""
        self.counter_end += 1

    def add_action(self, key: str, value: BaseComponent) -> None:
        """Adds Actions to the dictionary"""
        self.action_dictionary[key] = value
    
    def add_step(self, key: str, value: BaseComponent) -> None:
        """Adds Steps to the dictionary"""
        self.step_dictionary[key] = value
