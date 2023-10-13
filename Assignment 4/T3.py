weight = float(input("Enter weight (kg)?"))
height = float(input("Enter height (cm)?"))
Bmi = (weight / 10) * (10 ** 5 ) / (height * height)
print(Bmi)
if Bmi < 18.5:
    print("under weight")
if 18.5 <= Bmi <25:
    print("normal")
elif 25<= Bmi < 30:
    print("Overweight")    
elif 30 <= Bmi <35:
    print("fat")   
else: 
    print("very fat")    
