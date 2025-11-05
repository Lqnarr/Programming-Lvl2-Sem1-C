# Mountain range drawing
# By Eric Gao, block C

# Configurations
import turtle
import random

screen_width = 950
screen_height = 600

snow_colour = "WHITE"
mountain_colours = ["gray", "green", "darkgreen", "black"]

start_level = 5
mountain_width = 400
mountain_height = 300
shrink = 0.6

# Setup
screen = turtle.Screen()
screen.title("Cool mountain range with snow on top")
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(2)
turtle.tracer(False)


def draw_triangle(base, height, colour):
    # Helping functions, triangle base for drawing mountains

    t.fillcolor(colour)
    t.pencolor(colour)
    t.begin_fill()

    t.forward(base / 2)
    t.left(120)

    t.forward(height)
    t.left(120)

    t.forward(height)
    t.left(120)

    t.forward(base / 2)
    t.end_fill()


def draw_snowcap(base, height, colour=snow_colour):
    t.fillcolor(colour)
    t.pencolor(colour)
    t.begin_fill()

    t.forward(base * 0.1)
    t.left(120)

    t.forward(height * 0.3)
    t.left(120)

    t.forward(height * 0.3)
    t.left(120)

    t.forward(base * 0.1)
    t.end_fill()


def draw_mountain_range(level, base, height):
    # Recursions, for drawing multiple mountain ranges with different sizes and colours

    if level <= 0 or base < 20 or height < 20:
        return

    start_pos = t.position()
    start_heading = t.heading()

    colour = random.choice(mountain_colours)
    t.pendown()
    draw_triangle(base, height, colour)

    # Drawing the snowcap
    t.penup()
    t.forward(base / 2)
    t.left(145)
    t.forward(height)
    t.right(145)
    t.pendown()
    draw_snowcap(base, height)

    # Reset to base
    t.penup()
    t.goto(start_pos)
    t.setheading(start_heading)
    t.pendown()

    # Recursive: mountains on the left
    t.penup()
    t.goto(start_pos[0] - base * 0.5, start_pos[1])
    t.pendown()
    draw_mountain_range(level - 1, base * shrink, height * shrink)

    # Recursive: mountains on the right
    t.penup()
    t.goto(start_pos[0] + base * 0.5, start_pos[1])
    t.pendown()
    draw_mountain_range(level - 1, base * shrink, height * shrink)


def main():
    # Main function for calling the other functions to start drawing

    t.penup()
    t.goto(0, -screen_height // 4)
    t.setheading(0)
    t.pendown()

    # Start drawing mountains
    draw_mountain_range(start_level, mountain_width, mountain_height)

    turtle.done()


main()
