import random
from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=500,height=500)
user_guess=screen.textinput(title="Make a bet",prompt="Choose a colour of turtle")
print(user_guess)


def object_create(obj,colour,xc,yc):
    obj.shape("turtle")
    obj.color(colour)
    obj.penup()
    obj.goto(x=xc,y=yc)
    obj.pendown()

def game(obj):
    obj.penup()
    obj.forward(random.randint(0,30))
    obj.pendown()

def check_finish(obj):
    if obj.xcor() > 240:
        return 0,obj.pencolor()
    else:
        return 1,obj.pencolor()


red=Turtle()
blue=Turtle()
green=Turtle()
yellow=Turtle()
brown=Turtle()
object_create(red,"red",-230,200)
object_create(blue,"blue",-230,100)
object_create(green,"green",-230,0)
object_create(yellow,"yellow",-230,-100)
object_create(brown,"brown",-230,-200)

condition = True
while condition == True:
   list = [red,blue,green,yellow,brown]
   for i in list:
       result,winner = check_finish(i)
       if result == 0:
           condition = False
           break;
           break;
       else:
           game(i)
if winner == user_guess:
    print(" You Won!!!")
else:
    print(f"You lose: winner is {winner}")
