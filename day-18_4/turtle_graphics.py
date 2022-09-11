import turtle
import random

screen = turtle.Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


class TurtleGraphics:

    def __init__(self):
        self.bot = turtle.Turtle()
        self.bot.shape('circle')
        self.idx = 0

    def drawCircle(self):
        while self.idx < 100:
            self.bot.pencolor(random_color())
            self.bot.speed(9)
            self.bot.circle(100)
            current_heading = self.bot.heading()
            self.bot.setheading(current_heading + 5)
            self.idx += 1
