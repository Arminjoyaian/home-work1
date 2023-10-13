Sentences = input("Enter Sentences :")
Sentences = Sentences.split()
Sentences = '' .join(Sentences)
b =0
for i in range(len(Sentences) // 2):
    if Sentences[i] == Sentences[b]:
        print("is not")
        exit(0)
    else:
        b = b +1
print("LT is")