class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I am classy apples!")


thing = MyStuff()
thing.apple()

print(thing.tangerine)


# 对象

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def join_song(self):
        a_word_song = '#&***$'.join(self.lyrics)
        print(a_word_song)


happy_bday = Song(["Happy birthday to you",
                  "I don't want to get sued", "So,I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                       "With pocketsfull of shells"])

aWord = Song(["This is a word", "in the futher",
             "i will join all togher!", "yes"])
print("*"*10)
aWord.join_song()

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
