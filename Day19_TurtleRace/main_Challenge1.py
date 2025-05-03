from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def up():
    tim.forward(10)

def back():
    tim.backward(10)

def turnLeft():

    tim.left(10)

def turnRight():

    tim.right(10)

def clear():
    tim.reset()

screen.listen()
screen.onkey(up, "w")
screen.onkey(back, "s")
screen.onkey(turnLeft, "a")
screen.onkey(turnRight ,"d")
screen.onkey(clear, "c")

screen.exitonclick()