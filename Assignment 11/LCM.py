def LCM (x ,y ):
    a =0
    b =0 
    h = abs(x * y) + 1
    if abs(x)> abs(y):
        a = abs(x)
    else:
        a = abs(y)
    for i in range(a , h):
        if i%x == 0 and i%y == 0 :
            b = i
            break
    return b
x = int(input("Enter number x : "))
y = int(input("Enter number y :"))
o = LCM(x , y)
print(o)