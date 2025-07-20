# from turtle import Turtle, Screen
# import time

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("Snake Game")
# screen.tracer(0)

# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
# snake_segments = []

# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     snake_segments.append(new_segment)


# game_is_on = True
# while game_is_on:
#     time.sleep(0.3)
#     screen.update()
#     for seg_num in range(len(snake_segments) - 1, 0, -1):
#         new_X = snake_segments[seg_num - 1].xcor()
#         new_Y = snake_segments[seg_num - 1].ycor()
#         snake_segments[seg_num].goto(new_X, new_Y)

#     snake_segments[0].forward(20)

# screen.exitonclick()


#######################################
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    snake.move()

screen.exitonclick()