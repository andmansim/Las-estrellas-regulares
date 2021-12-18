import random
from turtle import *

def stars(x1,y1):
    color('white') # color of the star 
    goto(x1,y1)
    color('blue') # color of the star 
    for i in range(0,9):
            forward(100)
            left (160)
            

x = 0.00
y = 0.00

a = 0
while a != 5:
     
    stars(x,y)
    a = a + 1
    
    y = y + 90.00
    x = x + 90.00

done()  # finished