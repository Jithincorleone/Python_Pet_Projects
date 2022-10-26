import turtle
import colorgram
import random

class TurtleGraphics(turtle.Turtle):

#    colorList = []

    def __int__(self):
        super().__init__()
    #     color = colorgram.extract('colors.jpg', 20)
    #     for i in range(0, 20):
    #         rgb = color[i].rgb
    #         self.colorList.append(rgb)
    #
    # def get_colors(self):
    #     val = random.randint(0, len(self.colorList)-1)
    #     color = self.colorList[val]
    #     return color

    def init_turtle(self, pos, color):
        self.shape('circle')
        self.color(color)
        self.penup()
        self.goto(pos)
        self.speed(5)


class Mouth(turtle.Turtle):

    def __int__(self):
        super().__init__()

    def create_mouth(self, x_cor, y_cor):
        self.shape("square")
        self.color("black")
        self.resizemode("user")
        self.shapesize(0.8, 0.8, 0.8)
        self.setx(int(x_cor))
        self.sety(int(y_cor))


