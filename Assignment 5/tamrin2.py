a = input("write your sentence:")
print(a.title())

b = input("write your sentence:")
print(b.istitle())

c =' hello, armin good morning.'
print(c.find('good'))

d = "Hossein is my friend"
print(d.replace("Hossein", "Ali"))

e = "Ali"
print("My friend's name is", e.rstrip())

f = " Ali " 
print("My friend's name is", f .lstrip())


g = "Ali"
print(g.rjust(17), "My friend's name is.")


h = "Ali"
print(h.ljust(10), "My friend's name is")


p = "20"
print(p.zfill(7))
