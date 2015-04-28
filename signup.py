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

assert "Ripple Trade" in driver.title
driver.implicitly_wait(10)
username = driver.find_element_by_id("register_username")
username.send_keys(name)
username = driver.find_element_by_id("register_password")
username.send_keys(pwd)
username = driver.find_element_by_id("register_password2")
username.send_keys(pwd)
username = driver.find_element_by_id("register_email")
email="julianine+"+name+"@gmail.com"
username.send_keys(email)
username = driver.find_element_by_id("terms").click()
username = driver.find_element_by_css_selector(".btn.btn-block.btn-success").click()
#driver.close()

