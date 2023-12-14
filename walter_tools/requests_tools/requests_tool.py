# !/usr/bin/python3
import requests

import requests
import json

# 发送GET请求
response = requests.get('https://www.waltersun.cn')

# 打印请求结果
print(response.status_code)  # 获取响应状态码
print(response.text)  # 获取响应内容

# 发送带参数的GET请求
params = {'page': 1, 'limit': 10}
response = requests.get('https://www.waltersun.cn', params=params)
# 打印请求结果
print(response.status_code)  # 获取响应状态码
print(response.text)  # 获取响应内容

# 发送POST请求
data = {'title': 'New Post', 'content': 'This is a new post.'}
response = requests.post('https://www.waltersun.cn', data=data)
# 打印请求结果
print(response.status_code)  # 获取响应状态码
print(response.text)  # 获取响应内容

# 发送带JSON数据的POST请求

data = {'title': 'New Post', 'content': 'This is a new post.'}
headers = {'Content-Type': 'application/json'}
response = requests.post('https://www.waltersun.cn', data=json.dumps(data), headers=headers)

# 处理响应
if response.status_code == 200:
    print('请求成功')
    print(response.json())  # 将响应内容解析为JSON格式
else:
    print('请求失败')
    print(response.text)  # 获取响应内容

# 添加请求头
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get('https://www.waltersun.cn', headers=headers)
