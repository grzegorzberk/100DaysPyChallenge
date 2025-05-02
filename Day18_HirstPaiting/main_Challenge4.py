import turtle as t
import random

player = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color
angles = [0, 90, 180, 270]

player.speed("fastest")
player.pensize(15)

for i in range (150):
    player.color(random_color())
    player.forward(30)
    player.setheading(random.choice(angles))

t.done()