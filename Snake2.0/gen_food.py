import turtle
import random


class Food(turtle.Turtle):

    def __int__(self):
        super().__init__()

    def gen_food(self, max_height, max_width):
        x_cor = random.randint(1, int(max_height))
        y_cor = random.randint(1, int(max_width))
        self.shape('circle')
        self.color('yellow')
        self.resizemode("user")
        self.shapesize(0.5, 0.5, 0.5)
        self.penup()
        pos = (int(x_cor), int(y_cor))
        self.setpos(pos)

    def del_food(self):
        self.clear()

    def __del__(self):
        print('Food Eaten')
