# function and file
# 没有搞定打印任意一行的功能

from sys import argv

# script, input_file = argv

input_file = "test.txt"

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(f"这是第{line_count}行的内容：{f.readline().rstrip()}")

    #  readline()读出一行的内容，同时会在这一行结束后加上\n
    #  当你调用 print() 函数打印这些行时，print() 函数本身会添加一个换行符，因此会导致每行之间多出一个空行。
    #要解决这个问题，你可以使用 rstrip() 方法去除每行末尾的换行符。这样就可以确保打印的行不会出现额外的空行。

def printAnyLine(line_count,f):
    print(f"这是第{line_count}行的内容：{f.readline()}")

current_file = open(input_file)

print("First,let's print the whole file:\n")

print_all(current_file)

print("Let's rewind,kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)


# rewind(current_file)
current_line = int(input("请输入你想打印的行数："))
current_file.seek(0)
printAnyLine(current_line,current_file)

current_file.close()


