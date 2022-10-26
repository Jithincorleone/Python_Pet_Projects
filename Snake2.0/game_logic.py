import turtle
import game_screen
import gen_food
import turtle_graphics
import time
import colorgram
import random
import SpeechRecognizer

startingList = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0)]
turn_left = False
turn_right = False
turn_up = False
turn_down = False


def turn_left_fun():
    global turn_left
    turn_left = True


def turn_right_fun():
    global turn_right
    turn_right = True


def turn_up_fun():
    global turn_up
    turn_up = True


def turn_down_fun():
    global turn_down
    turn_down = True


def get_color(p_color_list):
    val = random.randint(0, len(p_color_list)-1)
    color = p_color_list[val]
    return color


class GameLogic:

    colorList = []

    def __init__(self):
        # self.head = None
        # self.food = None
        self.world_cord_list = []
        self.screen = None
        self.objectList = []
        color = colorgram.extract('colors.jpg', 1)
        for i in range(0, 1):
            rgb = color[i].rgb
            self.colorList.append(rgb)

        print('Game Logic class built complete')

    def get_screen_coordinates(self, height, width):
        t1 = (-int(width), -int(height))
        t2 = (-int(width), int(height))
        t3 = (int(width), int(height))
        t4 = (int(width), -int(height))

        self.world_cord_list.append(t1)
        self.world_cord_list.append(t2)
        self.world_cord_list.append(t3)
        self.world_cord_list.append(t4)

        print('world_cordinate_list : ' + str(self.world_cord_list))

    def play_game(self, screen_width, screen_height):
        global turn_left, turn_up, turn_down, turn_right
        self.objectList = []
        self.screen = game_screen.GameScreen(screen_width, screen_height)
        self.screen.bot.colormode(255)
        self.screen.bot.tracer(n=0, delay=0)

        for pos in startingList:
            t = turtle_graphics.TurtleGraphics()
            t.init_turtle(pos, 'White')
            self.objectList.append(t)

        self.screen.bot.update()

        self.screen.bot.listen()
        self.screen.bot.onkey(key="Left", fun=turn_left_fun)
        self.screen.bot.onkey(key="Right", fun=turn_right_fun)
        self.screen.bot.onkey(key="Up", fun=turn_up_fun)
        self.screen.bot.onkey(key="Down", fun=turn_down_fun)

        start = True
        food = gen_food.Food()
        food.gen_food(int(self.screen.bot.window_height() / 2) - 50, int(self.screen.bot.window_width() / 2) - 50)

        self.get_screen_coordinates(self.screen.bot.window_width(), self.screen.bot.window_height())

        score = turtle.Turtle()
        score.hideturtle()
        score.penup()
        score_x = -(self.screen.bot.window_width()/2)+40
        score_y = (self.screen.bot.window_height()/2)-40
        score.setx(score_x)
        score.sety(score_y)
        score.color("White")
        score.write("Score : ", align="left", font=("Verdana", 10, "italic"))

        speech = SpeechRecognizer.SpeechAudio()
        points = 0

        while start:

            # text = speech.activate_voice_control()
            # print('from game:'+str(text))

            head = self.objectList[0]
            bot_pos = head.pos()
            head.forward(20)
            bot_pos1 = bot_pos

            for idx in range(1, len(self.objectList)):
                bot_pos = self.objectList[idx].pos()
                self.objectList[idx].goto(bot_pos1)
                bot_pos1 = bot_pos

            if str(head.heading()) == "0.0":
                if turn_left:
                    head.left(90)
                    turn_left = False
                if turn_up:
                    head.left(90)
                    turn_up = False
                if turn_down:
                    head.right(90)
                    turn_down = False
                if turn_right:
                    head.right(90)
                    turn_right = False
            elif str(head.heading()) == "90.0":
                if turn_left:
                    head.left(90)
                    turn_left = False
                if turn_right:
                    head.right(90)
                    turn_right = False
            elif str(head.heading()) == "180.0":
                if turn_left:
                    head.left(90)
                    turn_left = False
                if turn_up:
                    head.right(90)
                    turn_up = False
                if turn_down:
                    head.left(90)
                    turn_down = False
                if turn_right:
                    head.right(90)
                    turn_right = False
            elif str(head.heading()) == "270.0":
                if turn_left:
                    head.right(90)
                    turn_left = False
                if turn_right:
                    head.left(90)
                    turn_right = False

            # collision with food
            if head.distance(food) < 15:

                points += 1

                score.clear()
                score.write("Score : "+ str(points) , align="left", font=("Verdana", 10, "bold"))

                food.hideturtle()
                del food

                for bots in self.objectList:
                    #bots.color('Red')
#                    bots.color('black')
                    bots.fillcolor(get_color(self.colorList))
                    time.sleep(0.03)
                    self.screen.bot.update()
                    bots.color('white')

                t = turtle_graphics.TurtleGraphics()
                t.init_turtle(self.objectList[len(self.objectList) - 1].pos(), 'white')
                self.objectList.append(t)

                food = gen_food.Food()
                food.gen_food(int(self.screen.bot.window_height() / 2) - 50,
                              int(self.screen.bot.window_width() / 2) - 50)

                print('Food generated')

            # collision with wall
            for pos in self.objectList:
                if pos.xcor() >= int(self.screen.bot.window_width()) / 2:
                    pos.setx(-int(pos.xcor()))
                    time.sleep(0.001)
                    self.screen.bot.update()
                elif pos.xcor() <= -(int(self.screen.bot.window_width()) / 2):
                    pos.setx(int(abs(pos.xcor())))
                    time.sleep(0.001)
                    self.screen.bot.update()
                elif pos.ycor() >= int(self.screen.bot.window_height()) / 2:
                    pos.sety(int(-pos.ycor()))
                    time.sleep(0.001)
                    self.screen.bot.update()
                elif pos.ycor() <= -(int(self.screen.bot.window_height()) / 2):
                    pos.sety(int(abs(pos.ycor())))
                    time.sleep(0.001)
                    self.screen.bot.update()

           #collision with self

            for bot in range(1, len(self.objectList)):
                if head.distance(self.objectList[bot]) < 1:
                    print('collision with self')
                    self.objectList[bot].color('Red')
                    start = False
                    break


            time.sleep(0.100)
            # time.sleep(1)
            self.screen.bot.update()

        if start == False :

            print('in if::')
            for idx in range(0, len(self.objectList)):
                angle = random.randint(0,360)
#                self.objectList[idx].shape('circle')
#                self.objectList[idx].color('white')
                self.objectList[idx].fillcolor('red')
                self.objectList[idx].seth(angle)
                self.objectList[idx].forward(100)

                time.sleep(0.050)
                self.screen.bot.update()
            turtle.color("White")
            turtle.write("GAME OVER!!", align="center", font=("Verdana", 45, "italic"))

        self.screen.screen_exit()
