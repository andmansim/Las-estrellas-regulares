import random
from turtle import *
color('blue')  # color of the star 

def stars():
    while True:
            forward(100)
            left (160)
            if abs(pos()) < 1: # stop drawing
                break
    done() # finished
stars()