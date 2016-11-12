#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By

display = Display(visible=0, size=(800, 600))
display.start()

browser = webdriver.Chrome('/root/chromedriver')

browser.get('https://www.noip.com/login')

# Page loaded
#print browser.page_source

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("<ACCOUNTS_USER_NAME>")
password.send_keys("<PASSWORD>")

browser.find_element_by_name("Login").click()

# Logged in to page
#print browser.page_source

# Go to Dynamic DNS page
browser.get('https://my.noip.com/#!/dynamic-dns')

# Hostnames
print browser.page_source.encode('utf-8')


browser.implicitly_wait(60)

#Click link
browser.find_element_by_xpath("//*[@id='host-panel']/table/tbody/tr/td[5]/span/span/div/a").click()

browser.quit()
