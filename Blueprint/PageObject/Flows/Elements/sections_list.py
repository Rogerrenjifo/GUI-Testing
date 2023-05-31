from Libraries.Drivers.singleton import Singleton


class SectionsList(metaclass = Singleton):
    """This class represents the sections displayed in project tracing page"""

    def __init__(self):
        super().__init__()
        self.default_section = "Section 1"
        self.sections_list = [self.default_section]
