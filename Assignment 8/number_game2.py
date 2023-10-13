import random
a = 0
b =100
number = int(input("Enter number : "))
number_2 = random.randint(a ,b)
while True:
    if number_2 == number :
        print(f"computer:{number_2}","you win")
        number_2 += 1
        break
    elif number_2 > number:
        print(f"computer:{number_2}", "go down")
        number_2 -1 
        number_2 == b
        number = 1 
        number_2 = random.randint(a ,b)
    else:
        print(f"computer:{number_2}", "go up")
        number_2 = -1
        player = number_2
        number =1
        number_2 = random.randint(a ,b )
