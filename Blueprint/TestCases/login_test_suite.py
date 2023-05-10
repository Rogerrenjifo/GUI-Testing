from Blueprint.Actions.login_page_actions import *


def test_verify_if_a_user_is_able_to_log_in():
    login = LoginPage()
    print(login.get_header().text)
    print(login.get_title().text)
    print(login.get_username_label().text)
    print(login.get_password_label().text)
    login.insert_user()
    login.insert_password()
    login.click_in_sign_button()
    login.close_open_browser()


test_verify_if_a_user_is_able_to_log_in()
