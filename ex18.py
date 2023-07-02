#  函数  
# this one is like your script with argv

def print_two(*args):
    arg1,argv2 = args
    print(f"arg1:{arg1},arg2:{argv2}")

# ok ,that *agrv is actually pointless, we can just do this

def print_two_again(arg1,arg2):
    print(f"arg1:{arg1},arg2:{arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1:{arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("zed","shaw")
print_two_again("zed","shawsss")
print_one("first!")
print_none()