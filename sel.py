from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://staging.rippletrade.com/#/register")
assert "Ripple Trade" in driver.title
username = driver.find_element_by_id( "register_username" )
username.send_keys( "julian" )
username = driver.find_element_by_id( "register_password" )
username.send_keys( "julian" )
username = driver.find_element_by_id( "register_password2" )
username.send_keys( "julian" )
#driver.close()

