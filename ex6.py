type_of_people = 10
x = f"There are {type_of_people} types of people" #文本？通过格式化字符f""把变量放入中{}

binary = "binary"
do_not = "don't"
y=f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said : {x}")
print(f"I also said:'{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?{}!"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side"

print(w+e)