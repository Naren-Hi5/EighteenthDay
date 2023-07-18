'''

Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon


'''

from turtle import Turtle, Screen
import random

mbappe_turtle = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        mbappe_turtle.forward(100)
        mbappe_turtle.right(angle)

for num_sides in range(3, 11):
    mbappe_turtle.color(random.choice(colours))
    draw_shape(num_sides)

screen = Screen()
screen.exitonclick()
