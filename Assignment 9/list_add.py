number = [21 , 3 ,54 ,76 ,98 ,32, 2]
dick = {}
for i in number:
    if number in dick:
        dick[number] += 1
    else:
        dick[number]= 1
print(dick)