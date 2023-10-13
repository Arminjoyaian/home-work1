number1 = int(input("enter number1 : "))
number2 = int(input("enter number2 : "))

for p in range(1, number2+1):
    for i in range(1, number1+1):
        print(i * p, end = "     ")

    print()