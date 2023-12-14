# !/usr/bin/python3
import requests

import requests

params = {'_e': 'QueryAccountingScene', '_m': 'query'}
response = requests.options('https://api.aidc-dchain.com/river/record-api/invoke', params=params)
# 打印请求结果
print(response.status_code)  # 获取响应状态码
print(response.text)  # 获取响应内容
