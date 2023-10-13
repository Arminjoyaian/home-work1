
while True:
    num= int(input("11: Celsius to Kelvin _ 12:Celsius fahrenheit _ 13:Kelvin to celsius _ 14:Kelvin to fahrenheit _ 15:fahrenheeit to celsius _ 16:fahrenheeit to kelvin: , Enter number:      "))
    if 10 < num < 17:
        num0 = float(input("Enter number"))
        if num == 11:
            m = num0 + 273.15
        elif num == 12:
            m = (num0 * 9 / 5) + 32
        elif num == 13:
            result = num0 - 273.15
        elif num == 14:
            m = (num0 - 273.15) * 9 / 5 + 32
        elif num == 15:
            m = (num0 - 32) * 5 / 9 
        elif num == 16:
            m = (num0 - 32) * 5 / 9 + 273.15
            print(m)
        else:
             print("not Ture")
