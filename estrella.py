import random
from turtle import *
color('blue')  # color de la estrella

def stars():
    while True:
            forward(100)
            left (160)
            if abs(pos()) < 1: # para que pare
                break
    done() # terminar
stars()