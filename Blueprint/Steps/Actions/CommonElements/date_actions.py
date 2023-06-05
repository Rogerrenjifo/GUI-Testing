from Blueprint.PageObject.CommonElements.date_objects import DateObjects


class DateActions(DateObjects):
    """This class represents the dates possible actions to interact in Blueprint."""
    
    def set_year(self, year: str):
        """Sets a year value in the date selection"""
        self.get_date_default_year_select().click()
        self.get_date_default_year_value(year).click()
        
    def set_month(self, month: str):
        """Sets a month value in the date selection"""
        self.get_date_default_month_select().click()
        self.get_date_default_month_value(month).click()
        
    def set_day(self, day: str):
        """Sets a day value in the date selection."""
        self.get_date_default_day_value(day).click()
    
    def go_prev_month(self):
        """Clicks the previous month button."""
        self.get_prev_month_button().click()
    
    def go_next_month(self):
        """Clicks the next month button."""
        self.get_next_month_button().click()
        
    def set_date(self, year: str, month: str, day: str):
        """Sets date value in the date selection."""
        self.set_year(year)
        self.set_month(month)
        self.set_day(day)
    
    def click_to_display_year_in_datapicker(self):
        """clicks to display year in datapicker"""
        self.get_date_default_year_select().click()
    
    def click_to_display_month_in_datapicker(self):
        """clicks to display month in datapicker"""
        self.get_date_default_month_select().click()
        