import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Obstaw żółwia",
                             prompt="Który żółw wygra ten wyścig? "
                             "(red, orange, yellow, green, blue, purple) Podaj kolor: ")
colors=["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
start_cordX = -230
start_cordY = -100

is_race_on = False

for x in range(0, 6):
    next_posY = start_cordY + (40*x)
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(x=start_cordX, y=next_posY)
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.textinput(title="Gratulacje", 
                                 prompt="Twój żółw wygrał ten wyścig!")
            else:
                screen.textinput(title="Przegrałeś", prompt=(f"Wygrał żółw {winning_color}"))


screen.exitonclick()