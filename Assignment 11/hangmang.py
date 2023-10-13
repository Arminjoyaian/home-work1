import random

Animals = ["cat", "dog", "cow", "pig", "fly", "eik", "fox", "bat", "ant", "bee"]
An_medium = ["deer", "crab", "duck", "fish", "goat", "wolf", "tang", "lion", "hare", "frog"]
Colors= ["red", "blue", "black", "white", "green", "orange", "gold", "gray", "coral", "purple"]
Colors_medium = ["teal", "cyan", "pink", "bice", "puce", "jade", "aero", "fawn", "finn", "erin"]
Musical_instruments_easy = ["harp", "flute", "guitar", "drums", "tuba", "organ", "sitar", "piano", "ukelele", "violin"]
def hang():
    word = random.choice(Animals)
    hearts = (len(word) * 1.5) // 1
    show_word = []
    for i in range(len(word)):
        show_word.append("_")
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

user= input("")
hang(user)