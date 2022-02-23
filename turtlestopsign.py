import math
import turtle
from turtle import *

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

# Size of window
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# Calculations
s = LENGTH
x = s / math.sqrt(2)
diameter = 100 + (2 * x)

# Initialize the turtle.
turtle.speed(ANIMATION_SPEED)


# Turtle Starting Point
turtle.penup()
turtle.goto(-5,150)
turtle.pendown()

# Draw the octagon
color('black', 'red')
begin_fill()
for x in range(NUM_SIDES):
    turtle.forward(s)
    turtle.right(ANGLE)
end_fill()

# Display 'STOP'
turtle.penup()
turtle.goto(TEXT_X,TEXT_Y)
turtle.pendown()
turtle.write("STOP", font=("Calibri", 35, "bold"))
turtle.hideturtle()

