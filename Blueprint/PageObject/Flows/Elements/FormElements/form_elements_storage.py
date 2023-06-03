from Libraries.Drivers.singleton import Singleton
from Blueprint.PageObject.Flows.Elements.FormElements.form_section import Section
from Blueprint.PageObject.Flows.Elements.FormElements.form_component import Component


class FormElementsStorage(metaclass=Singleton):
    """This class represents the all the comments displayed in project tracing page"""

    def __init__(self):
        super().__init__()
        self.sections_list = []
        self.components_in_sections = {}
        self.default_section_title = "Section 1"
        self.default_component_id = "section-1_textbox-1"

    def add_default_section(self):
        """Adds the default section to sections list"""
        self.sections_list.append(Section(self.default_section_title))

    def add_default_component(self):
        """Adds the default component in default section to components dict"""
        section = self.default_component_id.split('_')[0]
        self.components_in_sections[section] = {self.default_component_id : Component(self.default_component_id)}

    def add_section(self, direction: str = None, existing_section_index: int = None):
        """Adds a new section to sections list"""
        new_section_title = f"Section {str(len(self.sections_list) + 1)}"
        if direction == "up":
            if existing_section_index != 0:
                self.sections_list.insert(existing_section_index, Section(new_section_title))
        elif direction == "down":
            self.sections_list.insert(existing_section_index + 1, Section(new_section_title))
        else:
            section_title = f"Section {str(len(self.sections_list)+1)}"
            self.sections_list.append(Section(section_title))

    def add_component_to_section(self, component_type: str, reference: str = None, component_number: str = "1"):
        """Adds a new component in its section to components dict"""
        section = reference.split('_')[0]
        component_id = f"{section}_{component_type}-{component_number}"
        if section in self.components_in_sections:
            self.components_in_sections[section].update({component_id: Component(component_id)})
        else:
            self.components_in_sections[section] = {component_id: Component(component_id)}

    def get_section_index(self, section_title: str) -> int:
        """Gets section index from a section list"""
        section_index = self.get_sections_title().index(section_title)
        return section_index

    def get_sections_title(self) -> list:
        """Gets sections title from a section list"""
        sections_title = []
        for section_index in range(0, len(self.sections_list)):
            sections_title.append(self.sections_list[section_index].obtain_section_title(section_index+1))
        return sections_title

    def get_components_title(self, section: str = "section-1") -> list:
        """Gets components title from component dict"""
        components_title = []
        components_list = list(self.components_in_sections[section[0:9]].values())
        for component_index in range(0, len(components_list)):
            components_title.append(components_list[component_index].obtain_component_title())
        return components_title
