import random 
player1 = int(input(f"player1 Guess a number from 1 to 100:"))
while True: 
    player2 = int(input("Guess a number from 1 to 100:")) 
    if player2 < player1: 
        print("is low") 
    if player2 > player1: 
        print("is a lot") 
    if player2 == player1:
        print("good job") 
        try_again = input("do you want to try again?:(y, n) ")
        break
