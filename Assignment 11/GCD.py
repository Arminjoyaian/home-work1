def GCD (a , b):
    x = 0 
    d = 0 
    if abs(a) > abs(b):
        x = abs(a)
    else:
        d = abs(b)
    for i in range(1 , x + 1):
        if a % i == 0  and b % i == 0 :
            d = i
            print(d)
    return d
a = int(input("Enter number : "))
b = int(input("Enter number : "))
c = GCD(a , b)

print("LCN:", c)