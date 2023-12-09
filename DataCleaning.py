import pandas as pd

a = input("请输入一个字符串：")
b = a.split(" ")
c = [i for i in b if not (('➞' in i) or ('-' in i) or ('分' in i) or ('秒' in i))]

# 将列表c转换为DataFrame
df = pd.DataFrame(c, columns=['内容'])

# 将DataFrame保存为Excel文件
# df.to_excel('output.xlsx', index=False, engine='openpyxl')  

##----
#   以上代码实现了，净化数据，将内容只处理保存开始时间、结束时间、使用项目；但是现在所有数据都是在第一列，还需要对于数据处理，处理到没每三行转置到一行数据中 
## ---   
