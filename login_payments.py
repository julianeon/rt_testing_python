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
#driver.find_element_by_xpath("//div[@id='t-register']/section/div[4]/div[2]/div[5]/button").click()
driver.find_element_by_xpath("//div[@id='wrapper']/header/div[2]/nav/div[4]/div/ul/li[2]/a").click()
#id('t-register')/x:section/x:div[4]/x:div[2]/x:div[5]/x:button
driver.find_element_by_xpath("//div[@id='t-history']/section/group/div[1]/div[1]/div/div[2]/div[1]/label/span").click()
time.sleep(3)
driver.find_element_by_xpath("//div[@id='t-history']/section/group/div[1]/div[1]/div/div[2]/div[1]/label/span").click()
driver.find_element_by_xpath("//div[@id='t-history']/section/group/div[1]/div[1]/div/div[2]/div[2]/label/span").click()
time.sleep(3)
driver.find_element_by_xpath("//div[@id='t-history']/section/group/div[1]/div[1]/div/div[2]/div[2]/label/span").click()
driver.find_element_by_xpath("//div[@id='t-history']/section/group/div[1]/div[1]/div/div[2]/div[3]/label/span").click()

