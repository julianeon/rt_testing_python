# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://rippletrade.com/")
    wd.find_element_by_link_text("Sign Up").click()
    wd.find_element_by_id("register_username").click()
    wd.find_element_by_id("register_username").clear()
    wd.find_element_by_id("register_username").send_keys("yuiyoxui")
    wd.find_element_by_id("register_password").click()
    wd.find_element_by_id("register_password").clear()
    wd.find_element_by_id("register_password").send_keys("b1zd3vf0r3v3r")
    wd.find_element_by_id("register_password2").click()
    wd.find_element_by_id("register_password2").clear()
    wd.find_element_by_id("register_password2").send_keys("b1zd3vf0r3v3r")
    wd.find_element_by_id("register_email").click()
    wd.find_element_by_id("register_email").clear()
    wd.find_element_by_id("register_email").send_keys("julianine+yuiyoxui@gmail.com")
    if not wd.find_element_by_id("terms").is_selected():
        wd.find_element_by_id("terms").click()
    wd.find_element_by_xpath("//div[@id='t-register']//button[.='Sign UpMigrate Account']").click()
    wd.find_element_by_xpath("//div[@id='t-register']/section/div[4]/div[2]/div[5]/button").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
