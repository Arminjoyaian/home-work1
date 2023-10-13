from turtle import *
import colorsys as cs
bgcolor('black')
tracer(300)
def draw():
    h = 0
    n = 20
    up()
    goto(0,60)
    down()
    pensize(5)
    for i in range(449):
        c = cs.hsv_to_rgb(h,1,1)
        h += 1/n
        color(c)
        fd(10)
        circle(i,4,5)
        for j in range(550):
            lt(971)
            circle(i*.1, j,steps=2)
            circle(i, 2)
draw()