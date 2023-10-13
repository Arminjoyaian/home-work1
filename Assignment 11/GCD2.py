
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))
p=gcd(num1, num2)
print(p)