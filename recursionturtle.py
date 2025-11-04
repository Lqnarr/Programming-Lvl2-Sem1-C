# Mountain Range - Fixed Layout
import turtle
import random

# ======= CONFIG =======
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
BACKGROUND = "skyblue"

MOUNTAIN_COLORS = ["dimgray", "gray", "darkslategray", "slategray"]
SNOW_COLOR = "white"

START_LEVEL = 5
MOUNTAIN_WIDTH = 200
MOUNTAIN_HEIGHT = 150
SHRINK = 0.6
GREENCOLOR = "GREEN"

# ======= TURTLE SETUP =======
screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(2)
turtle.tracer(False)


# ======= HELPER FUNCTIONS =======
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


def draw_snowcap(base, height, color=SNOW_COLOR):
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

    color = random.choice(MOUNTAIN_COLORS)
    t.pendown()
    draw_triangle(base, height, GREENCOLOR)

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
    draw_mountain_range(level - 1, base * SHRINK, height * SHRINK)

    # Recursive: right mountain
    t.penup()
    t.goto(start_pos[0] + base * 0.5, start_pos[1])
    t.pendown()
    draw_mountain_range(level - 1, base * SHRINK, height * SHRINK)


# ======= MAIN =======
def main():
    t.penup()
    t.goto(0, -SCREEN_HEIGHT // 4)
    t.setheading(0)
    t.pendown()

    draw_mountain_range(START_LEVEL, MOUNTAIN_WIDTH, MOUNTAIN_HEIGHT)

    turtle.tracer(True)
    t.hideturtle()
    turtle.done()


main()
