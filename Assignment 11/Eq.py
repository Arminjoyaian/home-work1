import math
def Eq (a , b , c ):
    n = (b ** 2-4*a*c)
    if n > 0:
        x1 = (-b + (math.sqrt(n))) / (2 * a)
        x2 = (-b - (math.sqrt(n))) / (2 * a)
        print(x1 , x2)
    elif n == 0 :
        x3 = (-b / (2 * a))
        print(x3)
    else:
        print("There is no answer")

a = int(input("Enter number a:"))
b = int(input("Enter number b:"))
c = int(input("Enter number c:"))
Eq(a ,b , c )