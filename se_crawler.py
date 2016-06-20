#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
binary = FirefoxBinary('/home/xFrog/workspace/firefox/firefox')
drv = webdriver.Firefox(firefox_binary=binary)
link = "http://e1.englishtown.com/partner/englishcenters/cn"
drv.get(link)
username = drv.find_element_by_id("username")
password = drv.find_element_by_id("password")
username.send_keys("zyuruc")
password.send_keys("120215")
drv.find_element_by_class_name("etc-login-btn").click()
delay = 10 # seconds
try:
    WebDriverWait(drv, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'ue-menu-list')))
    print "Page is ready!"
except TimeoutException:
    print "Loading took too much time!"
html_list = drv.find_element_by_class_name("ue-menu-list")
items = html_list.find_elements_by_tag_name("li")
for item in items:
    text= item.text
    print text
#print drv.page_source
