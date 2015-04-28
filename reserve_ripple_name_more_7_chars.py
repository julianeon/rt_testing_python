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

length=8
string= ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(length))
print string

ripple_name=get_name(string)

email_name="julianine"
domain="gmail.com"
pwd="b1zd3vf0r3v3rand3v3r"

driver = webdriver.Firefox()
driver.get("http://staging.rippletrade.com/#/register")

def send_key(name_id,key):
  username = driver.find_element_by_id(name_id)
  username.send_keys(key)

assert "Ripple Trade" in driver.title
email=email_name+'+'+ripple_name+'@'+domain
driver.implicitly_wait(10)
send_key("register_username",ripple_name)
send_key("register_password",pwd)
send_key("register_password2",pwd)
send_key("register_email",email)
driver.find_element_by_id("terms").click()
driver.find_element_by_css_selector(".btn.btn-block.btn-success").click()
driver.find_element_by_xpath("//div[@id='t-register']/section/div[4]/div[2]/div[5]/button").click()

#driver.close()

