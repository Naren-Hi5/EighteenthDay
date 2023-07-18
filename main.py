import random
import turtle as t
from turtle import Screen

mbappe_turtle = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


directions = [0, 90, 180, 360]
mbappe_turtle.pensize(15)
mbappe_turtle.speed("fastest")

for _ in range(200):
    mbappe_turtle.color(random_color())
    mbappe_turtle.forward(30)
    mbappe_turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()

#Done and dusted. But some bug is there in the main.py file.
