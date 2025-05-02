import colorgram
import turtle as t
import random

def colors_from_file(file_path, num_of_colors):
    colors = colorgram.extract(file_path, num_of_colors)
    color_rgb = [(c.rgb.r, c.rgb.g, c.rgb.b) for c in colors]
    return color_rgb

color_list = colors_from_file("/Users/grzegorzberk/Desktop/100DaysPyChallenge/Day18_HirstPaiting/image.jpg", 12)
turtle = t.Turtle()
t.colormode(255)
turtle.hideturtle()

def draw_dots(color_list, dots_num):
    for _ in range(dots_num):
        turtle.pendown()
        turtle.dot(10, random.choice(color_list))
        turtle.penup()
        turtle.forward(30)

for position in range(10):
    turtle.goto(0, position*30)
    draw_dots(color_list, 10)