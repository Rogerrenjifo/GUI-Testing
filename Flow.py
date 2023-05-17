from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
import os
import time
load_dotenv()

user = os.getenv('email')
password = os.getenv('password')
browser = webdriver.Chrome()
browser.get("https://test.blueprint.ses-unit.com/designer/7c733152-5eb1-4835-8193-8f88f3ed9169")
browser.maximize_window()
time.sleep(10)
username_input = browser.find_element(By.ID, "username")
password_input = browser.find_element(By.ID, "password")
username_input.send_keys(user)
password_input.send_keys(password)
signIn_button = browser.find_element(By.ID, "kc-login")
signIn_button.click()
time.sleep(30)

create_flow = browser.find_element(By.XPATH, "//main[text()=' Create Flow ']")
create_flow.click()

step_comp = browser.find_element(By.XPATH, "//p[text()=' Step ']")
action_comp = browser.find_element(By.XPATH, "//p[text()=' Action ']")
canvas = browser.find_element(By.ID, "canvas")

action = ActionChains(browser)
# action.drag_and_drop(step_comp, canvas).perform()
action.click_and_hold(step_comp).move_to_element(canvas).release(canvas).perform()
# action.click_and_hold(step_comp).move_to_element_with_offset(canvas, 500, 100).release().perform()

# step1 = browser.find_element(By.ID, "001Added4")
# action.drag_and_drop(step1, canvas).perform()


step_initial = browser.find_element(By.ID, "first")
action.move_to_element(step_initial).perform()
step_comp2 = browser.find_element(By.XPATH, '(//div[contains(@class,"endpointfirst")])[8]')
time.sleep(10)
action_comp2 = browser.find_element(By.XPATH, '(//div[contains(@class,"endpoint002Added1")])[16]')
time.sleep(10)
action.click_and_hold(step_comp2).move_to_element(action_comp2).release(action_comp2).perform()
time.sleep(10)



from selenium.webdriver.support.ui import Select

def click_dropdown_option(driver, dropdown_id, option_text):
    dropdown = Select(driver.find_element_by_id(dropdown_id))
    dropdown.select_by_visible_text(option_text)




