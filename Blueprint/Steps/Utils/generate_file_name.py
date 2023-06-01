from datetime import datetime


class FileNameGenerator:
    """Provides file names with the format specified as the business logic"""
    def actual_date(self) -> str:
        """Generates the actual date in the following format: d_m_YYYY"""
        today = datetime.today().strftime('%d_%m_%Y')
        today_list = today.split("_")
        if today_list[1][0] == "0":
            today_list[1] = today_list[1][1:2]
        if today_list[0][0] == "0":
            today_list[0] = today_list[0][1:2]
        today = "_".join(today_list)
        return today

    def generate_file_name(self, project_name: str) -> str:
        """Generates the filename in the following format: export_project_name_d_m_YYYY"""
        date = self.actual_date()
        project_name = project_name.replace(" ", "_")
        file_name = f"export_{project_name}_{date}"
        return file_name
