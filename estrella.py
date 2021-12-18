import random
from turtle import *
color('blue')  # color of the star 

def stars():
    while True:
            forward(100)
            left (160)
            if abs(pos()) < 90: # stop drawing
                break
    done() # finished

x = 90
y = 90

a = 0
while a != 5:
    
    penup(h)
    h = setposition(x,y)
    
    stars()
    a = a + 1
   # x = x + 90