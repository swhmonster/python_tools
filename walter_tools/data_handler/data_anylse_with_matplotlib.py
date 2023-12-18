import os
from odps import ODPS
from odps import options
import pandas as pd
import matplotlib.pyplot as plt
import json

o = ODPS(
    access_id=os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'),
    secret_access_key=os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'),
    project='******',
    endpoint='******',
)

options.sql.settings = {"odps.sql.submit.mode": "script", "odps.sql.hive.compatible": "true"}

with open('sqls/overdue_in_transit.json') as f:
    data = json.load(f)

sql = data['sql']
print(sql)

# sql查询与结果读取
result = o.execute_sql(sql)
x_axis_list = []
y_axis_list = []
df_dict = {}
with result.open_reader() as reader:
    for record in reader:
        print(record)
        x_axis_list.append(int(record[data['x-axis']]))
        y_axis_list.append(float(record[data['y-axis']]))
df_dict.update({'x-axis': x_axis_list})
df_dict.update({'y-axis': y_axis_list})

# 绘制图表
df = pd.DataFrame(df_dict)
# 数据过滤
df_filtered = df.dropna()
plt.plot(df_filtered['x-axis'], df_filtered['y-axis'])
plt.xlabel(data['x-axis-label'])
plt.ylabel(data['y-axis-label'])
plt.title(data['title'])
plt.show()
