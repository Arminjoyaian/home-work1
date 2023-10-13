number = int(input("Enter number:"))
s = 0

for itam in range(1,number):
    if number % itam == 0:
        s += itam
    
if s == number:
	print('yes')
else:
	print('No')