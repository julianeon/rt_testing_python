import sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

ripple_name="ncawz"
pwd="snyP8vcBeCLpe3Dmj5CP3xufA1BQ6"
def get_name(string):
  try:
    sys.argv[1]
  except IndexError:
    print "Using randomly generated name."
    ripple_name=string
  else:
    ripple_name=sys.argv[1]
  return ripple_name

def send_key(name_id,key):
  username = driver.find_element_by_id(name_id)
  username.send_keys(key)

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://staging.rippletrade.com/#/login")
driver.find_element_by_css_selector(".btn.btn-link.recover").click()
send_key("recover_username",ripple_name)
send_key("recover_masterkey",pwd)
driver.find_element_by_css_selector(".btn.btn-block.btn-success").click()

