from datetime import date
today = date.today()
print(today)
day = int(input("Enter day :"))
month = int(input("Enter month: "))
year_1 = int(input("enter year : "))
days = (today.year - year_1) * 365 + (today.month - month) * 30 + today.day - day
weeks = days / 7
seconds = ((days * 24) * 60) * 60
a= ( weeks , f"{year_1}.{month}.{day}")
b = (days, f"{year_1}.{month}.{day}")
c =(seconds, f"{year_1}.{month}.{day}")
print(a , b , c )