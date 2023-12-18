import pandas as pd
import matplotlib.pyplot as plt

# 创建Pandas DataFrame对象
data = {'year': [2010, 2011, 2012, 2013, 2014],
        'sales': [5, 8, 12, 10, 15]}
df = pd.DataFrame(data)

# 使用Matplotlib绘制折线图
plt.plot(df['year'], df['sales'])
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales by Year')
plt.show()

# 创建Pandas DataFrame对象
data = {'year': [2010, 2011, 2012, 2013, 2014],
        'sales': [5, 8, 12, 10, 15]}
df = pd.DataFrame(data)

# 使用Matplotlib绘制柱状图
plt.bar(df['year'], df['sales'])
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales by Year')
plt.show()

# 创建Pandas DataFrame对象
data = {'x': [1, 2, 3, 4, 5],
        'y': [2, 4, 6, 8, 10]}
df = pd.DataFrame(data)

# 使用Matplotlib绘制散点图
plt.scatter(df['x'], df['y'])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')
plt.show()

# 创建Pandas DataFrame数据
data = {'Category': ['Data 1', 'Data 2', 'Data 3', 'Data 4'],
        'Value1': [100, 90, 80, 70],
        'Value2': [110, 85, 75, 60],
        'Value3': [120, 95, 70, 50]}
df = pd.DataFrame(data)
# 提取值列的数据
values = df[['Value1', 'Value2', 'Value3']].values

# 使用Matplotlib绘制箱线图
plt.boxplot(values)
# 添加x轴刻度标签
plt.xticks(range(1, len(df.columns)), df.columns[1:])
plt.title('Boxplot')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()


