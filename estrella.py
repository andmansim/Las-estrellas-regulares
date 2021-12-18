import random
from turtle import *

def stars(x1,y1):
    color('white') # color of the star 
    goto(x1,y1)
    color('blue') # color of the star 
    for i in range(0,9):
            forward(100)
            left (160)
            
'''
def movement(x2, y2):
    if (x2, y2) == (90.00, 90.00):
        x2 = -x2
        y2 = y2
    elif (x2, y2) == (-90.00, 90.00):
        x2 = -x2
        y2 = -y2
    elif (x2, y2) == (-90.00, -90.00):
        x2 = x2
        y2 = -y2
    return x2, y2
'''
x = 0.00
y = 0.00

a = 0
while a != 5:
     
    stars(x,y)
    #movement(x,y)
    if (x,y) == (0.00, 0.00):
        x = 90.00
        y = 90.00
    elif (x, y) == (90.00, 90.00):
        x = -x
        y = y
    elif (x, y) == (-90.00, 90.00):
        x = x
        y = -y
    elif (x, y) == (-90.00, -90.00):
        x = -x
        y = y
    

    
    a = a + 1
    
    

done()  # finished