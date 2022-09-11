import turtle_graphics
import turtle
import colors
import random

screen = turtle.Screen()

idx = 0
while idx <=100:
    val = 't_'+str(idx)
    val = turtle_graphics.TurtleGraphics()
    val.bot_move()

screen.exitonclick()
