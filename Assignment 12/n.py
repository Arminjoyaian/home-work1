def add(x):
    o  = []
    o.append(str(x + x*11 + x *111 ))
    x = " ".join(o)
    x = x.replace(" ", "")
    return x

p = int(input("enter number: "))
print(add(p))