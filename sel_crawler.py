from selenium import webdriver
from selenium.webdriver.common.keys import Keys
drv = webdriver.Firefox()
link = "http://e1.englishtown.com/partner/englishcenters/cn"
drv.get(link)
username = drv.find_element_by_id("username")
password = drv.find_element_by_id("password")
username.send_keys("zyuruc")
password.send_keys("120215")
drv.find_element_by_class_name("etc-login-btn").click()
print drv.page_source
