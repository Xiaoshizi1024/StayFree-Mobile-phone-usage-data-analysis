import openpyxl

# 打开Excel文件
workbook = openpyxl.load_workbook(r'C:\Users\Administrator\Desktop\output2.xlsx') #这个表单需要链接DataCleaning中做出来的文件

# 选择第一个工作表
worksheet = workbook.active

# 获取第一列数据
column_data = [cell.value for cell in worksheet['A']]

# 将数据每三个转成一行
rows = [column_data[i:i+3] for i in range(0, len(column_data), 3)]

# 输出结果
for row in rows:
    print(row)

# 关闭Excel文件
workbook.close()