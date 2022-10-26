import turtle


class GameScreen:

    def __init__(self, screen_width, screen_height):
        self.bot = turtle.Screen()
        self.bot.setup(width=screen_width, height=screen_height)
        self.bot.bgcolor('black')

    def screen_exit(self):
        self.bot.exitonclick()
