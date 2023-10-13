def str(r):
    o = l =  0
    for i in r:
        if 65 <= ord(i) <= 90:
            o += 1
        elif 95 <= ord(i) <= 120:
            l += 1
    return o, l
p = input("Enter str :  ")
o , l  = str(p)
print(o)
print(l)
