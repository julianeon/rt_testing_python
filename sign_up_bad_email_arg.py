import sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

try:
  sys.argv[1]
except IndexError:
  print "You have to enter an argument."
  sys.exit()
else:
  name= sys.argv[1]

pwd="b1zd3vf0r3v3rand3v3r"
driver = webdriver.Firefox()
driver.get("http://staging.rippletrade.com/#/register")

def send_key(name_id,key):
  username = driver.find_element_by_id(name_id)
  username.send_keys(key)

assert "Ripple Trade" in driver.title
email="stupidfakemail.com"
driver.implicitly_wait(10)
send_key("register_username",name)
send_key("register_password",pwd)
send_key("register_password2",pwd)
send_key("register_email",email)
username = driver.find_element_by_id("terms").click()
username = driver.find_element_by_css_selector(".btn.btn-block.btn-success").click()
#driver.close()

