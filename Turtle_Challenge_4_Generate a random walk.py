from turtle import Turtle, Screen
import random

mbappe_turtle = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
directions = [0, 90, 180, 360]
mbappe_turtle.pensize(15)
mbappe_turtle.speed(0)

for _ in range(200):
    mbappe_turtle.color(random.choice(colours))
    mbappe_turtle.forward(30)
    mbappe_turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()

#
# Done and dusted