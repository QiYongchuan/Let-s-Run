from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    while True:
        choice = input("> ")
        if choice.isdigit():
            how_much = int(choice)
            if how_much < 50:
                print("Nice, you are not greedy , you win! 🎉🎈 ")
                exit(0)
            else:
             dead("You are greedy bastard! 你真是一个贪婪的混蛋 😏 ")

        else:
            print("Man,learn to type a number  🔢 😠")
       
def bear_room():
    print("This is a bear here.这里有一只熊 🐻")
    print("The bear has a bunch of honey. 熊有一罐蜂蜜🍯")
    print("The fat bear is in front of another door. 熊在另一个门前🚪")
    print("How are you going to move the bear? 你要移动这只熊嘛")
    print("    take honey （拿走蜂蜜）  #1\n  taunt bear（嘲弄熊）   #2"
    )
    bear_moved = False

    while True:
        choice = int(input(">> "))

        if choice == 1:
            dead("The bear looks at you then slaps your face off.熊吃掉了你的脸！")
        elif choice ==  2 :
            print("The bear has moved from door.熊从门前走掉")
            print("You can go through it now.")
            bear_moved = True
            print("  take honey   #1\n  taunt bear（嘲弄熊）   #2")
        elif choice == 3 and bear_moved:
            dead("The bear gets pissedd off and chews your leg off.")
        elif choice ==  4 and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He,it,whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input(">> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why,"Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take? left #1  or right #2")

    choice = int(input(">> "))

    if choice == "left" or 1:
        bear_room()
    elif choice == "right" or 2:
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start() 