import turtle as t
import random

tim = t.Turtle()
colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown",
    "black", "white", "gray", "cyan", "magenta", "lime", "maroon", "navy",
    "teal", "olive", "silver", "gold", "violet", "indigo", "coral", "salmon",
    "khaki", "lavender", "turquoise", "azure", "beige", "chocolate"
]

def draw_shape(num_vertices):
    angle = 360/num_vertices
    for _ in range(num_vertices):
        tim.forward(40)
        tim.right(angle)

for x in range(3, 20):
    tim.color(random.choice(colors))
    draw_shape(x)

t.done()