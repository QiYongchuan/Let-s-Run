
# function and variable  函数和变量

from sys import argv
fun , num = argv

def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly")
cheese_and_crackers(20,30)

print("OR,we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

# we can even do math in inside too
cheese_and_crackers(2+11,5+6)

print("And we can combine the two,variables and math:")
cheese_and_crackers(amount_of_cheese * 2,amount_of_crackers+100)



print("And we can combine the argv and  variables ***********************:")
print(f"this is {fun}")
cheese_and_crackers(num,num)

print("And we can combine the input and  variables ***********************:")
cheese_and_crackersInput = int(input("number?:"))
amount_of_cheeseInput = input("nuber:?")

cheese_and_crackers(cheese_and_crackersInput,amount_of_cheeseInput)