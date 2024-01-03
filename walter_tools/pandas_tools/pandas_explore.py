import numpy as np
import pandas as pd

print(pd.__version__)
# 创建Series对象
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=["a", "b", "c", "d", "e", "f"])
print(s)

# 创建DataFrame对象
data = {'Site': ['Google', 'Runoob', 'Wiki'], 'Age': [10, 12, 13]}
df = pd.DataFrame(data)

print(df)
