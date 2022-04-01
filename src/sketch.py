from turtle import Turtle,Screen

bala = Turtle()
screen = Screen()

screen.listen()
def move_forwards():
   bala.forward(20)
def rotate_right():
    bala.right(15)
def rotate_left():
    bala.left(15)
def move_backward():
   bala.backward(20)
def clear():
    bala.clear()
    bala.penup()
    bala.home()
    bala.pendown()

screen.onkey(key="Up",fun=move_forwards)
screen.onkey(key='Right',fun=rotate_right)
screen.onkey(key='Left',fun=rotate_left)
screen.onkey(key='Down',fun=move_backward)
screen.onkey(key='space',fun=clear)

screen.exitonclick()
