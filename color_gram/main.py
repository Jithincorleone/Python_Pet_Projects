import Turtle_Graphics
import turtle

screen = turtle.Screen()
screen.colormode(255)
#screen.setup(width=500, height=500)

screen.bgcolor('black')
t = Turtle_Graphics.TurtleGraphics(20)
t.bloom()

screen.exitonclick()