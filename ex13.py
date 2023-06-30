# 参数、解包、变量
# 第一个参数是程序的名称，运行时需要输入 python ex13.py first 2nd 3rd
#需要输入三个参数的名称，第一个默认是程序的名称是，即不用输入，script

from sys import argv


script,first,second,thrid = argv

print("The script is called:",script)
print("Your first variable is :",first)
print("Your second variable is:",second)
print("Your third variable is:",thrid)



