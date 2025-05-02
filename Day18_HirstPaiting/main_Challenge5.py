import turtle as t
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

t.colormode(255)
turtle = t.Turtle()
turtle.speed("fastest")

for angle in range(0, 361, 3):
    turtle.color(random_color())
    turtle.circle(70)
    turtle.setheading(angle)

t.done()