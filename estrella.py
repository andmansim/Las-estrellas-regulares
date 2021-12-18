import random
from turtle import *
color('blue')  # color of the star 

def stars(x1,y1):
    goto(x1,y1)
    for i in range(0,9):
            forward(100)
            left (160)
            
            
           # if abs(pos()) < 1: # stop drawing
          #      break
    #done() # finished

x = 0.00
y = 0.00

a = 0
while a != 50:
     
    stars(x,y)
    a = a + 1
    y = y + 90.00
    x = x + 90.00

done()