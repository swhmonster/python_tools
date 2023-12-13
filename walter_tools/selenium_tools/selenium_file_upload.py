# !/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()
driver.get("https://zhilian.ctyscourt.gov.cn/?fybh=3184#/hyfw/3184")

# 将相对路径转换为当前工作目录下的绝对路径
upload_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "selenium-snapshot.png"))

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(upload_file)
driver.find_element(By.ID, "file-submit").click()

driver.quit()