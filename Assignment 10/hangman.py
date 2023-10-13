import random

Animals = ["cat", "dog", "cow", "pig", "fly", "eik", "fox", "bat", "ant", "bee"]
An_medium = ["deer", "crab", "duck", "fish", "goat", "wolf", "tang", "lion", "hare", "frog"]
Colors= ["red", "blue", "black", "white", "green", "orange", "gold", "gray", "coral", "purple"]
Colors_medium = ["teal", "cyan", "pink", "bice", "puce", "jade", "aero", "fawn", "finn", "erin"]
Musical_instruments_easy = ["harp", "flute", "guitar", "drums", "tuba", "organ", "sitar", "piano", "ukelele", "violin"]
word = random.choice(Animals)
hearts = (len(word) * 1.5) // 1
show_word = []
for i in range(len(word)):
    show_word.append("_")
# print("_"* len(word))
while True:
    # print word hearts
    print(" ".join(show_word))
    print("*" * int(hearts))
    if hearts == 0:
        print("Game over")
        break
    user_char = input("enter character : ")
    # check_end_game
    if not("_" in show_word):
        print("Hip Hip Hoorey!")
        break
    # new_char
    if user_char in word:
        idx = word.index(user_char)
        show_word[idx] = user_char
    else:
        print("this is not exist")
        hearts -= 1









#word = random.choice(Animals)
#hearts = (len(word) * 1.5) // 1
#c = 0 
#for i in word:
 #   c += 1
#x = c *"-"
#n = list(x)
#print(n)
#y = input("Enter a letter :")
#x2 = ''
#while True:
 #   print(" ".join(n ))
 #   print("❤" * int(hearts))
#    if hearts == 0:
    #   print("Game over")
#        break
#while "-" in n :
#    x2 = ''
#    if y in word:
#        for z in range(0 , len(word)):
 #           if word[z] == y :
#                n[z] = word[z]
#            x2 = x2 + n [z]
#        print(x2)
 #       if '-' in n :
 #           y = input("Well done, enter another word:")
   #     else:
#            print("you win")
 #   else :
#        y = input("It was a mistake")