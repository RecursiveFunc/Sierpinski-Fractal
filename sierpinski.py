import turtle


def sierpinski_triangle(t, length, depth):
    if depth == 0:
        for _ in range(3):
            t.forward(length)
            t.left(120)
    else:
        sierpinski_triangle(t, length / 2, depth - 1)
        t.forward(length / 2)
        sierpinski_triangle(t, length / 2, depth - 1)
        t.backward(length / 2)
        t.left(60)
        t.forward(length / 2)
        t.right(60)
        sierpinski_triangle(t, length / 2, depth - 1)
        t.left(60)
        t.backward(length / 2)
        t.right(60)


# Set up the Turtle Graphics
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed

# Initial settings
length = 200  # Size of the triangle
depth = 4  # Number of recursive iterations

# Draw the Sierpinski Triangle
sierpinski_triangle(t, length, depth)

# Complete the drawing
turtle.done()
