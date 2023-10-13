number = int(input("Enter number?"))
z = number % 2
b = number % 10
if 0 == z and  b > 6:
    print("A")
elif b < 4:
    print("B")
else:
    print("C")   
if number < 0 :
    print("D")