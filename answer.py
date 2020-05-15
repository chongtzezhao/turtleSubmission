from turtle import *
import time
from random import randint

speed(0)
pencolor('white')
bgcolor('black')

x = 0

up()
fd(200)
lt(90)
down()


up()
rt(90)
bk(200)
lt(90)
fd(90)
rt(90)
down()
while x < 120: # while the value of x is lesser than 120,
                #continuously do this:
    for i in range(5):
        fd(200)     
        rt(73)
    circle(randint(1, 100)+10)
    rt(12)
    up()
    fd(20)
    down()
    x+=1
    
    
