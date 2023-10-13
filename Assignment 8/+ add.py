number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Sentence = input("sentence:")
list = []
Zero = 0
for i in number:
    for p in Sentence:
        if str(i) == p:
            Zero += i
        else:
            list.append(p)
print(Zero)
