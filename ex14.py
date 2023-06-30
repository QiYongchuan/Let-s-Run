from sys import argv

script,user_name,hoppy = argv
prompt = '>>> '
tips = '==: tea OR milk \n'

print(f"Hi {user_name},I'm the {script} script.I konw you love {hoppy}")
print("I'd like to ask you a few questions")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print("would you like some drinks? tea or milk?")
drink = input(tips)

print(f"""
      Alright,so you said {likes} about liking me.
      You live in {lives}. Not sure where that is.
      And you have a {computer} computer.Nice
      Last your hoppy is {hoppy},and your said you wanna drink some {drink}
      """)
