#number1 = int(input("Enter number1 :"))
#number2 = int(input("Enter number2 :"))
import math
print("1.- , 2.* , 3.+ , 4./ ")
print("log , sin , tan , cos , ** , ronud , abs ,// , jazr , factorial ,% ")
op = int(input("Enter number?"))
Result = 0
while True:
    if 1<= op <=5:
        num1=int(input("f num:"))
        num2=int(input("s num:"))
        if op ==1:
            Result = num1 - num2
        elif op == 3:
            Result = num1 + num2
        elif op == 4:
            Result = num1 * num2  
        elif op == 10:
            Result = num1 // num2   
        elif op == 11:
            Result = num1 % num2
        elif op == 12:
            Result = num1 ** num2      
        elif op == 2:
            Result = num1 / num2
        elif op == 87:
            Result = math.pow(num1 , num2)        
        mun1 = float(input("enter a mun:"))
        if  op == 5:
            Result= math.log(mun1)
        elif op == 6:
            Result= math.sin(math.radians(mun1)) 
        elif op == 7:
            Result= math.cos(math.radians(mun1))       
        elif op == 8:
            Result= math.tan(math.radians(mun1))  
        elif op == 9:
            Result= abs(mun1) 
        elif op == 15:
            Result=round(mun1) 
        elif op == 16:
            Result= math.factorial(mun1)
        elif op == 17:
            Result= (math.sprt(mun1))
        else:
            print("Again")
