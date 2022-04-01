import turtle
from turtle import Turtle, Screen
import random
bala_the_turtle = Turtle()
bala_the_turtle.hideturtle()
turtle.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

def square():
    for i in range(0,4):
        turtle.dot(20,"blue")
        bala_the_turtle.forward(100)
        bala_the_turtle.right(90)


def drawdot(space, x,tur):

    for i in range(x):
        for j in range(x):
            r, g, b = random_colour()
            turtle.pencolor((r, g, b))
            tur.dot()


        tur.right(90)
        tur.forward(space)
        tur.left(90)
def dash(tur):
    for i in range(15):
      tur.forward(5)
      tur.penup()
      tur.forward(5)
      tur.pendown()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw(side):
  angle = 360 / side
  for i in range(side):
    bala_the_turtle.forward(100)
    bala_the_turtle.left(angle)
  for i in range(side):
    bala_the_turtle.forward(100)
    bala_the_turtle.right(angle)

def random_walk(turtle):
  for i in range (0,200):

    angle = [90,270,180,360]
    turtle.pensize(15)
    turtle.speed("fastest")
    if -300 < turtle.xcor() < 300 and -300 < turtle.ycor() < 300 :
        #turtle.color(random.choice(colours))
        r,g,b = random_colour()
        turtle.pencolor((r,g,b))
        turtle.forward(random.randint(30,50))
        turtle.setheading(random.choice(angle))
    else:
        # turtle.color(random.choice(colours))
        r, g, b = random_colour()
        turtle.pencolor((r, g, b))
        turtle.setheading(random.choice(angle))
        turtle.forward(random.randint(0,50))

def spirograph(turtle):
  for i in range(75):
    turtle.pensize(0.5)
    turtle.speed("fastest")
    r, g, b = random_colour()
    turtle.pencolor((r, g, b))
    turtle.circle(100)
    h = turtle.heading()
    turtle.setheading(h + 5)

def hist_paint(tim):
    tim.ht()
    tim.speed("fastest")
    tim.penup()
    tim.hideturtle()
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    number_of_dots = 100
    for dot_count in range(1, number_of_dots + 1):
        r, g, b = random_colour()
        tim.dot(20, (r,g,b))
        tim.forward(50)
        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


#drawdot(15,15,bala_the_turtle)
#dash(bala_the_turtle)
# for i in range(3,11):
#     bala_the_turtle.pensize(15)
#     r,g,b = random_colour()
#     bala_the_turtle.pencolor((r,g,b))
#     draw(i)
#random_walk(bala_the_turtle)
# spirograph(bala_the_turtle)


hist_paint(bala_the_turtle)
screen = Screen()
screen.exitonclick()
