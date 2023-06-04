from Blueprint.PageObject.Flows.create_form_main_panel_objects import FormMainPanelPage
from robot.api import logger


class Section(FormMainPanelPage):
    """This class represents an 'action' component"""
    def __init__(self, section_title):
        super().__init__()
        self.section_title = section_title

    def select_section(self):
        """Clicks a section from main panel for display its properties"""
        self.get_section(self.section_title).click()

    def display_section_delete_menu(self, index=None):
        """Clicks drop-down button, if it does not display, clicks on its corner"""
        drop_down_button = self.get_section_dropdown(self.section_title, index)
        self.action_chains.move_to_an_element(drop_down_button)
        drop_down_button.click()
        display_drop_down_menu = drop_down_button.get_attribute("aria-expanded")
        if display_drop_down_menu.lower() == "false":
            logger.info("Clicking on middle drop-down button failed, "
                        "It will try clicking on one side of the button")
            self.action_chains.custom_click_element(drop_down_button)

    def obtain_section_error_message(self, index=None) -> str:
        """Returns section error message displayed in main panel"""
        message = self.get_section_error_message(self.section_title, index).text
        return message

    def obtain_section_title(self, index: str) -> str:
        """Returns section title displayed in main panel"""
        section_title = self.get_section_title(index).text
        return section_title

    def select_section_delete_button(self):
        """Clicks delete button from section drop-down menu"""
        self.get_section_delete_button().click()

    def obtain_section_error_message_rgb_color(self, index=None) -> str:
        """Gets the rgb color of the error message"""
        rgb_color = self.get_section_error_message(self.section_title, index).value_of_css_property('color')
        return rgb_color

    def obtain_section_rgb_color(self, index: str) -> str:
        """Gets the rgb color of the section title"""
        rgb_color = self.get_section_title(index).value_of_css_property('color')
        return rgb_color
