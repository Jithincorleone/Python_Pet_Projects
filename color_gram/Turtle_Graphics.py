import turtle
import colorgram
import random

def get_color(p_color_list):
    val = random.randint(0, len(p_color_list)-1)
    color=p_color_list[val]
    return color

class TurtleGraphics:
    colorList = []

    def __init__(self, p_color_num):
        self.bot = turtle.Turtle()
        self.bot.shape('circle')
        self.bot.shapesize(1)
        self.bot.penup()
        self.bot.hideturtle()
        self.bot.setpos(-610, -310)
        self.bot.showturtle()
        self.idx = 0
        color = colorgram.extract('hirst2.jpg', p_color_num)

        for i in range(0, p_color_num):
            rgb = color[i].rgb
            self.colorList.append(rgb)

        print(self.colorList)

    def bloom(self):
        x = self.bot.xcor()
        for i in range(1, 22):
            idx = 1
            y = self.bot.ycor()
            self.bot.penup()
            self.bot.hideturtle()
            self.bot.setpos(x, y+30)
            self.bot.showturtle()
            print('i = '+str(i))
            while idx <= 41:
                self.bot.pencolor('black')
                self.bot.pensize(0)
                self.bot.speed(10)
                self.bot.pendown()
                self.bot.fillcolor(get_color(self.colorList))
                #self.bot.dot(30, get_color(self.colorList))
                self.bot.stamp()
                self.bot.forward(30)
                idx += 1





    # def drawCircle(self):
    #     while self.idx < 100:
    #         self.bot.pencolor(random_color())
    #         self.bot.speed(9)
    #         self.bot.circle(100)
    #         current_heading = self.bot.heading()
    #         self.bot.setheading(current_heading + 5)
    #         print('Current Degree : ' + str(self.bot.heading()))
    #         self.idx += 1
    #         if self.bot.heading() == 0.0 :
    #             self.idx = 100
