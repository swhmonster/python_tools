# !/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver = webdriver.EdgeOptions()
driver = webdriver.Chrome()
driver.get("fulfill your url")

login_options = driver.find_elements(by=By.TAG_NAME, value="span")
for login_option in login_options:
    if login_option.text == '员工登录':
        # 切换到员工登录
        login_option.click()
        login_button = driver.find_element(by=By.CLASS_NAME, value="staff-login-btn")
        login_button.click()
        break

# 员工登录
driver.find_element(by=By.ID, value="account").send_keys("******")
driver.find_element(by=By.ID, value="password").send_keys("******")
driver.find_element(by=By.CLASS_NAME, value="next-btn-helper").click()

# 等待进入页面
time.sleep(15)
iframe = driver.find_element(by=By.ID, value="iframe-page-1")
driver.switch_to.frame(iframe)
span_list = driver.find_elements(by=By.TAG_NAME, value="span")
for span in span_list:
    print(span.text)
    if '数据接入' in span.text:
        span.click()
        break

driver.quit()
