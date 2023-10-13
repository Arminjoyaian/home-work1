my_list = []
Total = []
for i in range(10):
    number = int(input("Enter number :"))
    my_list.append(number) 
m = 0 
while m < len(my_list):
    Total_1 = my_list[m] + 2
    Total.append(Total_1)
    m = m + 1
print(my_list , end = '')
print(Total)

