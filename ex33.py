# while 循环
i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i+1
    print("Numbers now: ",numbers)
    print(f"At the bottom i is {i}")
    print("The numbers: ")

    for num in numbers:
        print(num)


## 将while 函数写成一个函数，将测试条件中的改成一个变量
# x = int(input(">>:number:"))

def fun(x,z):
    y =0
    numbers2 = []
    while y < x:
        numbers2.append(y)
        y = y+z
        print("Numbers now: ",numbers2)


x= int(input("number:"))
z = int(input("number:"))
fun(x,z)


# 使用for 与range()来改写程序

for i in range(0,6):
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i+1
    print("Number now: ",numbers)
    print(f"At the bottom i is {i}")

    print("The numbers: ")
    for num in numbers:
        print(num)