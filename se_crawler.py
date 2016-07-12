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
from selenium.webdriver.common.action_chains import ActionChains
binary = FirefoxBinary('/opt/firefox/firefox')
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
li_course = None
for item in items:
    if item.text == "课程":
        li_course = item 
        break;
        print li_course.text
    #text= item.text
#ActionChains(drv).move_to_element(li_course).move_to_element(drv.find_element(By.LINK_TEXT,"我的课程")).click().perform()
ActionChains(drv).move_to_element(li_course).perform()
WebDriverWait(drv, delay).until(EC.presence_of_element_located((By.LINK_TEXT, "我的课程")))
my_course = drv.find_element(By.LINK_TEXT,"我的课程")
ActionChains(drv).move_to_element(my_course).click().perform()
    
#print drv.page_source
