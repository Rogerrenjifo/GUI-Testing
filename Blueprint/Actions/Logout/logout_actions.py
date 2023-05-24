import time
from Blueprint.PageObject.Logout.logout_objects import Logout


class LogoutActions(Logout):
    """Represents the logout actions of the application"""

    def display_logout_menu(self):
        """Clicks profile button for display logout menu"""
        self.get_profile_button().click()
        time.sleep(1)

    def obtain_username(self):
        """Returns username displayed in logout menu"""
        self.display_logout_menu()
        user_name = self.get_username().text
        return user_name
