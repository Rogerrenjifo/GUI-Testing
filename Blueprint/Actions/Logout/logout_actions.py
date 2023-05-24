import time
from Blueprint.PageObject.Logout.logout_objects import Logout


class LogoutActions(Logout):
    """This class represents the logout actions of the Blueprint application"""

    def clicks_on_logout_menu(self):
        """Clicks on profile button for display the logout menu"""
        self.get_profile_button().click()
        time.sleep(1)

    def obtain_username(self) -> str:
        """Returns username displayed in logout menu"""
        self.clicks_on_logout_menu()
        user_name = self.get_username().text
        return user_name
