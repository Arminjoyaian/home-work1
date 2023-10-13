n = int(input())
for i in range(n):
    i += 1 
    for p in range(i + 1):
        p += 1
        print(p , end= '')
    print()

for n in range(n,0 ,-1): 
    for j in range(1,n + 1):
        print(j , end="")
    print()