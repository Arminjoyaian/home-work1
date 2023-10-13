import random
dise = []
a = 0
b = 0 
while a != 6:
    dise.append(a)
    a=random.randint(1 , 6)
    b += 1
    if a == 6 :
        print(f"Good job {b}")
        break
    else :
        print(f"Number{b} is :", a)
l = sum(dise) 
print(l + 6)