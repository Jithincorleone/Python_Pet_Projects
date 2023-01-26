import turtle
import game_screen
import gen_food
import turtle_graphics
import time
import colorgram
import random
import SppechRecognizer
from threading import Thread
from queue import Queue

# import SpeechRecognizer

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
    val = random.randint(0, len(p_color_list) - 1)
    color = p_color_list[val]
    return color


class GameLogic:
    audio_command = Queue()
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

    def audio_deamon(self):
        audio_start = True

        while audio_start:
            text = SppechRecognizer.get_audio_command()
            # print('audio_command : ' + text)
            # if 'left' in text:
            #     turn_left_fun
            # if 'right' in text:
            #     turn_right_fun
            # if 'down' in text:
            #     turn_down_fun
            # if 'up' in text:
            #     turn_up_fun

            #
            #
            self.audio_command.put(text)

    # def audio_movement(self):
    #
    #     while not self.audio_command.empty():
    #         print('audio_command : ' + self.audio_command.get())
    #
    #         audio_command = self.audio_command.get()
    #
    #         if 'left' in audio_command:
    #             turn_left_fun
    #         if 'right' in audio_command:
    #             turn_right_fun
    #         if 'down' in audio_command:
    #             turn_down_fun
    #         if 'up' in audio_command:
    #             turn_up_fun

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
        score_x = -(self.screen.bot.window_width() / 2) + 40
        score_y = (self.screen.bot.window_height() / 2) - 40
        score.setx(score_x)
        score.sety(score_y)
        score.color("White")
        score.write("Score : ", align="left", font=("Verdana", 10, "italic"))

        SppechRecognizer.start_recon()

        audio_thread = Thread(target=self.audio_deamon)
        audio_thread.start()
        # audio_movement_mapper = Thread(target=self.audio_movement)
        # audio_movement_mapper.start()

        points = 0

        while start:

            if not self.audio_command.empty():

                audio_command = self.audio_command.get()
                print('audio_command : ' + audio_command)

                if 'left' in audio_command:
                    turn_left = True
                if 'right' in audio_command:
                    turn_right = True
                if 'do' in audio_command:
                    turn_down = True
                if 'up' in audio_command:
                    turn_up = True


#            audio_thread.join()
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
                score.write("Score : " + str(points), align="left", font=("Verdana", 10, "bold"))

                food.hideturtle()
                del food

                for bots in self.objectList:
                    # bots.color('Red')
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


            print('snake x::'+str(head.xcor()))
            print('snake y::'+str(head.ycor()))

            for pos in self.objectList:
                #if pos.xcor() >= int(self.screen.bot.window_width()) / 2:
                if pos.xcor() >= int(screen_width) / 2:
                    print('Screen x1::' + str(self.screen.bot.window_width()))
                    pos.setx(-int(pos.xcor()))
                    print('after adjust x cor : '+str(pos.xcor()))
                    time.sleep(0.001)
                    self.screen.bot.update()
                #elif pos.xcor() <= -(int(self.screen.bot.window_width()) / 2):
                elif pos.xcor() <= -(int(screen_width) / 2):
                    print('Screen x2::' + str(self.screen.bot.window_width()))
                    pos.setx(int(abs(pos.xcor())))
                    print('after adjust x cor : ' + str(pos.xcor()))
                    time.sleep(0.001)
                    self.screen.bot.update()
                #elif pos.ycor() >= int(self.screen.bot.window_height()) / 2:
                elif pos.ycor() >= int(screen_height) / 2:
                    print('Screen y1::' + str(self.screen.bot.window_height()))
                    pos.sety(-int(pos.ycor()))
                    print('after adjust y cor : ' + str(pos.ycor()))
                    time.sleep(0.001)
                    self.screen.bot.update()
                #elif pos.ycor() <= -(int(self.screen.bot.window_height()) / 2):
                elif pos.ycor() <= -(int(screen_height) / 2):
                    print('Screen y2::' + str(self.screen.bot.window_height()))
                    pos.sety(int(abs(pos.ycor())))
                    print('after adjust y cor : ' + str(pos.ycor()))
                    time.sleep(0.001)
                    self.screen.bot.update()

            # collision with self

            for bot in range(1, len(self.objectList)):
                if head.distance(self.objectList[bot]) < 1:
                    print('collision with self')
                    self.objectList[bot].color('Red')
                    start = False
                    break

            time.sleep(0.100)
            # time.sleep(1)
            self.screen.bot.update()

        if start == False:

            print('in if::')
            for idx in range(0, len(self.objectList)):
                angle = random.randint(0, 360)
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
