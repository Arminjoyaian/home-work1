def isprime (number):
    a = 0
    for i in range(1, number+1):
        if number%i == 0:
            a+=1
    if a==2:
        print('your isprime')
    else:
        print('It is composite')
        
number = int(input("Enter number :"))
isprime(number)