face = input("the face : ")
d = input('the denominator  :')
class deduction:
    def __init__(self, add_1, add_2):
        self.m1 = add_1
        self.m2 = add_2
    def sub(self):
        ser =  (self.m1[face] * self.m2[d]) - (self.m2[face] * self.m2[d])
        mer = self.m1[d] * self.m2[d]
        print(ser , mer)
    def mul(self):
        ser = self.m1[face] * self.m2[face]
        mer = self.m1[d] * self.m2[d]
        print(ser , mer)
    def sum(self):
        ser = (self.m1[face] * self.m2[d]) + (self.m2[face] * self.m1[d])
        mer = self.m1[d] * self.m2[d]
        print(ser , mer)
    def div(self):
        if self.m2[d] == 0 or self.m2[face] == 0:
            print("")
        elif not(self.m2[d] == 0 or self.m2[face] == 0):
            ser = self.m1[face] * self.m2[d]
            mer = self.m1[d] * self.m2[face]
            print(ser , mer)
        else:
            print("is incorrect")
n = int(input("1=sum , 2=sub , 3=mul , 4=div   :"))
if n == 1 :
    pass
elif n == 2:
    pass
elif n == 3:
    pass
elif n == 4:
    pass