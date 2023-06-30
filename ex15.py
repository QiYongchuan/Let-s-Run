# 读取文件  (一) 读
# 用open 来获取打开文件  用read()方法来读出来
# 这里需要输入对应的文件名字

from sys import argv

script , filename = argv

txt = open(filename)

print(f"Here is your file {filename}:")
print(txt.read())

txt.close()
print("Type the filename again:")
file_again = input(">>")

txt_again = open(file_again)

print(txt_again.read())