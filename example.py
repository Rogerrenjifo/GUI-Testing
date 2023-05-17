from Libraries.Drivers.base_page import BasePage
class DropDown(BasePage):
    def __init__(self, driver, number):
        super().__init__(driver)
        self.title = ""
        self.number = number + 1
    def get_title(self):
        # xpath = f"(//ng-select[@id='{self.number}']//parent::div)[1]/label"
        xpath = f"(//ng-select[@bindlabel='name'])[{self.number}]//preceding-sibling::label"
        element = self.find_element.by_xpath(xpath)
        title = element.get_attribute("textContent")
        print(title)

    def click_dropdown(self, user):
        #click en el box y click user denilson
        # xpath = f"//input[@id='{self.id}']"
        xpath = f"(// ng-select[@ bindlabel='name'])[{self.number}]"
        text_box = self.find_element.by_xpath(xpath)
        text_box.click()
        user_xpath = f"//span[@title='{user}']"
        user = self.find_element.by_xpath(user_xpath)
        user.click()

    def write_user(self):
        # TO DO
        pass
    def edit_user(self):
        # TO DO
        pass
    def get_element(self, xpath):
        element = self.find_element.by_xpath(xpath)
        return element


from Blueprint.Actions.Login.login_page_actions import LoginPageActions
from Libraries.Drivers.browser import Browser
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://test.blueprint.ses-unit.com/designer/87acb018-fb08-42f3-a81c-3226357089b9"
browser = "chrome"
driver = Browser(url, browser).driver
time.sleep(7)
username = "Denisse.Cordova"
password = "nadeco93"

LoginPageActions(driver).login(username, password)
time.sleep(20)
create_flow = driver.find_element(By.XPATH, "//main[text()=' Permissions ']")
create_flow.click()
time.sleep(10)

dropdown_list = []
a = driver.find_elements(By.XPATH, "(//ng-select[@bindlabel='name'])")
for i in range(len(a)):
    print(i)
dropdown_fabian = DropDown(driver, 0)
dropdown_denisse = DropDown(driver, 1)
dropdown1 = DropDown(driver, 2)
dropdown2 = DropDown(driver, 3)
dropdown3 = DropDown(driver, 4)
dropdown4 = DropDown(driver, 5)
dropdown1.get_title()
dropdown2.get_title()
dropdown3.get_title()
dropdown4.get_title()
dropdown1.select_user("Denilson Vargas")
dropdown3.select_user("Roger Renjifo")
dropdown_fabian.get_title()
dropdown_denisse.get_title()
time.sleep(5)