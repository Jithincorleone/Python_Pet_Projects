#import turtle_graphics
import turtle
import colorgram
import random
p_color_num = 1

color = colorgram.extract('Tree_Color.jpg', p_color_num)
bark = colorgram.extract('Bark_Color.jpg', p_color_num)
color_list = []
bark_list = []

def get_color(p_color_list):
    val = random.randint(0, len(p_color_list)-1)
    color=p_color_list[val]
    return color

for i in range(0, p_color_num):
    rgb = color[i].rgb
    color_list.append(rgb)
    rgb = bark[i].rgb
    bark_list.append(rgb)


screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor('Black')
#screen.setup(500, 500)
#screen.screensize(canvwidth=1000, canvheight=1000)
#screen.setup(width=0.75,height=0.75)
bot = turtle.Turtle()
bot.shape('arrow')
bot.pensize(2)
bot.pencolor()
bot.pencolor(get_color(color_list))
bot.left(90)
bot.penup()
bot.backward(300)
bot.pendown()
bot.speed(100)

itr = 0

def tree(idx):
    global itr
    if idx < 10:
        return
    else:
        itr += 1
        print('Call no ::'+str(itr)+'beginning idx::'+str(idx))
        bot.forward(idx)
        bot.color(get_color(bark_list))
#        bot.begin_fill()
        bot.circle(2)
#        bot.end_fill()
        bot.pencolor(get_color(color_list))
        bot.left(30)
        tree(3*idx/4)
        bot.right(60)
        print('Call no ::'+str(itr)+'later idx::'+str(idx))
        tree(3*idx/4)
        print('Call no ::'+str(itr)+'post second recursion idx::'+str(idx))
        bot.left(30)
        bot.backward(idx)
        print('after backward::'+str(idx))


# def increase_size():
#     size = bot.turtlesize()
#     increase = (10 * num for num in size)
#     bot.pensize()
#     bot.turtlesize(*increase)


tree(150)
#bot.done()

screen.exitonclick()