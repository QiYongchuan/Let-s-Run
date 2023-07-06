# 列表- 如何访问列表的元素
#序数等于有序，从1开始； 基数等于随机选择，从0开始。

animals = ['bear','python3.6','peacock','kangaroo','whale','platypus']

# for animal,i in animals,range(0,6):

#     print(f"第{i+1}只动物是{animal},它的位置是{i}")
 

for i,animal in enumerate(animals):
     print(f"第{i+1}只动物是{animal},它的位置是{i}")

# enumerate 函数会返回一对元素，包括列表中每个元素的索引和对应的值。
# 在 for 循环中，变量 i 会存储当前元素的索引，而变量 animal 则会存储当前元素的值。
# 然后，使用这些变量来输出每个动物及其位置的信息。