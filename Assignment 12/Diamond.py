num = int(input("Enter number :  "))

for i in range(num):
    print((num - i) * " ", end=' ')
    print((i * 2 - 1) * '❤')

for i in range(num, 0, -1):
    print((num - i) * " ", end=' ')
    print((i * 2 - 1) * '❤')