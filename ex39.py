# 字典  键值对的形式存储  dict
# 字典的关键是映射 （关联） 一一对应

stuff = {'name':'Zed','age':39,"height":6*12+2}

print(stuff['name'])

# print(stuff[0])   dict只能通过键值对中的键访问元素，

print(stuff['height'])

stuff['city'] = "ShanDong"
print(stuff['city'])

# key的形式，不仅可以使用字符串，还可以使用数字

stuff[1] = "Wow"
stuff[2] = "Neato"

print(stuff[1])
print(stuff[2])

# 使用del 删除创建的键
del stuff[1]

print(stuff)

## 字典的例子

print("**开始字典的例子**"* 3)

# create  a mapping of state to abbreviation

states = {
    "Orengon":'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

# create a basic set of states and some cities in them

cities = {
    'CA':'San Franciso',
    'MI':'Detroit',
    'FL':'Jacksonville',
}

# add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities

print('--' * 10)
print("Michigan has: ", states['Michigan'])
print("Florida has: ",states['Florida'])


# print every state abbreviation

print('**' * 14)
for state,abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")


# print every city in state

print('--' * 20)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city{city}")

# now do both at the same time

print('-' * 10)
for state,abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city:{cities[abbrev]}")

print('--'*10)
# safely get a abbreviation by state that might not there

state = states.get('Texas')

if not state:
    print("Sorry,no Texas")

# get a city with a default value

city = cities.get('TX','Does Not Exist')
print(f"The city for the state 'TX' is: {city}")