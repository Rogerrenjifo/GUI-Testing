from Blueprint.Actions.Flows.flow_page_actions import NewFlowActions
from Blueprint.Actions.Login.login_page_actions import LoginPageActions
from Blueprint.Actions.MainMenu.main_menu_actions import MainMenuActions
from Libraries.Drivers.browser import Browser
import time


def test_verify_flow():
    browser = Browser("https://test.blueprint.ses-unit.com/", "Firefox")
    time.sleep(3)
    login = LoginPageActions(browser.driver)
    # flow = NewFlowActions(browser.driver)
    login.login()
    time.sleep(15)

    menu = MainMenuActions(browser.driver)
    menu.click_on_projects_button()
    time.sleep(3)
    menu.get_projects_results_list()
    time.sleep(5)

    # flow.click_on_flows_drop_down_button()
    # time.sleep(2)
    # flow.click_on_new_flow_button()
    # time.sleep(2)
    # flow.insert_new_flow_name("At_test")
    # flow.insert_new_flow_code("43H")
    # time.sleep(2)
    # flow.click_on_create_button()
    # time.sleep(3)
    # browser.close_browser()


test_verify_flow()
