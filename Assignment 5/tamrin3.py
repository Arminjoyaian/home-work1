
num = int(input("enter youre number:"))
num = str(abs(num))
odd = 0
even = 0
even='number'.count(1) + 'number'.count(3) +'number'.count(5)+'number'.count(7)+'number'.count(9)
odd='number'.count(0)+'number'.count(2)+'number'.count(4)+'number'.count(6)+'number'.count(8)
if odd > even:
    print(odd)
elif even > odd:
    print(even)
else:
    print("equal")
print("odd:", odd,"even:", even)
