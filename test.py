import pandas as pd

# 读取Excel文件
data = pd.read_excel("be_bianma_zong.xlsx", sheet_name="yz_instrust")

for index, row in data.iterrows():
    print(index, row)
