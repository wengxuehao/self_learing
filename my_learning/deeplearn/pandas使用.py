import pandas as pd
from IPython.display import display
data = {
    "name":['张三','李四','王五'],
    "addr":['北京','上海','安徽'],
    "age":[18,19,20]
}
# pandas的DataFrame 类似于数据表格结构
data_pandas = pd.DataFrame(data)
# display的优化展示
display(data_pandas)
print('aaaaaaa')
# 查询操作
print(data_pandas[data_pandas.age>19])