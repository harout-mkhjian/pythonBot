from selenium import webdriver
import time

browser = webdriver.Chrome('E://ToolsforProgramming/chromedriver80.exe')
for x in range(0, 30):
    browser.get('https://staging.estateguru.co/portal/registration/signup')
    email = browser.find_element_by_id('regEmail')
    password = browser.find_element_by_id('regPassword')
    email.send_keys("harout.estateguru+ara" + str(x) + "@gmail.com")
    password.send_keys("password")
    reg = browser.find_element_by_id("register")
    time.sleep(2)
    reg.click()
    time.sleep(2)
exit()
