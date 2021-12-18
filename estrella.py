import random
from turtle import *

def stars(x1,y1):
    color('white') # color of the star 
    goto(x1,y1)
    color('blue') # color of the star 
    for i in range(0,9):
            forward(100)
            left (160)
            

def movementx():
    x2 = float(random.randint(-200,200))
   
    if 0 < x2 < 100:
        x2 = x2 + 110
      
    return x2


def movementy():
    y2 = float(random.randint(-200,200))
   
    if 0 < y2 < 100:
        y2 = y2 + 110
      
    return y2


x = 0.00
y = 0.00

a = 0
while a != 5:
     
    stars(x,y)
    x = movementx()
    y = movementy()
    print(x)
    a = a + 1
    
    

done()  # finished