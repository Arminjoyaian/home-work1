names = ["ali", "atefe", "reza", "homa", "amir", "fateme"]
a =int(input("enter number :"))-1
b = str(input("Enter name :"))
c = int(input("enter number :"))-1
n = str(input("Enter name :"))
e =int(input("enter number :"))-1
v = str(input("Enter name :"))
if a <= 7 and c <= 8 and e <= 9:
    names.insert(a , b)
    print(names)
    names.insert(c , n)
    print(names)
    names.insert(e , v )
    print(names)
else:
    print("Not true")