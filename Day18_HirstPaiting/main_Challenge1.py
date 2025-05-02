import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
for x in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)
t.done()