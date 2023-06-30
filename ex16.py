# 读写文件 （二） 写
from sys import argv
script , filename =argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRLL-C (^C).")
print("If you want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename,'w')
# 打开文件并执行 w 写操作.

print("Truncating the file. Goodbye!")

target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close it.")
target.close()

txt = open(filename)

print(f"Here is your file {filename}:")
print(txt.read())


print("Now I'm going to append you for three lines.")

line1 = input("line 1+: ")
line2 = input("line 2+: ")
line3 = input("line 3+: ")

print("Opening the file...")
target = open(filename,'a+')

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close it.")
target.close()