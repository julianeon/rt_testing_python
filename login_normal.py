import sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

ripple_name="ncawz"
pwd="b1zd3vf0r3v3rand3v3r"

def send_key(name_id,key):
  username = driver.find_element_by_id(name_id)
  username.send_keys(key)

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://staging.rippletrade.com/#/login")
send_key("login_username",ripple_name)
send_key("login_password",pwd)
driver.find_element_by_css_selector(".btn.btn-block.btn-success").click()

