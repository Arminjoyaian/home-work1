import random
number = int(input("Enter number :"))
add = []
while len(add) < number :
    n = random.randint(1 , 100)
    if n in add  :
        continue
    else:
        add.append(n)
print(add)