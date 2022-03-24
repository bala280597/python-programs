import turtle
from turtle import Turtle, Screen
import random
bala_the_turtle = Turtle()
bala_the_turtle.shape("turtle")
bala_the_turtle.color("brown")
def square():
    for i in range(0,4):
        turtle.dot(20,"blue")
        bala_the_turtle.forward(100)
        bala_the_turtle.right(90)


def drawdot(space, x,tur):
    for i in range(x):
        for j in range(x):
            tur.dot()

            tur.forward(space)
        tur.backward(space * x)

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
def random_walk(turtle):
  while True:
    angle = [90,270,180,360]
    turtle.pensize(15)
    turtle.speed("fastest")
    if -300 < turtle.xcor() < 300 and -300 < turtle.ycor() < 300 :
        turtle.color(random.choice(colours))
        turtle.forward(random.randint(30,50))
        turtle.setheading(random.choice(angle))
    else:
        turtle.color(random.choice(colours))
        turtle.setheading(random.choice(angle))
        turtle.forward(random.randint(0,50))


# drawdot(10, 8,bala_the_turtle)
# dash(bala_the_turtle)
# for i in range(3,11):
#     bala_the_turtle.color(random.choice(colours))
#     draw(i)
#random_walk(bala_the_turtle)


screen = Screen()
screen.exitonclick()
