from turtle import *
color('blue')  #color de la estrella

while True:
    forward(100)
    left (160)
    if abs(pos()) < 1: # para que pare
        break

done()