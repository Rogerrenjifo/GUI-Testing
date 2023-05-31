from Blueprint.PageObject.Projects.ProjectPage.export_dialog_objects import ExportDialogObjects


class ExportDialogActions(ExportDialogObjects):
    """This class represents the actions of the export Dialog in Blueprint page."""
       
    def click_cancel_export_dialog_button_in_project_page(self):
        """Clicks on the Cancel button of the export dialog."""
        cancel = self.get_cancel_export_dialog_button()
        cancel.click()

    def click_export_dialog_button_in_project_page(self):
        """Clicks on the export button of the export dialog."""
        export = self.get_export_dialog_button()
        export.click()

    def click_close_export_dialog_button_in_project_page(self):
        """Clicks on the close button of the export dialog."""
        close = self.get_close_export_dialog_button()
        close.click()

    def obtain_export_dialog_title_text_in_project_page(self) -> str:
        """Obtains the title text of the export dialog."""
        title_text = self.get_export_dialog_title().text
        return title_text
    
    def obtain_export_dialog_input_label_text_in_project_page(self) -> str:
        """obtains the question text of the export dialog."""
        question_text = self.get_export_dialog_label().text
        return question_text

    def obtain_export_dialog_input_value_in_project_page(self) -> str:
        """Obtains the actual value of the input"""
        value = self.get_export_dialog_input().get_attribute("value")
        return value

    def edit_text_in_export_dialog_input_value_in_project_page(self, value: str):
        """Edits text value in the input"""
        input_text = self.get_export_dialog_input()
        input_text.clear()
        input_text.send_keys(value)

    def obtain_export_dialog_cancel_button_text_in_project_page(self) -> str:
        """obtains the cancel button text of the export dialog."""
        button_text = self.get_cancel_export_dialog_button().text
        return button_text

    def obtain_export_dialog_export_button_text_in_project_page(self) -> str:
        """obtains the export button text of the export dialog."""
        button_text = self.get_export_dialog_button().text
        return button_text

    def export_changing_file_name_in_project_page(self, value: str = ""):
        self.edit_text_in_export_dialog_input_value_in_project_page(value)
        self.click_export_dialog_button_in_project_page()
