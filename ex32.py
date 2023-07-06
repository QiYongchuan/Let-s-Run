# 列表和循环  在python中列表list，其实是数组

the_count = [1,2,3,4,5]
fruits = ['apple','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

# this first kind of for-loop goes through a list 

for number in the_count:
  print(f"This is count {number}")

# same as the above

for fruit in fruits:
  print(f"A fruit of type:{fruit}")

# also wo can go through mixed lists too
# notice we have to use {} since we don't know what's in it 

for i in change:
  print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range funcction to do 0 to 5 counts

for i in range(1,6):
  print(f"Adding {i} to the list.")
  # append is a function that lists understand
  elements.append(i)

# now we can print them out too
for i in elements:
  print(f"Element was:{i}")