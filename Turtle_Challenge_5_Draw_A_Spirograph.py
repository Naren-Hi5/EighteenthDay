import random
import turtle as t

mbappe_turtle = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour

mbappe_turtle.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        mbappe_turtle.color(random_color())
        mbappe_turtle.circle(100)
        mbappe_turtle.setheading(mbappe_turtle.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()


