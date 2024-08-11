import turtle


def dragon_curve(t, length, depth, sign):
    if depth == 0:
        t.forward(length)
    else:
        t.left(45 * sign)
        dragon_curve(t, length / (2**0.5), depth - 1, 1)
        t.right(90 * sign)
        dragon_curve(t, length / (2**0.5), depth - 1, -1)
        t.left(45 * sign)


# Set up the Turtle Graphics
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed

# Initial settings
length = 200  # Length of the initial line segment
depth = 11  # Number of recursive iterations

# Draw the Dragon Curve
t.penup()
t.goto(-length // 2, 0)  # Start position
t.pendown()
dragon_curve(t, length, depth, 1)

# Complete the drawing
turtle.done()
