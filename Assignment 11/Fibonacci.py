def fb(x):
    if x == 0:
        print(0)
    elif x == 1:
        print(1)
    else:
        print(0,1, end=" ")
        c = n  = 0
        for i in range(2, x):
            p = c + n 
            print(p, end=" ")
            c = n
            n = p
number = int(input("Enter number: "))
fb(number)