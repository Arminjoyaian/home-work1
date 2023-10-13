myset = {'a' , 'o' , 'u' , 'i' , 'e'}
myset.remove('u')
print(myset)

myset.add('u')
print(myset)

myset.remove('a')
myset.remove('e')
print(myset)
myset.update(['a' ,'e'])
print(myset)

myset.discard('u')
print(myset)


myset.clear()
print(myset)


myset.copy()
print(myset)

s ={2 , 9 ,8 ,5 ,4 ,0}
m = {3 ,2 ,9 ,0 ,5, 4 ,10}
print(s & m)
print(s - m)
print(m - s)
print(s ^ m)