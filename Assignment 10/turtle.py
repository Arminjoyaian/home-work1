from turtle import *
pencolor = ('bule')
for i in range(50):
    forward(50)
    left(53)
done()


from turtle import *
color('res' , 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1 :
        break
end_fill()
done()
