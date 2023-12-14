# !/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# config
merchant_Name = 'AMS'

# driver = webdriver.EdgeOptions()
driver = webdriver.Chrome()
driver.get(
    "")

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
elements = driver.find_elements(by=By.CSS_SELECTOR, value=".next-btn.next-medium.next-btn-primary")
for element in elements:
    print(element.text)
    if '数据接入' in element.text:
        element.click()
        break

# 下拉筛选选择
select_element = driver.find_element(by=By.CSS_SELECTOR,
                                     value=".next-formily-item-control.next-formily-item-item-col-12")
select = Select(select_element)
select.select_by_visible_text(merchant_Name)
driver.quit()
