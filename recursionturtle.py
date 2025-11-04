# Mountain range drawing
# By Eric Gao, block C

# Config
import turtle
import random

screen_width = 900
screen_height = 600

snow_colour = "WHITE"
mountain_colours = ["gray", "green", "darkgreen", "black"]

start_level = 5
mountain_width = 200
mountain_height = 150
shrink = 0.6

# Setup
screen = turtle.Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(2)
turtle.tracer(False)


# Drawing triangles
def draw_triangle(base, height, color):
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.forward(base / 2)
    t.left(120)
    t.forward(height)
    t.left(120)
    t.forward(height)
    t.left(120)
    t.forward(base / 2)
    t.end_fill()


def draw_snowcap(base, height, color=snow_colour):
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.forward(base * 0.1)
    t.left(120)
    t.forward(height * 0.3)
    t.left(120)
    t.forward(height * 0.3)
    t.left(120)
    t.forward(base * 0.1)
    t.end_fill()


# ======= RECURSIVE FUNCTION =======
def draw_mountain_range(level, base, height):
    if level <= 0 or base < 20 or height < 20:
        return

    start_pos = t.position()
    start_heading = t.heading()

    colour = random.choice(mountain_colours)
    t.pendown()
    draw_triangle(base, height, colour")

    # Draw snowcap
    t.penup()
    t.forward(base / 2)
    t.left(120)
    t.forward(height)
    t.right(120)
    t.pendown()
    draw_snowcap(base, height)

    # Reset to base
    t.penup()
    t.goto(start_pos)
    t.setheading(start_heading)
    t.pendown()

    # Recursive: left mountain
    t.penup()
    t.goto(start_pos[0] - base * 0.5, start_pos[1])
    t.pendown()
    draw_mountain_range(level - 1, base * shrink, height * shrink)

    # Recursive: right mountain
    t.penup()
    t.goto(start_pos[0] + base * 0.5, start_pos[1])
    t.pendown()
    draw_mountain_range(level - 1, base * shrink, height * shrink)


# ======= MAIN =======
def main():
    t.penup()
    t.goto(0, -screen_height // 4)
    t.setheading(0)
    t.pendown()

    draw_mountain_range(start_level, mountain_width, mountain_height)

    turtle.tracer(True)
    t.hideturtle()
    turtle.done()


main()
