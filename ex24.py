print("Let's practice everything!")
print('You\'d need to know \'about escapes with \\ that do :')
print('\n newlines and \t tabs.')

poem = '''
\tThe lovely world
with logic so firmly planted
can not discern \n the needs of love
nor comparehend passion from intuition
and requres and explanation
\n\twhere there is none.
'''

print("--------------------")
print(poem)
print("--------------------")

five = 10 - 2 +3 -6
print(f"This is should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars /100
    return jelly_beans,jars,crates

start_point = 10000
beans,jars,crates = secret_formula(start_point)

# remeber that this is another way to format a string

print("With a starting point of : {}".format(start_point))

#it's just like with an f"" string

print(f"we'd have {beans}beans, {jars} jars , and {crates} creats.")

start_point =start_point/10

print("we can also do that this way:")
format = secret_formula(start_point)

# this is an easy way to apply a list to format string

print("we'd have {} beans,{} jars, and {} creates.".format(*format))
