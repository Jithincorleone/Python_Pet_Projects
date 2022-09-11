import turtle
import random

screen = turtle.Screen()
screen.colormode(255)

angleList = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


class TurtleGraphics:
    bot = ''

    def __init__(self):
        self.bot = turtle.Turtle()
        self.bot.shape('circle')
        self.idx = 0

    def bot_move(self):
        self.bot.pensize(10)
        self.bot.speed('slow')

        while self.idx < 100:
            self.bot.pencolor(random_color())
            val = random.randint(0, len(angleList) - 1)
            angle = angleList[val]
            self.bot.seth(angle)
            self.bot.forward(30)
            self.idx += 1
