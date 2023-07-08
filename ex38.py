#列表的操作  一些简单的操作，比如列表转字符串，列表中添加元素，列表取元素等
# 进一步深入理解列表：
# 每个编程的概念都与显示世界某个东西有关，如果你能在现实世界中找到类比，你就能弄明白这个数据结构有什么用。

# 
# 每个编程的概念都与显示世界某个东西油管，如果你能在现实世界中找到类比，你就能弄明白这个数据结构有什么用。
# 现在把一摞纸牌看作列表：
# 1.你有一堆纸牌，每张都有一个值。
# 2.这些纸牌拍成一摞，即一个从上到下的列表。
# 3.然后你可以从上面或者下面取牌，也可以从中间随机抽一张牌
# 4.如果你需要某张特定的牌，你需要一张一张的检查，直到找出那张牌为止

# 再类比列表：

# 有序的列表：是的，纸牌是从头到尾都是有序排列的。
# 要存储的东西：就是我的纸牌；
# 随机访问：我可以从纸牌中抽取任意一张。
# 线性：如果我要找到某张牌，我可以从第一张开始，依次寻找。
# 通过索引：差不多是这样，如果我告诉你找出第19张牌，你需要数到19然后找到这张牌。在python列表中，如果你要某个索引位置的牌，计算机可以直接跳到索引对应的位置将其找出来。


ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that lit. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding",next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print("-1的位置是倒数第一个",stuff[-1])

print("pop是倒数第一个",stuff.pop())

print(' '.join(stuff))  # join 和起来

print("#".join(stuff[3:5]))
