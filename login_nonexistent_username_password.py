import sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

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

length=20
name_string= ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(length))
password_string= ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(length))
password_string=password_string+'X@#$%'
print name_string
print password_string

ripple_name=get_name(name_string)

email_name="julianine"
domain="gmail.com"
pwd=password_string

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://staging.rippletrade.com/#/login")
send_key("login_username",ripple_name)
send_key("login_password",pwd)
driver.find_element_by_id("loginBtn").click()
