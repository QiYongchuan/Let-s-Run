# 读写文件 （二） 设置一个数据记录器
from sys import argv
from datetime import date,datetime

current_date = date.today().isoformat()
current_datetime_s= datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# script , filename =argv

filename = "date.txt"

print(f"This is QYC code datebase: {filename}.")
print("If you don't want that, hit CTRLL-C (^C).")
print("If you want that, hit ENTER.\n")

input("?\n")

print(f"Opening your database in {current_date}....")


txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read())


target = open(filename,'+a')

print("Write your record:\n")
lines = input(">> ")

# target.write(f" 这条记录生成于 {current_datetime_s}\n")
# target.write(lines)
# target.write("\n")

# target.close()


# 读取已有记录的数量，如果文件不存在，则默认为0
try:
    with open('date.txt', 'r') as file:
        count = len(file.readlines())
except FileNotFoundError:
    count = 0

# 获取当前日期和时间并格式化为字符串
current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 自动编号
count += 1
record = f"{count}. {current_datetime} - {lines}"

# 写入文件
with open('date.txt', 'a') as file:
    file.write(record + '\n')


txt = open(filename)


print(f"Here is your file {filename}:")
print(txt.read())



