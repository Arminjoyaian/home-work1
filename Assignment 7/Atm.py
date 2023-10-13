password = '8976'
password_1 = 1
m = 0
while password == '8976':
    password_i = input("enter password:")
    if password_i == password:
        print("log in")
        exit()
    if len(password) > len(password_i):
        print("is low")
        password_i = '1234'

    password_l = list(password) 

    password_li = list(password_i)

    for p in range(4):
        k = (p+1) * -1
        if password_l[p] == password_li[k]:
            m = m +1
    if password_1 == 7:
        print("Closed")
        exit()
    if m == 6:
        print("police")
        exit()
    elif  len(password) < len(password_i):
        password == '8976'
    else:
        print("Is wrong")
        password_1 = password_1 + 1