# return

def add(a,b):
    print(f"Adding {a} + {b}")
    return a+b

def substract(a,b):
    print(f"Substracting {a} - {b}")
    return a-b

def multiply(a,b):
    print(f"multiplying {a} * {b}")
    return a * b

def divide(a,b):
    print(f" dividing {a} / {b}")
    return a / b

def math(a,b,c,d):
    print(f"we are doing ({a} + {b}) /( {c}-{d})")
    return (a + b) / (c -d)

print("Let's do some math with just functions!")

age = add(30,5)
height = substract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age:{age},Height:{height} ,Weight:{weight},IQ:{iq}")

# A puzzle for the extra credit,type is in anyway

print("Here is the puzzle")

what = add(age,substract(height,multiply(weight,divide(iq,2))))

print("That becomes: ",what,"can you do it by hand?.")

fl = float(input(">>>"))

result = math(10,5,9,fl)
print("计算的结果是",result)