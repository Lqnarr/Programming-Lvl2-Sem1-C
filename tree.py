import turtle as t
import random


def draw_complicated_tree(level: int, branch_length: float, thickness: float):
    """Draw a realistic tree recursively."""
    if level == 0:
        # Draw a leaf
        t.color("forest green")
        t.begin_fill()
        t.circle(3)
        t.end_fill()
        t.color("saddle brown")
        return

    # Set branch thickness
    t.pensize(thickness)

    # Set color based on level (darker near trunk, lighter up)
    if level > 4:
        t.color("#4B2E05")  # dark brown trunk
    elif level > 2:
        t.color("#8B5A2B")  # medium brown branch
    else:
        t.color("#A0522D")  # lighter branch

    t.pendown()
    t.forward(branch_length)

    # Random number of sub-branches
    num_branches = random.randint(3, 5)
    for i in range(num_branches):
        # Random angle for each branch
        angle = random.randint(-45, 45)
        t.left(angle)

        # Recursive draw with smaller branch
        draw_complicated_tree(
            level - 1, branch_length * random.uniform(0.6, 0.8), thickness * 0.7
        )

        t.right(angle)

    # Return to base
    t.penup()
    t.backward(branch_length)
    t.pendown()


# --- SETUP ---
t.colormode(255)
t.speed("fastest")
t.left(90)
t.penup()
t.goto(0, -250)
t.pendown()
t.color("#4B2E05")  # dark brown
t.pensize(12)

# --- DRAW TREE ---
draw_complicated_tree(level=7, branch_length=90, thickness=12)

t.hideturtle()
t.done()
