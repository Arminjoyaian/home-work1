s = 'apple'
try:
	num = int(s)
except ValueError:
	raise ValueError("String can't be changed into integer")