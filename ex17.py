# 文件操作，从一个文件复制内容到另一个
# 选择你的一个现存文件，复制到新文件中，如果新文件不存在，就新建一个，如果存在就不新建。因为out_file本质上执行的是w操作

from sys import argv
from os.path import exists

script,from_file,to_file = argv

print(f"Copying from {from_file} to {to_file}")

# We could do these two on one line,but how? 

# in_file = open(from_file)
# indata = in_file.read()

indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exits? {exists(to_file)}")
print("Ready,hit Enter to continue , Ctrl-C to abort.")

input(">>>>")

out_file = open(to_file,'w')
out_file.write(indata)

print("Alright,all done")

out_file.close()
# in_file.close()

# 其实就是读一个文件，到一个变量中； 再执行写入操作