import random
def play(player): 
        r = random.randint(0 , 2)
        if r ==0 :
             computer = 'rock'
        elif r == 1 :
             computer = 'paper'
        else:
             computer = 'scissors '
        print(player)
        print(computer)

        if player == computer:
            print('equal')
        elif player == 'rock':
            if computer == 'scissors':
                print("player win")
            else:
                print("computer win")
        elif player == 'paper':
            if computer == 'rock':
                print('player win')
            else:
                 print('computer win')
        elif player == 'scissors':
            if computer == 'paper':
                 print('player win')
            else:
                print("computer win")
        else:
             print("No")
def play2(player_1 , player_2):
          if player_1 == player_2:
              print('equal')
          elif player_1 == 'rock':
              if player_2 == 'scissors':
                  print("player_1 win")
              else:
                  print("player_2 win")
          elif player_1 == 'paper':
              if player_2 == 'rock':
                  print('player_1 win')
              else:
                  print('player_2 win')
          elif player_1 == 'scissors':
              if player_2 == 'paper':
                  print('player_1 win')
              else:
                  print("player_2 win")
          else:
              print("No _2")

print('10 : "1play"  , 11 : "2play"' )
Play = int(input("Enter number :"))
if Play == 10:
    player = input('rock , paper , scissors    : ')
    play(player)
elif Play == 11:
    player_1 = input('rock , paper , scissors    : player_1 : ')
    player_2 = input('rock , paper , scissors    : player_2 : ')
    print(player_1)
    print(player_2)
    play2(player_1 , player_2)
else:
      print("The entered number is incorrect")