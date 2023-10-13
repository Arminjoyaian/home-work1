def word(str):
    for i in str:
        if   ord(i) ==  97 or ord(i) == 65:
            str = str.replace(i, "!")
        elif ord(i) == 101 or ord(i) == 69: 
            str = str.replace(i, "!")
        elif ord(i) == 105 or ord(i) == 73: 
            str = str.replace(i, "!")
        elif ord(i) == 111 or ord(i) == 79:
            str = str.replace(i, "!")
        elif ord(i) == 117 or ord(i) == 85: 
            str = str.replace(i, "!")
    print(str)

s = input("Enter str : ")
print(word(s))