from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# time.sleep(3)#等待页面加载
# print(driver.page_source)#browser.page_source是获取网页的全部html

# 获取页面组件
input = driver.find_element(by=By.ID,value="kw")  # 找百度搜索输入框
button = driver.find_element(by=By.ID,value="su")  # # 找到“百度一下”的按钮

# 操作页面组件
input.send_keys("waltersun.cn")  # 输入框输入关键字，查找本人博客（搜这个关键词就能找到）
# time.sleep(3)
button.click()  # 点击“百度一下”进行搜索
time.sleep(5)  # 等待页面加载
link = driver.find_element(by=By.ID,value="1").find_element(by=By.TAG_NAME,value="a")
link.click()

driver.quit()